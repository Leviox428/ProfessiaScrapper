import requests
from bs4 import BeautifulSoup as bs
from concurrent.futures import ThreadPoolExecutor, as_completed


class WebScrapper():
    def __init__(self):
        self.mainUrl = "https://www.profesia.sk"
        self.jobPostingsByRegion = {}
        self.regionLinks = []
        self.soup = None
        
        response = requests.get(self.mainUrl)
        if response:
            self.soup = bs(response.content, "html.parser")

    def PerformWebScrapping(self):
        if not self.soup:
            return 
        
        ul = self.soup.find("ul", class_="regions")
        if not ul:
            return 
        #gets li tags from ul which contains a tag with "kraj" substring
        liTags = [
            li for li in ul.find_all("li")
            if li.find("a") and "kraj" in li.find("a").get_text(strip=True).lower()
        ] 
        #fills the dictionary with name of region as key and number of jobs as value
        self.jobPostingsByRegion = {
            li.find("a").get_text(strip=True): int(li.find("span").get_text(strip=True).replace(" ", ""))
            for li in liTags
        }        
        self.regionLinks = [li.find("a")["href"] for li in liTags]
        self.ScrapeAllRegions()


       
    def ScrapeAllRegions(self):
        if not self.regionLinks:
            return
        for regionLink in self.regionLinks:
            self.ScrapeRegion(regionLink)

    def ScrapeRegion(self, regionLink):
        regionJobs = []
        with ThreadPoolExecutor(maxWorkers=10) as executor:  
            futures = [executor.submit(self.ScrapePage, regionLink, page) for page in range(1, 51)]
            for future in as_completed(futures):
                regionJobs.extend(future.result())

    def ScrapePage(self, regionLink, page):
        fullLink = self.mainUrl + f"{regionLink}/?page_num={page}"

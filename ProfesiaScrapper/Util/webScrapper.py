import requests
from bs4 import BeautifulSoup as bs
from concurrent.futures import ThreadPoolExecutor, as_completed

class WebScrapper():
    def __init__(self):
        self.mainUrl = "https://www.profesia.sk"
        self.jobCountRegions = {}
        self.regionLinks = []
        self.soup = None
        
        response = requests.get(self.mainUrl)
        if response:
            self.soup = bs(response.content, "html.parser")
            self.FindRegionLinks()

    def FindRegionLinks(self):
        if not self.soup:
            return 
        
        ul = self.soup.find("ul", class_="regions")
        if not ul:
            return 
        #getting li tags from ul which contains a tag with "kraj" substring
        liTags = [
            li for li in ul.find_all("li")
            if li.find("a") and "kraj" in li.find("a").get_text(strip=True).lower()
        ] 
        #
        self.jobCountRegions = {
            li.find("a").get_text(strip=True): int(li.find("span").get_text(strip=True).replace(" ", ""))
            for li in liTags
        }        
        self.regionLinks = [li.find("a")["href"] for li in liTags]


       
    def ScrapeAllRegions(self, daysCount):
        if not self.regionLinks:
            return
        for regionLink in self.regionLinks:
            self.ScrapeRegion(regionLink, daysCount)

    def ScrapeRegion(self, regionLink, daysCount):
        regionJobs = []
        with ThreadPoolExecutor(maxWorkers=10) as executor:  # Adjust number of threads as needed
            futures = [executor.submit(self.ScrapePage, regionLink, daysCount, page) for page in range(1, 51)]
            for future in as_completed(futures):
                regionJobs.extend(future.result())

    def ScrapePage(self, regionLink, daysCount, page):
        fullLink = self.mainUrl + f"{regionLink}?count_days={daysCount}&page_num={page}"

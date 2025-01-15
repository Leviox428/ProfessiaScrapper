import requests
from bs4 import BeautifulSoup as bs
from concurrent.futures import ThreadPoolExecutor, as_completed
from DataModels.jobPost import JobPost
import re


class WebScrapper():
    def __init__(self):
        self.mainUrl = "https://www.profesia.sk"
        self.jobPostingsAndAverageWageByRegion = {}
        self.regionLinks = {}
        self.jobs = []
        self.soup = None
        
        response = requests.get(self.mainUrl)
        if response:
            self.soup = bs(response.content, "html.parser")

    def GetNumOfJobPostingsAndAverageWages(self):
        return self.jobPostingsAndAverageWageByRegion

    def GetJopPosts(self):
        return self.jobs

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
        self.jobPostingsAndAverageWageByRegion = {
            li.find("a").get_text(strip=True): [int(li.find("span").get_text(strip=True).replace(" ", ""))]
            for li in liTags
        }
        self.regionLinks = {
            li.find("a").get_text(strip=True): li.find("a")["href"] for li in liTags
        }
        if not self.regionLinks:
            return
        with ThreadPoolExecutor() as executor:
            executor.map(lambda item: self.ScrapeRegion(item[0], item[1]), self.regionLinks.items())

    def ScrapeRegion(self, region, regionLink):
        try:
            sumOfJobWages = 0
            numOfJobs = 0
            for i in range (1, 50):
                fullLink = self.mainUrl + f"{regionLink}?page_num={i}"
                response = requests.get(fullLink)
                if not response:
                    return
                self.soup = bs(response.content, "html.parser")
                if not self.soup:
                    return
                ul = self.soup.find("ul", class_="list")
                if not ul:
                    return 
                liTags = [
                    li for li in ul.find_all("li", class_="list-row")
                ] 
                for liTag in liTags:
                    wage = self.GetWageFromLabel(liTag)
                    if wage > 0:
                        sumOfJobWages += wage
                        numOfJobs += 1
                    self.ScrapeJobPost(liTag, region)
            averageWageInRegion = sumOfJobWages / numOfJobs
            if region in self.jobPostingsAndAverageWageByRegion:
                self.jobPostingsAndAverageWageByRegion[region].append(averageWageInRegion)
        except Exception as e:
            i = 0
            
    def GetWageFromLabel(self, liTag):
        try:
            span = liTag.find("span", class_="label-group")
            if not span:
                return 0
            a = span.find("a")
            wageLabel = a.find("span", class_="label")
            wageLabelText = wageLabel.get_text(strip=True)
            matchWage = re.search(r'(\d[\d\s]*)\s*(?:EUR|eur)?\s*\/mesiac', wageLabelText, re.IGNORECASE)
            matchHourly = re.search(r'(\d[\d\s]*)\s*(?:EUR|eur)?\s*\/hod', wageLabelText, re.IGNORECASE)
            if matchWage:
                return int(matchWage.group(1).replace(" ", ""))
            elif matchHourly:
                return self.CalculateMothlyWage(int(matchHourly.group(1).replace(" ", "")))
            else:
                return 0
        except Exception as e:
            return 0

    def CalculateMothlyWage(self, hourWage):
        hoursPerDay = 8
        daysPerWeek = 5
        weeksPerMonth = 4.33
        if not hourWage:
            return 0
        return hourWage * hoursPerDay * daysPerWeek * weeksPerMonth

    def ScrapeJobPost(self, liTag, region):
        spanEmployer = liTag.find("span", class_="employer")
        spanJobLocation = liTag.find("span", class_="job-location")
        spanWge = liTag.find("span", class_="label-group")
        spanTitle = liTag.find("span", class_="title")
        wage = 0
        if spanWge:
             a = spanWge.find("a")
             wageLabel = a.find("span", class_="label")
             wage = wageLabel.get_text()
        employer = spanEmployer.get_text()
        title = spanTitle.get_text()
        jobLocation = spanJobLocation.get_text()
        jobPost = JobPost(region, wage, employer, jobLocation, title)
        self.jobs.append(jobPost)


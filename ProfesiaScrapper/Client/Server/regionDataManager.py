import requests
from DataModels.region import Region

class RegionDataManager():
    regions = []
    @staticmethod
    def LoadRegionDataFromServer():
        url = "http://127.0.0.1:5000/data/get-data"
        try:
            # Make the GET request
            response = requests.get(url)
            
            # Check if the response was successful (status code 200)
            if response.status_code == 200:
                result = response.json()
                for region, values in result.items():
                    region = Region(regionName=region, numOfJobPostings=values[0], averageWage=values[1])
                    RegionDataManager.regions.append(region)
            return "Error retrieving data"

        except requests.exceptions.RequestException:
            return 
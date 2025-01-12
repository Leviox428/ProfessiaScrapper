import requests
from DataModels.user import User

class UserDataManager():
    user = None
    def __init__(self):
        self.userEndpoint = "http://127.0.0.1:5000/user"

    def FindUserByEmail(self, email):
        url = f"{self.userEndpoint}/find-user-by-email?email={email}"
        try:
            # Make the GET request
            response = requests.get(url)
            
            # Check if the response was successful (status code 200)
            if response.status_code == 200:
                result = response.json()
                if "user" in result:
                    userData = result["user"]
                    userID = userData.get("userID")
                    email = userData.get("email")
                    username = userData.get("username")
                    UserDataManager.user = User(userID, username, email)
                    return "Success"  
                else:
                    return {"error": "User not found"}
            elif response.status_code == 404:
                return {"error": "User not found"}
            else:
                return {"error": f"An error occurred: {response.status_code}"}

        except requests.exceptions.RequestException as e:
            return {"error": f"Request failed: {str(e)}"}
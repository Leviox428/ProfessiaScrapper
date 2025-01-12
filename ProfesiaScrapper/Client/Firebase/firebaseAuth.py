import requests
import os
from DataModels.user import User
from Server.userDataManager import UserDataManager
from dotenv import load_dotenv

class FirebaseAuth:
    user = None

    def __init__(self):
        load_dotenv()
        self.serverUrl = "http://127.0.0.1:5000/user"
        self.API_KEY = os.getenv('API_KEY')
    
    def LoginUser(self, email, password):
        url = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={self.API_KEY}"
        payload = {
            "email": email,
            "password": password,
            "returnSecureToken": True
        }
        response = requests.post(url, json=payload)
        if response.status_code != 200:
            return "Wrong login credentials"
        userDataManager = UserDataManager()
        message = userDataManager.FindUserByEmail(email)
        return message


    def RegisterUser(self, email, password, username):
        url = f"https://identitytoolkit.googleapis.com/v1/accounts:signUp?key={self.API_KEY}"
        payload = {
            "email": email,
            "password": password,
            "returnSecureToken": True
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code != 200:
                return "Error registering user"
            data = response.json()
            userData = {
                "username": username,
                "userID": data["localId"],
                "email": email
            }
            endpoint = "/create-user"
            response = requests.post(f"{self.serverUrl}{endpoint}", json=userData)
            if response.status_code != 201:
                self.DeleteUser(data["idToken"])
                return "Error creating user in db"   
            FirebaseAuth.user = User(data["localId"], username, email)
            return "User registered successfully"
        except Exception:
            return "Unknown error occured"

    def DeleteUser(self, idToken):
        url = f"https://identitytoolkit.googleapis.com/v1/accounts:delete?key={self.API_KEY}"
        payload = {
            "idToken": idToken
        }
        response = requests.post(url, json=payload)


import requests
import os
from Firebase.Database.userManager import UserManager
from Firebase.Database.DataModels.user import User
from dotenv import load_dotenv

class FirebaseAuth:
    user = None

    def __init__(self):
        load_dotenv()
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
            return False
        userDocument = UserManager.FindUserByEmail(email)
        if not userDocument.exists:
            return False
        
        id = userDocument.id
        username = userDocument.to_dict().get("username")

        FirebaseAuth.user = User(id, username, email)

        return True


    def RegisterUser(self, email, password, username):
        url = f"https://identitytoolkit.googleapis.com/v1/accounts:signUp?key={self.API_KEY}"
        payload = {
            "email": email,
            "password": password,
            "returnSecureToken": True
        }
        response = requests.post(url, json=payload)
        if response.status_code != 200:
            return False
        data = response.json()
        success = UserManager.CreateUser(data["localId"], username, email)
        if not success: 
            self.DeleteUser(data["idToken"])
            return False   
        FirebaseAuth.user = User(data["localId"], username, email)
        return True

    def DeleteUser(self, idToken):
        url = f"https://identitytoolkit.googleapis.com/v1/accounts:delete?key={self.API_KEY}"
        payload = {
            "idToken": idToken
        }
        response = requests.post(url, json=payload)


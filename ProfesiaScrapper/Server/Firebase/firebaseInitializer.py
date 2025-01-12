import firebase_admin
from firebase_admin import credentials, firestore

class FirebaseInitializer:
    db = None
        
    @staticmethod
    def Initialize():
        service_account_path = "ProfesiaScrapper/Server/Firebase/serviceAccountKey.json"

        cred = credentials.Certificate(service_account_path)
        firebase_admin.initialize_app(cred)

        FirebaseInitializer.db = firestore.client()

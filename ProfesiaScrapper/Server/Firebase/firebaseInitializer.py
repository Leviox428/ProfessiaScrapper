import firebase_admin
from firebase_admin import credentials, firestore

class FirebaseInitializer:
    db = None
    @staticmethod
    def Initialize():
        try:
            service_account_path = "ProfesiaScrapper\Server\Firebase\serviceAccountKey2.json"
            cred = credentials.Certificate(service_account_path)
            firebase_admin.initialize_app(cred)
            db = firestore.client()
            FirebaseInitializer.db = db
            print("Firebase initialized successfully!")
        except Exception as e:
            print(f"Error initializing Firebase: {e}")


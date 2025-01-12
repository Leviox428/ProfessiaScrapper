from Firebase.firebaseInitializer import FirebaseInitializer

class DataManager:
    @staticmethod
    def GetData():
        try:
            docRef = FirebaseInitializer.db.collection("data").document("data")
            doc = docRef.get()
            if doc.exists():
                return docRef.to_dict()
            else:
                return None
        except Exception:
            return None 
         
    @staticmethod
    def SetData(data):
        try:
            docRef = FirebaseInitializer.db.collection("data").document("data")
            doc = docRef.get()
            if doc.exists():
                docRef.set(data)
                return True
        except Exception:
            return False

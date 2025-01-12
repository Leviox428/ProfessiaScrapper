from Firebase.firebaseInitializer import FirebaseInitializer

class UserManager:
    @staticmethod
    def CreateUser(id, username, email):
        try:
            FirebaseInitializer.db.collection("users").document(id).set({"username": username, "email": email})
            return True  
        except Exception as e:
            return False  
    @staticmethod
    def FindUserByEmail(email):
        query = FirebaseInitializer.db.collection("users").where(field_path='email', op_string='==', value=email).get()
        doc = query[0]
        return doc

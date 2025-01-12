from Firebase.firebaseInitializer import FirebaseInitializer
class DataWriter:
    def __init__(self):
        self.db = FirebaseInitializer.db
    def SaveDataToDB(self, data):
        collectionRef = self.db.collection('data')
        for regionName, values in data.items():
            numOfJobPostings, averageWageOfRegion = values
            docRef = collectionRef.document(regionName)
            docRef.set({
            'numOfJobPostings': numOfJobPostings,
            'averageWageOfRegion': averageWageOfRegion
        })
from Firebase.firebaseInitializer import FirebaseInitializer
class DataWriter:
    def __init__(self):
        self.db = FirebaseInitializer.db
    def SaveRegionDataToDB(self, data):
        collectionRef = self.db.collection('data')
        for regionName, values in data.items():
            numOfJobPostings, averageWageOfRegion = values
            docRef = collectionRef.document(regionName)
            docRef.set({
            'numOfJobPostings': numOfJobPostings,
            'averageWageOfRegion': averageWageOfRegion
        })
    def SaveJobPostsToDB(self, data):
        collectionRef = self.db.collection('jobs')
        for jobPost in data:
            collectionRef.add({
                'Region': jobPost.regionName,
                'Wage': jobPost.wage,
                'Employer': jobPost.employer,
                'Job location': jobPost.jobLocation
            })
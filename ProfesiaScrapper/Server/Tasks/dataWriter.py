from Firebase.firebaseInitializer import FirebaseInitializer
import concurrent.futures
import threading

class DataWriter:
    def __init__(self):
        self.db = FirebaseInitializer.db
        self.totalDeleted = 0
        self.numOfOldCDocs = 0
    def SaveRegionDataToDB(self, data):
        collectionRef = self.db.collection('data')
        for regionName, values in data.items():
            if len(values) == 1:
                continue
            numOfJobPostings, averageWageOfRegion = values
            docRef = collectionRef.document(regionName)
            docRef.set({
            'numOfJobPostings': numOfJobPostings,
            'averageWageOfRegion': averageWageOfRegion
        })
            
    def SaveJobPostsToDB(self, data):
        collectionRef = self.db.collection('jobs')
        docs = collectionRef.stream()
        self.numOfOldCDocs = len(list(docs))
        print("Deleting old data...")
        self.DeleteOldData(collectionRef, 500)
        print("Deleting old data done")
        print("Saving new data")
        for jobPost in data:
            collectionRef.add({
                'Region': jobPost.regionName,
                'Wage': jobPost.wage,
                'Employer': jobPost.employer,
                'Job location': jobPost.jobLocation
            })
    def DeleteOldData(self, collectionRef, batchSize, maxThreads=4):
        docs = list(collectionRef.limit(batchSize).stream())
        if not docs:
            return
        lock = threading.Lock()
        def DeleteDocument(doc):
            doc.reference.delete()
            with lock:  # Ensure only one thread updates `self.totalDeleted` and prints
                print(f"Deleted files: {self.totalDeleted}/{self.numOfOldCDocs}", end='\r', flush=True)
                self.totalDeleted += 1

        with concurrent.futures.ThreadPoolExecutor(maxThreads) as executor:
            executor.map(DeleteDocument, docs)


        self.DeleteOldData(collectionRef, batchSize)
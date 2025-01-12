from flask import Blueprint, jsonify, request, abort
from Firebase.firebaseInitializer import FirebaseInitializer

db = FirebaseInitializer.db
dataRoutesBlueprint = Blueprint('data', __name__)

@dataRoutesBlueprint.route('/get-data', methods=['GET'])
def getData():
    try:
        collectionRef = db.collection('data') 
        docs = collectionRef.stream()
        regionsData = {}
        for doc in docs:
            regionName = doc.id
            regionData = doc.to_dict()
            numOfJobPostings = regionData.get('numOfJobPostings')
            averageWageOfRegion = regionData.get('averageWageOfRegion')
            regionsData[regionName] = [numOfJobPostings, averageWageOfRegion]
        return jsonify(regionsData), 200
    except Exception:
        abort(500)
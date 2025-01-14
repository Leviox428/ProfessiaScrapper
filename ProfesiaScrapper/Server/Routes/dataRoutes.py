from flask import Blueprint, jsonify, request, abort
from Firebase.firebaseInitializer import FirebaseInitializer

dataRoutesBlueprint = Blueprint('data', __name__)

@dataRoutesBlueprint.route('/get-data', methods=['GET'])
def GetData():
    try:
        db = FirebaseInitializer.db
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
    except Exception as e:
        abort(500)
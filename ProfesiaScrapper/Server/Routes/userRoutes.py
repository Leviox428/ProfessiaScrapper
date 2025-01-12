from flask import Blueprint, jsonify, request, abort
from Firebase.firebaseInitializer import FirebaseInitializer

userRoutesBlueprint = Blueprint('user', __name__)

@userRoutesBlueprint.route('/create-user', methods=['POST'])
def CreateUser():
    try:
        db = FirebaseInitializer.db
        userID = request.json.get('userID')
        email = request.json.get('email')
        username = request.json.get('username')

        if not userID or not email:
            return jsonify({"error": "userID and email are required"}), 400

        collectionRef = db.collection('users')

        collectionRef.document(userID).set({
            'email': email,
            'username': username
        })

        return jsonify({"message": "User created successfully"}), 201  

    except Exception as e:
        print(f"Error creating user: {e}")
        return jsonify({"error": "An internal server error occurred"}), 500  
    

@userRoutesBlueprint.route('/find-user-by-email', methods=['GET'])
def FindUserByEmail():
    try:
        db = FirebaseInitializer.db
        email = request.args.get('email')

        if not email:
            return jsonify({"error": "Email is required"}), 400

        usersRef = db.collection('users')
        query = usersRef.where('email', '==', email)
        results = query.stream()
        userData = None
        for doc in results:
            userData = doc.to_dict()
            userData['userID'] = doc.id  
            break  

        if userData:
            return jsonify({"user": userData}), 200
        else:
            return jsonify({"error": "User not found"}), 404

    except Exception as e:
        print(f"Error finding user by email: {e}")
        return jsonify({"error": "An internal server error occurred"}), 500
"""
Python Wrapper to handle sessions with MongoDB
"""

from pymongo import MongoClient

def getDB():
    """
    Returns the MongoDB database
    """
    client = MongoClient('mongodb+srv://rmadith:Adithya12@cluster0.hlcg26s.mongodb.net/?retryWrites=true&w=majority', 27017)
    db = client['Musix']
    return db

def createsession(host_id):
    """
    Creates a session with MongoDB
    Returns the new session ID
    """
    session_collection = getDB()["Session"]
    session_sample_document = {"users": {}, "host": host_id}
    new_document = session_collection.insert_one(session_sample_document)
    return new_document.inserted_id

def addUserToSession(session_id, user_id, access_token, refresh_token):
    """
    Adds a user to a session
    """
    try:
        # Check if the user is the host
        if user_id == session_collection.find_one({"_id": session_id})["host"]:
            return False
            
        session_collection = getDB()["Session"]
        # Get the users array
        users = session_collection.find_one({"_id": session_id})["users"]
        # Add the user to the array
        users[user_id] = {"access_token": access_token, "refresh_token": refresh_token}
        session_collection.update_one({"_id": session_id}, {"$set": {"users": users}})
        return True
    except:
        return False
    
def deleteUserFromSession(session_id, user_id):
    """
    Deletes a user from a session
    """
    try:
        session_collection = getDB()["Session"]
        # Get the users array
        users = session_collection.find_one({"_id": session_id})["users"]
        # Delete the user from the array
        del users[user_id]
        session_collection.update_one({"_id": session_id}, {"$set": {"users": users}})
        return True
    except:
        return False
    
def deleteSession(session_id):
    """
    Deletes a session
    """
    try:
        session_collection = getDB()["Session"]
        session_collection.delete_one({"_id": session_id})
        return True
    except:
        return False
    
    
def addUser(email, access_token, refresh_token):
    """
    Adds a user to the database
    """
    try:
        user_collection = getDB()["User"]
        if user_collection.find_one({"email": email}) != None:
            x = user_collection.update_one({"email": email}, {"$set": {"access_token": access_token, "refresh_token": refresh_token}})
            # Return the ID of the user
            return user_collection.find_one({"email": email})["_id"]
        x = user_collection.insert_one({"email": email, "access_token": access_token, "refresh_token": refresh_token})
        return x.inserted_id
    except:
        return False
    
def getUser(id):
    """
    Gets a user from the database
    """
    return getDB()["User"].find_one({"_id": id})



    


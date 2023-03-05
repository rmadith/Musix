"""
Python Wrapper to handle sessions with MongoDB
"""

import json
from pymongo import MongoClient

def getDB():
    """
    Returns the MongoDB database
    """
    client = MongoClient('mongodb+srv://rmadith:Adithya12@cluster0.hlcg26s.mongodb.net/?retryWrites=true&w=majority', 27017)
    db = client['Musix']
    return db

def createsession(host_id, type):
    """
    Creates a session with MongoDB
    Returns the new session ID
    """
    session_collection = getDB()["Session"]
    session_sample_document = {"users": {}, "host": host_id, "type": type}
    new_document = session_collection.insert_one(session_sample_document)
    return new_document.inserted_id

def addUserToSession(session_id, user_id):
    """
    Adds a user to a session
    """
    try:    
        session_collection = getDB()["Session"]
        # Get the users array
        users = session_collection.find_one({"_id": session_id})["users"]
        # Add the user to the array
        users[user_id] = True
        user = getDB()["User"].find_one({"_id": user_id})
        user["activeSessions"][session_id] = True
        getDB()["User"].update_one({"_id": user_id}, {"$set": {"activeSessions": user["activeSessions"]}})
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
        user = getDB()["User"].find_one({"_id": user_id})
        del user["activeSessions"][session_id]
        getDB()["User"].update_one({"_id": user_id}, {"$set": {"activeSessions": user["activeSessions"]}})
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
        x = user_collection.insert_one({"email": email, "access_token": access_token, "refresh_token": refresh_token, "activeSessions": {}, "topArtists": {}, "topTracks": {}, "streaming": False})
        return x.inserted_id
    except:
        return False
    
def getUser(ides):
    """
    Gets a user from the database
    """
    return getDB()["User"].find_one({"_id": ides})

def getUsersinSession(session_id):
    """
    Gets all the users in a session
    """
    x = getDB()["Session"].find_one({"_id": session_id})["users"]
    y = []
    for i in x:
        y.append(getUser(i))
    return json.dumps(y)



    
def getUserSession(id):
    """
    Gets a user's active sessions
    """
    return getDB()["User"].find_one({"_id": id})["activeSessions"]

def getAuth(id):
    return getDB()["User"].find_one({"_id": id})["access_token"]
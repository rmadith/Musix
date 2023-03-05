#!/usr/bin/env python3
"""
Spotify Calls using Authorizaation Code
"""

import requests

"""
Get the user's profile information
Required Scopes - 
	user-read-private

Parameters: Authorization Code (Accessed from DB)
Returns: JSON Object if Authorized, False if Unauthorized or Rate Limited
"""
def getme(authcode:str):
	headers = {
		"Authorization": "Authorization: Bearer " + authcode,
		"Content-Type": "application/json",
        
	}
	r = requests.get("https://api.spotify.com/v1/me", headers=headers)
    
	if r.status_code == 200:
		return r.json()
	
	if r.status_code == 401 or r.status_code == 403:
		return False
	
	if r.status_code == 429:
		return False
    
	return False


"""
Get User's Top {Anything}
Required Scopes -
	N/A

Parameters: Authorization Code (Accessed from DB)
Returns: JSON Object if Authorized, False if Unauthorized or Rate Limited
"""
def gettop(authcode:str, type:str, limit:int=3):
	headers = {
		"Authorization": "Authorization: Bearer " + authcode,
		"Content-Type": "application/json",
		"Accept": "application/json"
	}

	r = requests.get("https://api.spotify.com/v1/me/top/"+type+"?time_range=short_term&limit="+str(limit), headers=headers)

	if r.status_code == 200:
		return r.json()
	
	if r.status_code == 401 or r.status_code == 403:
		return False
	
	if r.status_code == 429:
		return False
	
	return False
	
"""
Get Spotify Playlist
Required Scopes -
	N/A

Parameters: Authorization Code (Accessed from DB)
Returns: JSON Object if Authorized, False if Unauthorized or Rate Limited
"""
def getplaylist(authcode:str, playlistid:str):
	headers = {
		"Authorization": "Authorization: Bearer " + authcode,
		"Content-Type": "application/json",
		"Accept": "application/json"
	}

	r = requests.get("https://api.spotify.com/v1/playlists/"+playlistid, headers=headers)

	if r.status_code == 200:
		return r.json()
	
	if r.status_code == 401 or r.status_code == 403:
		return False
	
	if r.status_code == 429:
		return False
	
	return False

"""
Add Songs to Spotify Queue
Required Scopes -
	user-modify-playback-state

Parameters: Authorization Code (Accessed from DB) and Song URI
Does not return anything
"""
def addtoQueue(authcode:str, trackID:str):
	headers = {
		"Authorization": "Authorization: Bearer " + authcode,
		"Content-Type": "application/json",
		"Accept": "application/json"
	}

	r = requests.post("https://api.spotify.com/v1/me/player/queue?uri="+trackID, headers=headers)

	if r.status_code == 204:
		return True
	
	if r.status_code == 401 or r.status_code == 403:
		return False
	
	if r.status_code == 429:
		return False
	
	return False

"""
Search Spotify
Required Scopes -
	N/A

Parameters: Authorization Code (Accessed from DB) and Search Query
Returns: JSON Object if Authorized, False if Unauthorized or Rate Limited
"""
def getSong(authcode:str, Song:str):
	headers = {
		"Authorization": "Authorization: Bearer " + authcode,
		"Content-Type": "application/json",
		"Accept": "application/json"		
	}

	r = requests.get("https://api.spotify.com/v1/search?q="+Song+"&type=track&limit=10", headers=headers)

	if r.status_code == 200:
		return r.json()
	
	if r.status_code == 401 or r.status_code == 403:
		return False
	
	if r.status_code == 429:
		return False
	
	return False


def test():
	return "Function call successful"


#!/usr/bin/env python

"""
Minimal Song Class designed to hold all Spotify Information required for musix
Parameters  - 
	Track - String
	TrackID - String (base64)
	Image - String (URL)
	Key - Integer
"""

class Song(object):

	# Constructor for Song Class
	def __init__(self, track, trackID, image, key):
		self.track = track
		self.trackID = trackID
		self.image = image
		self.key = 0
		self.played = False

	# String representation of Song Class
	def __str__(self):
		return self.track
	
	# Compare two Song Objects
	def __eq__(self, other):
		if other == None or not isinstance(other, Song):
			return False
		return self.trackID == other.trackID
	
	def __ne__(self, other):
		if other == None or not isinstance(other, Song):
			return True
		return self.trackID != other.trackID
	
	# Required Getters and Setters for Song Class
	def incrementKey(self):
		self.key += 1

	def zeroKey(self):
		self.key = 0

	def getPlayed(self):
		return self.played
	
	def setPlayed(self, played):
		self.played = played

	def getKey(self):
		return self.key
	
	
	


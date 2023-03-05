#!/usr/bin/env python

"""
Minimal Hashmap Class designed to hold all Song Objects
Parameters  -
    Key - Song TrackID
    Value - Song Object
"""

class HashMap(object):

    # Constructor for HashMap Class
    def __init__(self):
        self.hashmap = {}

    # String representation of HashMap Class
    def __str__(self):
        return str(self.hashmap)
    
    # Add a Song Object to the HashMap
    def add(self, key, value):
        self.hashmap[key] = value

    # Get a Song Object from the HashMap
    def get(self, key):
        return self.hashmap[key]
    
    # Remove a Song Object from the HashMap
    def remove(self, key):
        del self.hashmap[key]

    # Check if a Song Object is in the HashMap
    def contains(self, key):
        return key in self.hashmap
    
    # Check if the HashMap is empty
    def isEmpty(self):
        return len(self.hashmap) == 0
    
    # Get the size of the HashMap
    def size(self):
        return len(self.hashmap)




#!/usr/bin/env python

"""
Minimal Hashed Priority Queue Class designed to hold all Song Objects
Parameters  -
    Value - Song Object
"""
import HashMap
import PriorityQueue
import Song

class HashedQueue(object):
    def __init__(self):
        self.hashmap = HashMap.HashMap()
        self.priorityqueue = PriorityQueue.PriorityQueue()
    
    def add(self, song):
        if self.hashmap.contains(song.trackID):
            self.hashmap.get(song.trackID).incrementKey()
        
        else:
            self.hashmap.add(song.trackID, song)
            self.priorityqueue.insert(song)
    
    def pop(self, *args):
        if len(args) == 0:
            try:
                songs = self.priorityqueue.pop()
                self.hashmap.get(songs.trackID).zeroKey()
            except:
                songs = []
        else:
            songs = []
            for i in range(args[0]):
                try:
                    song = self.priorityqueue.pop()
                    self.hashmap.get(song.trackID).zeroKey()
                    songs.append(song)
                except:
                    pass
        self.priorityqueue.insertionSort()
        return songs
    
    def contains(self, key):
        return self.hashmap.contains(key)
    
    def isEmpty(self):
        return self.hashmap.isEmpty()
    
    def size(self):
        return self.hashmap.size()

    def __str__(self):
        return str(self.priorityqueue)




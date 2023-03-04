#!/usr/bin/env python
# coding: utf-8

# In[3]:


"""
Tester method for HashMap Class
"""
import Song
import HashMap


# In[27]:


def test():
    #check add
    hashmap = HashMap.HashMap()
    song1 = Song.Song("Track1", "TrackID1", "Image1", 1)
    song2 = Song.Song("Track2", "TrackID2", "Image2", 2)
    song3 = Song.Song("Track3", "TrackID3", "Image3", 0)
    song4 = Song.Song("Track4", "TrackID4", "Image4", 3)
    song5 = Song.Song("Track5", "TrackID5", "Image5", 10)
    
    hashmap.add(1, song1)
    hashmap.add(2, song2)
    hashmap.add(3, song3)
    hashmap.add(4, song4)
    hashmap.add(5, song5)
    
    print(hashmap.__str__())

    
def test2():
    #check remove/contains
    hashmap = HashMap.HashMap()
    song1 = Song.Song("Track1", "TrackID1", "Image1", 1)
    song2 = Song.Song("Track2", "TrackID2", "Image2", 2)
    song3 = Song.Song("Track3", "TrackID3", "Image3", 0)
    song4 = Song.Song("Track4", "TrackID4", "Image4", 3)
    song5 = Song.Song("Track5", "TrackID5", "Image5", 10)
    
    hashmap.add(1, song1)
    hashmap.add(2, song2)
    hashmap.add(3, song3)
    hashmap.add(4, song4)
    hashmap.add(5, song5)
    
    hashmap.remove(2)
    print(hashmap.contains(2))

def test3():
    #checks isEmpty, size, get
    hashmap = HashMap.HashMap()
    song1 = Song.Song("Track1", "TrackID1", "Image1", 1)
    song2 = Song.Song("Track2", "TrackID2", "Image2", 2)
    song3 = Song.Song("Track3", "TrackID3", "Image3", 0)
    song4 = Song.Song("Track4", "TrackID4", "Image4", 3)
    song5 = Song.Song("Track5", "TrackID5", "Image5", 10)
    
    hashmap.add(1, song1)
    hashmap.add(2, song2)
    hashmap.add(3, song3)
    hashmap.add(4, song4)
    hashmap.add(5, song5)
    
    print(hashmap.size())
    print(hashmap.isEmpty())
    print(hashmap.get(5))
    
    
    


# In[28]:


test()


# In[29]:


test2()


# In[30]:


test3()


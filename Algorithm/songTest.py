#!/usr/bin/env python
# coding: utf-8

# In[5]:


"""
Tester method for Song Class
"""
import Song


# In[34]:


def test():
    #tests object initialization
    song1 = Song.Song("Track1", "TrackID1", "Image1", 2)
    song2 = Song.Song("Track2", "TrackID2", "Image2", 10)
    song3 = Song.Song("Track3", "TrackID3", "Image3", 8)
    song4 = Song.Song("Track4", "TrackID4", "Image4", 5)
    song5 = Song.Song("Track5", "TrackID5", "Image5", 1)
    
    #song should be setting key to zero so then we can increment based on user preference..
    print(str(song1) + " " + str(song1.getKey()))
    print(str(song2) + " " + str(song2.getKey()))
    print(str(song3) + " " + str(song3.getKey()))
    print(str(song4) + " " + str(song4.getKey()))
    print(str(song5) + " " + str(song5.getKey()))

def test2():
    song = Song.Song("The Trooper - Iron Maiden", "TrackID","Image",0)
    
    for i in range(3):
        song.incrementKey()
        print(str(song) + ", " +"key: " + str(song.getKey()))

def test3():
    song = Song.Song("The Trooper - Iron Maiden", "TrackID","Image",0)
    song2 = Song.Song("The Trooper --> Iron Maiden", "TrackID","Image",0)
    
    print(song.__eq__(song2))


# In[35]:


test()


# In[33]:


test2()


# In[36]:


test3()


# In[ ]:





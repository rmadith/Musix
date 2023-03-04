#!/usr/bin/env python
# coding: utf-8

# In[7]:


"""
Tester method for PriorityQueue Class
"""
import Song
import PriorityQueue


# In[53]:


def test1():
    #tests insertion
    queue = PriorityQueue.PriorityQueue()
    queue.insert(1)
    queue.insert(10)
    queue.insert(12)
    queue.insert(4)
    queue.insert(14)
    
    print(queue)

def test2():
    #test pop
    queue = PriorityQueue.PriorityQueue()
    song1 = Song.Song("Track1", "TrackID1", "Image1", 1)
    song2 = Song.Song("Track2", "TrackID2", "Image2", 2)
    song3 = Song.Song("Track3", "TrackID3", "Image3", 0)
    song4 = Song.Song("Track4", "TrackID4", "Image4", 3)
    song5 = Song.Song("Track5", "TrackID5", "Image5", 10)

    queue.insert(song1)
    queue.insert(song2)
    queue.insert(song3)
    queue.insert(song4)
    queue.insert(song5)
    
    print(queue.pop().trackID)
    print(queue.pop().trackID)
    print(queue.pop().trackID)
    print(queue.pop().trackID)
    print(queue.pop().trackID)

def test3():
    #test isEmpty
    
    queue = PriorityQueue.PriorityQueue()
    print(queue.isEmpty())
    

def test4():
    queue = PriorityQueue.PriorityQueue()
    queue.insert(1)
    queue.insert(10)
    queue.insert(12)
    queue.insert(4)
    queue.insert(14)
    
    print(type(queue.__str__()))
    


# In[54]:


test()


# In[55]:


test2()


# In[56]:


test3()


# In[57]:


test4()


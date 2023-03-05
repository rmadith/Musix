#!/usr/bin/env python3
"""
Tester method for HashedQueue Class
"""
import Song
import HashedQueue

def test():
    # Tester method for HashedQueue Class
    queue = HashedQueue.HashedQueue()
    song1 = Song.Song("Track1", "TrackID1", "Image1", 0)
    song2 = Song.Song("Track2", "TrackID2", "Image2", 0)
    song3 = Song.Song("Track3", "TrackID3", "Image3", 0)
    song4 = Song.Song("Track4", "TrackID4", "Image4", 0)
    song5 = Song.Song("Track5", "TrackID5", "Image5", 0)

    queue.add(song1)
    queue.add(song1)
    queue.add(song1)
    queue.add(song2)
    queue.add(song2)
    queue.add(song3)
    queue.add(song4)
    queue.add(song4)
    queue.add(song4)
    queue.add(song4)
    queue.add(song4)
    queue.add(song5)

    for i in range(5):
        print(queue.hashmap.get("TrackID" + str(i+1)).key)

    print(queue.pop().trackID)
    
    print(queue.pop().trackID)
    print(queue.pop().trackID)
    print(queue.pop().trackID)
    print(queue.pop().trackID)
    print(queue.pop().trackID)

    for i in range(10):
        print(queue.pop().trackID)

test()



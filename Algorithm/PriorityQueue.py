#!/usr/bin/env python
"""
Minimal PriorityQueue Class designed to hold all Song Objects
Parameters  -
    Value - Song Object
"""

import random

class PriorityQueue(object):
    def __init__(self):
        self.queue = []

    def __str__(self):
        return ' '.join([str(i) for i in self.queue])
    
    # Check if the PriorityQueue is empty
    def isEmpty(self):
        return len(self.queue) == 0
    
    # Add a Song Object to the PriorityQueue
    def insert(self, data):
        self.queue.append(data)

    # Sort the PriorityQueue using Insertion Sort
    def insertionSort(self):
        test = True
        if len(self.queue) == 0:
            return True
        
        # Check if all keys are zero
        for i in range(len(self.queue)):
            if self.queue[i].key != 0 or self.queue[i].played == False:
                test = False
                break
        
        if test:
            for i in range(len(self.queue)):
                self.queue[i].played = False
            random.shuffle(self.queue)
            return True

        for i in range(1, len(self.queue)):
            key = self.queue[i]
            j = i-1
            while j >=0 and key.key > self.queue[j].key :
                    self.queue[j+1] = self.queue[j]
                    j -= 1
            self.queue[j+1] = key
        return True



    def pop(self):
        try:
            min = self.queue[0]
            min.played = True
            del self.queue[0]
            self.insert(min)
            return min
        except IndexError:
            return None
        
    def __str__(self):
        return str(self.queue)

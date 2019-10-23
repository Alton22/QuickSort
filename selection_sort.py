#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 11:36:11 2019

@author: altonsmith-beyii
"""

def selectionsort(arr):
  for i in range(len(arr)):
     #first item sorted is assumed to be the smallest
    minindex=i
    for j in range(i+1,len(arr)):
        #this loop iterates through the list to
      if arr[j] < arr [minindex]:
    #this if statement determines wether another item in the list is smller than the first sorted item.
          
        minindex=j
    temp = arr[i]
    arr[i]=arr[minindex]
    arr[minindex]=temp
    
    #the lines of code above swaps the items when an item in the list is smaller than the first one.
    
a=[1,4,6,2,3,5]
selectionsort(a)
print(a)
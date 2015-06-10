#! /Users/macl2/anaconda/bin/python -tt
'''
Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down, 
there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20x20 grid?
'''

'''
This solution uses numpy's nd array method
'''
import numpy as np

def main():

  n = 2 # size of array

  array = np.zeros((n+1,n+1)) # this is initializing a nD numpy array. I initialise it to be greater
                              # than the size to facilitate the counting
  
  
  for i in range(n+1):        # loop through the different values and count them, storing the ways in 
  	for j in range(n+1):    # each array value.  This way I don't have to do a brute force calculation
  	  if i==0 and j==0:
  	  	array[i,j] = 1
  	  else:
  	  	array[i,j] = array[i,j-1] + array[i-1,j]
  
  print 'Answer =', int(array[n,n])
  
  return
  
  
if __name__ == '__main__':
  main()
  
'''
Another solution, using lists of lists is as follows:

def main():

  n = 20 # size of array

  array = [[0 for x in range(n+1)] for x in range(n+1)] # this is initializing a list of lists, equivalent to a 2D array
                                                        # it is one larger to facilitate the counting
  
  
  for i in range(n+1):        # loop through the different values and count them, storing the ways in 
  	for j in range(n+1):    # each array value.  This way I don't have to do a brute force calculation
  	  if i==0 and j==0:
  	  	array[i][j] = 1
  	  else:
  	  	array[i][j] = array[i][j-1] + array[i-1][j]
  
  print 'Answer =', array[n][n]
  
  return
  
  
if __name__ == '__main__':
  main()

'''

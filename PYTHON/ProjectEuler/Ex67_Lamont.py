#! /Users/macl2/anaconda/bin/python -tt
'''
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the 
maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. 
However, Problem 67, is the same challenge with a triangle containing one-hundred rows; it 
cannot be solved by brute force, and requires a clever method! ;o)
'''

import numpy

lenPyramid = 0

def read_file(filename):
    
  global lenPyramid  # identify lenPyramid as a global variable
    
  f = open(filename,'rU')  # read in the values into a string
  Pyramid = f.read() 
  f.close()
  
  f2 = open(filename,'rU')  # read in the values into a list
  PyramidCount = f2.readlines()      
  f2.close()
  
  for lines in PyramidCount: # count the size of the pyramid
      print lines
      lenPyramid += 1 
  
  Pyramid2 = Pyramid.split() # split the pyramid string into a list of the individual numbers

  return Pyramid2 # note that it is the list which is being returned
  
def fill_array(Pyramid):  # fill the numpy array with the values
  rows = lenPyramid
  columns = lenPyramid
  s = (rows,columns)
  RawArray = numpy.zeros(s)
  
  n = 0
  
  for i in range (0,rows):
  	for j in range(0,i+1): # loop over and fill in the pyramid style the valus from the list
  	  RawArray[i][j] = float(Pyramid[n])
  	  n += 1
  
  return RawArray
  
def sum_array(RawArray): # now loop over the array and calculate the sums. Note that each sum is of only 2 elememts
    
  rows = lenPyramid
  columns = lenPyramid
  s = (rows,columns)
  SumArray = numpy.zeros(s) # create an empty array
  
  print 'Raw array =\n', RawArray

  for i in range(0,rows):
  	for j in range(0,rows):
  	  if i == 0 or j == 0:   # for the first column or row, set temp to 0
  	  	Temp1 = 0
  	  else:
  	  	Temp1 = SumArray[i-1][j-1] # otherwise, take temp1 equals the value in the array for the row-1 and column-1
  	  
  	  if i == 0:
  	  	Temp2 = 0 # if we're in the first row, temp2 is set to 0
  	  else:
  	  	Temp2 = SumArray[i-1][j] # otherwise, we take the value in this column from the row before
  	  
  	  if Temp1 > Temp2:  # whichever value from the row above is higher, we add this to the value from the raw array
  	  	SumArray[i][j] = Temp1 + RawArray[i][j]
  	  else:
  	  	SumArray[i][j] = Temp2 + RawArray[i][j]
  	  	
  print 'SumArray =\n', SumArray

  
  
  
  return SumArray
  
  
def main():
  
  
  filename = './Ex18_Test.txt'
  #filename = './Ex18_Real.txt'
  #filename = './p067_triangle.txt'
  
  Pyramid = read_file(filename) # read in the file and get the list of numbers
  
  RawArray = fill_array(Pyramid) # fill an array with this list of numbers

  SumArray = sum_array(RawArray) # create an array with the numbers of the maximum sum
     
  print max(SumArray[SumArray.shape[1]-1]) # print the maximum value from the last row of the array
  
  return
  
if __name__ == '__main__':
  main()



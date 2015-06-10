#! /Users/macl/anaconda/bin/python -tt
'''
The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
 
(1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten natural 
numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred 
natural numbers and the square of the sum.
'''

import math

def SquareOfSums(num):  # function to find the square of the sums
  
  sumnum = 0
  
  for i in range(1,num+1):  # loop over the numbers and sum them
  	sumnum += i
  
  sqofsum = math.pow(sumnum,2) # take the square of them (either math.pow() or **2)
  
  print 'Square of the sums =', sqofsum
  
  return sqofsum # return the square of the sums
  
def SumOfSquares(num):  # function to find the sum of the squares
  
  sumofsqs = 0
  
  for i in range(1,num+1):       # loop over the numbers and square their sums
  	sumofsqs += math.pow(i,2)
  	
  print 'Sum of the squares =', sumofsqs
  
  return sumofsqs # return the sum of the squares

def main():
  
  num = 100
  
  sqofsum = SquareOfSums(num)     # call the square of the sums function
  sumofsqs = SumOfSquares(num)    # call the sum of the squares function
  
  difference = sqofsum - sumofsqs # calculate the difference
  
  print 'Difference between square of sums and sum of squares of the first', \
        num, 'natural numbers is:', int(difference)
  
  return
  
if __name__ == '__main__':
  main()
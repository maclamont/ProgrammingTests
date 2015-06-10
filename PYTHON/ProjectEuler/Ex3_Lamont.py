#! /Users/macl2/anaconda/bin/python -tt
'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

import math                        # needed in order to calculate the square root
import sys                         # needed when reading the input argument from the command line
from time import time

def isPrime(num):                  # function for calculating if a number is prime
  
  rangenum2 = int(math.sqrt(num))  # first, take the square root of the passed number
  
  for i in range(3,rangenum2+1,2): # loop over even numbers up until the square root
                                   # if a number is even, by definition it is not a prime factor
  	if num%i==0:                 
  	  return 0                   # if it is not prime, return 0
  
  return 1                         # if it is prime, return 1
  
  '''
  Note that for much larger numbers, sieve implementations could be used to calculte the
  prime numbers first and then these can be iterated over
  '''
  
def main():
  
  
  #num = 13195
  #num = int(sys.argv[1])          # use this option to take an input from the command line if required
  num = 600851475143
  
  largestPrimeFactor = False       # initialising the counter.  Needed in case there isn't one (for tests)
  
  print 'Calculating the largest prime factor of', num,':'
  
  
  rangenum = int(math.sqrt(num))      # calculate the square root of the number to be assessed
  
  t0 = time()                         # get ready to time the algorithm
  
  for i in range(3,rangenum+1,2):     # loop over even numbers, up until the square root
      if num%i==0:                    # check if the number is a factor of "num"
          if isPrime(i):              # check if this factor is a prime number
              largestPrimeFactor = i  # if so, this is now the largest prime factor
  
  if largestPrimeFactor:
      print "largestPrimeFactor =", largestPrimeFactor
  
  print "done in %0.3fs" % (time() - t0) # print the timing information
  
  
  return
  
  
  
if __name__ == '__main__':
  main()
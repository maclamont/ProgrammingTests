#! /Users/macl2/anaconda/bin/python -tt
'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can 
see that the 6th prime is 13.

What is the 10 001st prime number?
'''

import math

def isPrime(num):                  # fucntion to calculate if the number is prime or not
  
  rangenum = int(math.sqrt(num))
  
  for i in range(3,rangenum+1,2):  # only loop until the square root
  	
  	if int(num)%i==0:            # if the number has a factor, it is not prime
  	  return 0
      
  return 1

def main():
  
  i = 2                            # initialise the loop indexers
  j = 3
  
  Prime = 10001
  
  while (i<Prime+1):               # loop over the prime numbers until we get to the one we want
  
      if isPrime(j):                      # if a number is prime, increment the counter
  	    print 'Prime Number', i, ' =', j
  	    i += 1
       
      j += 2 
  	
  j -= 2                           # correct for the extra 2 added to j in the while loop
  	
  print 'The 10001st prime number is:', j
  
  return
  
  
if __name__ == '__main__':
  main()
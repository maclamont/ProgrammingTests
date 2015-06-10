#! /Users/macl2/anaconda/bin/python -tt
'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

import math

def IsPrime(num): # function to check if it is prime or not
  
  rangenum = int(math.sqrt(num))
  
  for i in range(3,rangenum+1,2): # just loop to the square root of the value.  Only look at odd numbers
  	if num%i==0:
  	  return 0
  	  
  return 1



def main():
  
  SumOfPrimes = 2 # in my loop I'm only looking at odd numbers, so start the counter with 2
  
  num = 2000000
  
  for i in range(3,num,2): # loop over the odd numbers
  	
  	if IsPrime(i):       # if it is prime, sum it up
  	  SumOfPrimes += i
  	  
  print 'Sum of Primes below 2000000 =', SumOfPrimes
  
  return
  
if __name__ == '__main__':
  main()
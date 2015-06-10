#! /Users/macl2/anaconda/bin/python -tt
'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''
import math

def main():
  
  for a in range(1,1000):       # loop from 1 to 1000
  	for b in range(a,1000):   # loop from a to 1000 (b > a)
  	  for c in range(b,1000): # loop from b to 1000 (c > b)
  	  	
  	  	if a+b+c == 1000:   # check if it's a triplet only if their sum is 1000
      
  	  	  if (math.pow(a,2) + math.pow(b,2)) == math.pow(c,2):
  	  	  	
  	  	  	print 'a =', str(a), ' b =', str(b), ' c =', str(c)
  	  	  	print "Product =", a*b*c
  	  	  	
  	  	  	return
  
  return
  
  
if __name__ == '__main__':
  main()
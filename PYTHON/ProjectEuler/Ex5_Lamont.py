#! /Users/macl2/anaconda/bin/python -tt
'''
2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the 
numbers from 1 to 20?
'''

def main():
  
    i=20
  
    while(1):
        if i%1e7==0:        # just printing out a counter as I'm looping
  	    print 'i =', i
        for num in range(1,21):  # loop over the numbers from 1 to 20
  	      if i%num!=0:         # if a number isn't a factor, break out of this for loop
  	          break
      
        if num == 20:            # if we got here, then all numbers from 1 to 20 were factors
        
          print 'Smallest number divisible by (1,20) =', i
          return
          
        i += 20                  # increment the values by the minimum needed, which is 20

    return
  
if __name__ == '__main__':
  main()
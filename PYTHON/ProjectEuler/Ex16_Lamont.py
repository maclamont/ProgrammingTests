#! /Users/macl2/anaconda/bin/python -tt
'''
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
'''

'''
This is very easy in python as it has the "long" form of the integer.  So I don't
have to worry about its length, even though it turns out to have a length of 302
'''

import math

def main():
  
  total = 0
  
  pow1000 = ""  # eventually I will have to sum the digits of 2^1000 so I will
                # need this value to be a string
  
  pow10 = long(math.pow(2,10))
  
  print '2^10 =', pow10 # just a test
  
  pow100 = long(math.pow(pow10,10))
  
  print '2^100 =', pow100 # another test
  
  pow1000 = str(long(math.pow(pow100,10)))
  
  print '2^1000 =', pow1000 # wow- this is a huge number!
  
  print 'len 2^1000[0]=', len(pow1000)
  
  for i in range(len(pow1000)):
    total += int(pow1000[i])
  	
  print 'Total sum =', total
  
  
  return
  
  
if __name__ == '__main__':
  main()
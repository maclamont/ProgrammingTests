#! /users/macl2/anaconda/bin/python -tt
'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, 
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''

def main():
  
  sum = 0 # initialise the conter to 0
  
  for i in range(1,1000):     # loop in the range from 1 to 999
  	if i%3 ==0 or i%5==0:   # if the number is exactly divisible by 3 or 5
  	  sum += i              # increment the sum counter with the number
  	  
  print 'Sum = ', sum         # print the answer
  
  return
  
if __name__ == '__main__':
  main()
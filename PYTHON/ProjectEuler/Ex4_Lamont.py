#! /users/macl2/anaconda/bin/pthon -tt
'''
A palindromic number reads the same both ways. The largest palindrome made 
from the product of two 2-digit numbers is 9009 = 91 * 99.
 
Find the largest palindrome made from the product of two 3-digit numbers.
'''

def isPalindrome(num):      # function defined to check for palindromes
  
  string = str(num)
  
  j = 0
  k = -1
  
  for i in range(len(string)/2):  # loop over the length of the number (divided by 2 so no repeats)
      if string[j] != string[k]:  # check the first and last values are the same, and so on
          return 0
      j +=1                       # increment the counters
      k -= 1
 
  return 1
  

def main():
  
  LargestPalindrome = 0
  
  for i in range(100,1000):
  	for j in range(100,1000):
  	  num = i*j
  	  
  	  if isPalindrome(num):               # call the palindrome function
  	  	if num > LargestPalindrome:     # if it's a palindrome, assign it to the largest value
  	  	  LargestPalindrome = num
  
  print 'Largest Palindrome =', LargestPalindrome
  
  return
  
  
if __name__ == '__main__':
  main()
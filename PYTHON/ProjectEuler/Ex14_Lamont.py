#! /Users/macl2/anaconda/bin/python -tt
'''
The following iterative sequence is defined for the set of positive integers:

n -> n/2 (n is even)
n -> 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. 
Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers 
finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''

def n_is_even(n): # function for the case where n is even
  
  n = n/2
  
  return n
	
def n_is_odd(n): # function for the case where n is odd
  
  n = 3*n + 1
  
  return n

def main():
  
  dictNum = {}  # create a dictionary
  
  for i in range(13,1000000,1):  # loop from 13 to a million
  	k = i
  	j = 1                  # the number in the chain
  	while(i>1):
  	  if i%2==0:
  	  	i = n_is_even(i) # call the n is even function
  	  elif i%2!=0 and i>1:
  	  	i = n_is_odd(i)  # call the n is odd function
  	  if i in dictNum:
  	  	dictNum[k] = dictNum[i]+j # if the new number has already been counted, 
                                      # use this value and create a new entry into
                                      # the dictionary
  	  	break
  	  j+=1
  	  if i==1:                      # at the end of the chain, fill the dictionary
  	  	dictNum[k] = j
  	  	
  '''
  Instead of looping through each of my dictionary items and making a comparison, 
  I can cheat and create a list of the sorted dictionary items.  This created ntuples
  of the key:value pairs and if I sort in reverse order, the first entry is the one 
  that I want.
  '''
  
  sortedList = sorted(dictNum.items(), key=lambda x: x[1], reverse=True)
  
  print 'Greatest Number =', str(sortedList[0][1]), 'from starting number:', str(sortedList[0][0])    
  
  return
  
if __name__ == '__main__':
  main()
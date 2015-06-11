#! /Users/macl2/anaconda/bin/python -tt
'''
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there 
are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many 
letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 
23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing 
out numbers is in compliance with British usage.
'''

def main():

  dict = {}
  Total = 0

  '''
  In this problem, there are lots of repeated words.  I just need to create a dict which stores
  the values for each of these words and use those to count the length of the words
  '''

  dict['and'] = len('and')
  dict[1000] = 11
  dict[0] = 0
  dict[1] = len('one')
  dict[2] = len('two')
  dict[3] = len('three')
  dict[4] = len('four')
  dict[5] = len('five')
  dict[6] = len('six')
  dict[7] = len('seven')
  dict[8] = len('eight')
  dict[9] = len('nine')
  dict[10] = len('ten')
  dict[11] = len('eleven')
  dict[12] = len('twelve')
  dict[13] = len('thirteen')
  dict[14] = len('fourteen')
  dict[15] = len('fifteen')
  dict[16] = len('sixteen')
  dict[17] = len('seventeen')
  dict[18] = len('eighteen')
  dict[19] = len('nineteen')
  dict[20] = len('twenty')
  dict[30] = len('thirty')
  dict[40] = len('forty')
  dict[50] = len('fifty')
  dict[60] = len('sixty')
  dict[70] = len('seventy')
  dict[80] = len('eighty')
  dict[90] = len('ninety')
  dict['hundred'] = len('hundred')
  dict['thousand'] = len('thousand')

  for i in range(1,1000,1):
    if i not in dict:
      if i < 100: # this is the straightforward case
        dict[i] = dict[10*(i/10)] + dict[i%10] # eg 42 = 10*(42/10) (=4) + 2
      elif i > 99 and i < 1000:
        if i%100==0:
            dict[i] = dict[i/100] + dict['hundred'] # values which are multiples of a hundred
        else:
            dict[i] = dict[i/100] + dict['hundred'] + dict[i%100]  + dict['and']

  for i in range(1001): # now just loop over the entries in the dictionary and sum them
    Total += dict[i]

  print 'Total =', Total

  return
  
if __name__ == '__main__':
  main()
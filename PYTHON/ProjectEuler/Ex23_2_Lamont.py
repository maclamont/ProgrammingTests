#! /Users/macl2/anaconda/bin/python -tt
'''
A perfect number is a number for which the sum of its proper divisors is 
exactly equal to the number. For example, the sum of the proper divisors of
 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than 
n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest 
number that can be written as the sum of two abundant numbers is 24. By
 mathematical analysis, it can be shown that all integers greater than 28123 
can be written as the sum of two abundant numbers. However, this upper limit 
cannot be reduced any further by analysis even though it is known that the 
greatest number that cannot be expressed as the sum of two abundant numbers 
is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum 
of two abundant numbers.
'''

def abundant_numbers():
    
    print 'Entering abundant_numbers()'
    
    ab_nums = [] # create a list of abundant numbers
    
    for i in range(1,28124):
    #for i in range(1,2100):
        if i%1000==0:
            print 'num:', i
        sum = 0
        for j in range(1,i):

            if i%j==0: # find the divisors
                sum += j # sum the divisors
        if sum > i: #an abundant number
            ab_nums.append(i) # add the abundant number to the list
            
    print 'Leaving abundant_numbers()'
            
    return ab_nums # returns a list of abundant numbers
    
def binary_search(alist, item):
    first = 0
    last = len(alist)-1
    found = False
    while first<=last and not found:
        midpoint = (first + last)//2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1
                
    return found
    
    
def sum_of_abundant_numbers(ab_numbers):
    
    print 'Entering sum_of_abundant_numbers()'

    sum2 = 0
    
    for i in range(1,28124):
    #for i in range(1,50):
        count = 0
        
        for j in ab_numbers:
            if j > i/2: # this stops repetition of the calculation
                break
            if binary_search(ab_numbers,(i-j)): # do a binary search on the ab_numbers list.  If it is in, both i and j are ab numbers
                count = 1
                break

        if count == 0:      # here I'm counting the sum of numbers that fail the ab_numbers test
            print 'i =', i
            sum2 += i
    
    print sum2

    print 'Leaving sum_of_abundant_numbers()'

    return
    
def main():
    
    ab_nums = abundant_numbers()
    #print ab_nums
    sum_of_abundant_numbers(ab_nums)
    
    return
    
if __name__ == '__main__':
    main()
#! /Users/macl2/anaconda/bin/python -tt
'''
n! means n * (n-1) * ... * 3 * 2 * 1

For example, 10! = 10 * 9 * ... * 3 * 2 * 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
'''
'''
Due to python's ability to handle very large numbers, this again is very straightforward
in python
'''

def n_factorial(n):  # calculate the value of n factorial.  Just loop over n
                     # and multiply the value each time
    nfactorial = 1
    
    for num in range(1,n+1):
        nfactorial *= num
    
    return nfactorial

def main():
    
    n = 100
    
    num = str(n_factorial(n))  # create a string out of this so we have access to its elements
    
    print str(n)+"! =", num
    
    sum = 0
    
    for i in range(len(num)):
        
        sum += int(num[i])
        
        
    print "sum of digits =", sum
    
    return
    
if __name__ == '__main__':
    main()





#! /Users/macl2/anaconda/bin/python -tt
'''
Let d(n) be defined as the sum of proper divisors of n (numbers less than n 
which divide evenly into n).

If d(a) = b and d(b) = a, where a not equal to b, then a and b are an amicable pair and 
each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 
55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 
71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.

Here, I can just create a list of amicable numbers (with list.append) and then 
loop over them and sum them
'''

def CalculateDivisors(n): # loop from 1 to n and calculate the divisors and put them in a list
    
    Divisors = []   
    Sum = 0
    
    
    for i in range(1,n):
        if n%i==0:
            Divisors.append(i)
    
    for i in Divisors:
        Sum += i
    
    
    return Sum


def main():
    
    AmicableDict = {}
    
    for i in range(1,10000):
        Sum = CalculateDivisors(i)
        AmicableDict[i] = Sum      # create a dictionary of the amicable numbers
    
    print AmicableDict
    
    AmicableSum = 0
    
    for i in range(1,10000):
        if AmicableDict[i] < 10000: # this is a check as the question asks for amicable numbers under 10000
            j = AmicableDict[i]
            if j > 0:
                k = AmicableDict[j]
                
                if k == i and j!=k: #This second check is required as some numbers point to themselves
                    AmicableSum += i
                    print 'i =', str(i), 'j =', str(j)
                    print 'j =', str(j), 'k =', str(k)
    
    print AmicableSum
    
    return
    
if __name__ == "__main__":
    main()
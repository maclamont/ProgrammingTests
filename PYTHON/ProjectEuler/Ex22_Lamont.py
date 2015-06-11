#! /Users/macl2/anaconda/bin/python
'''
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file 
containing over five-thousand first names, begin by sorting it into 
alphabetical order. Then working out the alphabetical value for each name, 
multiply this value by its alphabetical position in the list to obtain a name 
score.

For example, when the list is sorted into alphabetical order, COLIN, which 
is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN 
would obtain a score of 938 * 53 = 49714.

What is the total of all the name scores in the file?
'''
import pandas as pd

def open_file(file):
    
    name_list = []
    
    name_list = pd.read_csv(file) # here I read the data into a list
        
    sortedList = sorted(name_list) # here I sort the names and return the sorted list
    
    return sortedList



def main():
    
    filename = "./p022_names.txt"
    
    sorted_name_list = open_file(filename)       

    total_sum = 0
        
    for i in range(len(sorted_name_list)): # loop over the names
        for letter in sorted_name_list[i]: # loop over the letters in each name
            ind_sum = 0
            ind_sum += ord(letter)-64 # ord("A") = 65 so using this to get the values listed in the question
            ind_sum = ind_sum*(i+1) # multiple by the names ranking in the list
            total_sum += ind_sum
                
    print total_sum

    return
    
if __name__ == '__main__':
    main()
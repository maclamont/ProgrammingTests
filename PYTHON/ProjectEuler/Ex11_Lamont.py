#! /Users/macl2/anaconda/bin/python -tt
'''
In the 20*20 grid below, four numbers along a diagonal line have been marked 
in red.

08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48

The product of these numbers is 26 * 63 * 78 * 14 = 1788696.

What is the greatest product of four adjacent numbers in the same direction 
(up, down, left, right, or diagonally) in the 20*20 grid?
'''

def readFile(filename):    # I have put these numbers into a file.  This function reads them in
  
  f = open(filename,'rU')  # read in the values into a list
  BigList = f.read()
  f.close()
  
  print '\nGridfile is:\n'
  print BigList
  
  return BigList
  
def FillDict(BigList): # a function to fill a dictionary.  This could also be done with numpy
  
  
  GridDict = {} #declare my dictionary
  
  #declare my integers
  i1, i2, i3, i4, i5, i6, i7, i8, i9, i10 = (0 for i in range(10))
  i11, i12, i13, i14, i15, i16, i17, i18, i19, i20 = (0 for i in range(10))
  j = 1  
  
  # fill my dictionary 
  for i in range(0,58,3):
  	GridDict[j] = (10*int(BigList[i+0])+int(BigList[i+1]))
  	GridDict[j+20] = (10*int(BigList[i+60])+int(BigList[i+61]))
  	GridDict[j+40] = (10*int(BigList[i+120])+int(BigList[i+121]))
  	GridDict[j+60] = (10*int(BigList[i+180])+int(BigList[i+181]))
  	GridDict[j+80] = (10*int(BigList[i+240])+int(BigList[i+241]))
  	GridDict[j+100] = (10*int(BigList[i+300])+int(BigList[i+301]))
  	GridDict[j+120] = (10*int(BigList[i+360])+int(BigList[i+361]))
  	GridDict[j+140] = (10*int(BigList[i+420])+int(BigList[i+421]))
  	GridDict[j+160] = (10*int(BigList[i+480])+int(BigList[i+481]))
  	GridDict[j+180] = (10*int(BigList[i+540])+int(BigList[i+541]))
  	GridDict[j+200] = (10*int(BigList[i+600])+int(BigList[i+601]))
  	GridDict[j+220] = (10*int(BigList[i+660])+int(BigList[i+661]))
  	GridDict[j+240] = (10*int(BigList[i+720])+int(BigList[i+721]))
  	GridDict[j+260] = (10*int(BigList[i+780])+int(BigList[i+781]))
  	GridDict[j+280] = (10*int(BigList[i+840])+int(BigList[i+841]))
  	GridDict[j+300] = (10*int(BigList[i+900])+int(BigList[i+901]))
  	GridDict[j+320] = (10*int(BigList[i+960])+int(BigList[i+961]))
  	GridDict[j+340] = (10*int(BigList[i+1020])+int(BigList[i+1021]))
  	GridDict[j+360] = (10*int(BigList[i+1080])+int(BigList[i+1081]))
  	GridDict[j+380] = (10*int(BigList[i+1140])+int(BigList[i+1141]))
  	j+=1
  
  return GridDict

def GreatestProduct(GridDict):
  
  GreatestProduct = 0
  
  
  # loop over the horizontal numbers
  print '***********************************'
  print 'Looping over the horizontal numbers'
  print '***********************************'
  for i in range(0,400,20):
  	for j in range(i+1,i+18,1):
  	  #print 'j = ', j
  	  Product = GridDict[j]*GridDict[j+1]*GridDict[j+2]*GridDict[j+3]
  	  if Product>GreatestProduct:
  	    GreatestProduct = Product
  print '\nAfter horizontal, greatest product =', GreatestProduct
  
  
  # loop over the vertical numbers
  print '\n*********************************'
  print 'Looping over the vertical numbers'
  print '*********************************'
  for i in range(0,340,20):
  	for j in range(i+1,i+21,1):
  	  Product = GridDict[j]*GridDict[j+20]*GridDict[j+40]*GridDict[j+60]
  	  if Product>GreatestProduct:
  	    GreatestProduct = Product
  print '\nAfter vertical, greatest product =', GreatestProduct
  
  
  # loop over the \ numbers
  print '\n**************************'
  print 'Looping over the \ numbers'
  print '**************************'
  for i in range(0,340,20):
  	for j in range(i+1,i+18,1):
  	  Product = GridDict[j]*GridDict[j+21]*GridDict[j+42]*GridDict[j+63]
  	  if Product>GreatestProduct:
  	    GreatestProduct = Product
  print '\nAfter \, greatest product =', GreatestProduct
  
  
  # loop over the / numbers
  print '\n**************************'
  print 'Looping over the / numbers'
  print '**************************'
  for i in range(0,340,20):
  	for j in range(i+4,i+21,1):
  	  Product = GridDict[j]*GridDict[j+19]*GridDict[j+38]*GridDict[j+57]
  	  if Product>GreatestProduct:
  	    GreatestProduct = Product
  print '\nAfter /, greatest product =', GreatestProduct
  
  
  return GreatestProduct


def main():
  
  filename = './Grid.txt'
  
  BigList = readFile(filename)
  
  GridDict = FillDict(BigList)

  Answer = GreatestProduct(GridDict)
  
  print '\nGreatest product =', Answer
  
  return
  
  
if __name__ == '__main__':
  main()
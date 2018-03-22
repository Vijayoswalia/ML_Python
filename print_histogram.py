# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 10:04:36 2018

@author: Vijay
"""

L = [1,2,3,4,5]
for i in L:
    print('*' * i )

str_numbers = str(input("Enter the number seperated by ,:: "))
numbers = [int(x) for x in str_numbers.split(",")]

i=max(numbers)
while i>=1:
    j=0
    while j<len(numbers):
        if numbers[j]-i>=0:
            print(' * ', end='')
        else:
            print('   ', end='')
        j+=1
    i-=1
    print("\n")
    
    
L = [1,2,3]
j=1
for i in L:
    print ('*' * i)
    
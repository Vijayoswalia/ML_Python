# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 10:43:39 2018

@author: Vijay
"""

str_numbers = str(input("Enter the number seperated by ,:: "))
numbers = [int(x) for x in str_numbers.split(",")]

while i<pose:
    right_pos.append(list_numbers[i])
    i+=1

i=0

while i<pos:
    list_numbers.pop(0)
    i+=1
    
i=0
print(right_pos)

while i
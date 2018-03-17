# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 10:33:28 2018

@author: Vijay
"""

cars = ['bmw','audi','honda']
magicians = ['alice','david','carolina']
for magician in magicians:
    print(magician)
    
squares = [value**2 for value in range(1,11)]
print(squares)

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
        
squares = []
for value in range(1,11):
     squares = value**2
     print(squares)
     
import numpy as np

numbers = []
for number in range(1,200):
    numbers.append(number)
print(numbers)

max(numbers)
min(numbers)
max(numbers)
numbers[-2]
numbers[1]
np.mean(numbers)
np.median(numbers)
np.percentile(numbers,0)

number2 = [number for number in range(1,100)]
number2

middle= int(len(numbers)/2)
middle
if middle/2==0:
    print(numbers[middle])
else:
    print(numbers[middle-1])
    
for number in range(numbers):
    if number<max(numbers) and number>max(number):
        print(number)
    secondhigh =  
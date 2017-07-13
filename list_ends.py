__author__ = 'leohck'

#exercise 12
"""
Write a program that takes a list of numbers for example, 
a = [5, 10, 15, 20, 25]
and makes a new list of only the first and last elements of the given list.
For practice, write this code inside a function.
"""
from random import randint


def Create_list(old_list):
	new_list= [old_list[0],old_list[-1]]
	return new_list
	
a = [randint(0,100) for x in range(0,10)]

new_list = Create_list(a)
print('old_list: \n',a)
print('New list: \n',new_list)
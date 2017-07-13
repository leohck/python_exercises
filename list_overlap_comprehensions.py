__author__ = 'leohck'

#exercise 10
"""
Take two lists, say for example these two:

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only 
the elements that are common between the lists (without duplicates). 
Make sure your program works on two lists of different sizes.
 Write using at least one list comprehension. 
"""
#extra
"""
Randomly generate two lists to test this
"""
from random import randint

a = [randint(0,100) for x in range(0,10)]
b = [randint(0,100) for x in range(0,10)]

new_list = []
new_list = [x for x in a if x in b if x not in new_list]

print('list a: \n',a,'\n list b: \n ',b,' \n new list: \n',new_list)
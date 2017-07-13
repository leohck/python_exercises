__author__ = 'leohck'
from random import randint
#exercise 5
"""
Take two lists, say for example these two:
  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that
contains only the elements that are common between the lists (without duplicates). 
Make sure your program works on two lists of different sizes.

Extras:

Randomly generate two lists to test this

""" 
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
common_nums=[]
for i in b:
	if i in a:
		if i not in common_nums:
		    common_nums.append(i)	

print('list a:',a,'\n list b: ',b)
print('commons nums between list a and b...')

for i in common_nums:
	print(i)

#extra

rand_a = [randint(0,9) for i in range(0,9)]
rand_b = [randint(0,9) for i in range(0,9)]
common_rand_nums = []

for i in rand_b:
	if i in rand_a:
		if i not in common_rand_nums:
		    common_rand_nums.append(i)	

print('list a:',rand_a,'\n list b: ',rand_b)
print('commons nums between list a and b...')
for i in common_rand_nums:
	print(i)



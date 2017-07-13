__author__ = 'leohck'

#exercise 3
"""
Take a list, say for example this one:
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
and write a program that prints out all the elements of the list that are less than 5.
"""
# answer 1
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
a_less_5 = []

for i in a:
	if i < 5:
		a_less_5.append(i)
	else:
		continue
print('list',a)
print('numbers less to 5 in list',a_less_5)

#answer 2
import numpy as np 

np_a = np.array(a)

np_a_less_5 = np_a[:] < 5

print('list',np_a)
print('numbers less to 5 in list',np_a[np_a_less_5])

num = int(input('Type a number to verify if any number of the list is smaller than yours\n>>>: '))
num_list=[]
for i in a:
	if i < num:
		num_list.append(i)


print('New list: \n',num_list)
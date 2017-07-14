__author__ = 'leohck'
#exercise 14
"""
Write a program (function!) that takes a list and returns a new list 
that contains all the elements of the first list minus all the duplicates.

Extras:

Write two different functions to do this - one using a loop and constructing a list, 
and another using sets.

Go back and do Exercise 5 using sets, 
and write the solution for that in a different function.
"""
def Remove_Duplicate(a):
	for i in a:
		if a.count(i) > 1:
			a.remove(i)
	return a

def Generate_Duplicate_list():
	a = [x for x in range(1,11)]
	b = list(a)
	a.extend(b)
	a.sort()
	return a

def Generate_W_Set():
	a = set()
	for i in range(1,11):
		a.add(i)
	return list(a)


a = Generate_W_Set()
a = Remove_Duplicate(a)
print(a)
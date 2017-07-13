__author__ = 'leohck'

#exercise 13

"""
Write a program that asks the user how much Fibonnaci numbers to generate and 
then generates them. Take this opportunity to think about how you can use functions. 
Make sure to ask the user to enter the number of numbers in the sequence to generate.
"""
def Fibonnaci(how_much):
	for i in range(0,how_much):
		print((i-1)+(i-1))



how_much = int(input('how much Fibonnaci numbers to generate? \n ><>>: '))
Fibonnaci(how_much)

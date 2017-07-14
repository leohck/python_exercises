__author__ = 'leohck'

#exercise 13

"""
Write a program that asks the user how much Fibonnaci numbers to generate and 
then generates them. Take this opportunity to think about how you can use functions. 
Make sure to ask the user to enter the number of numbers in the sequence to generate.
"""
def Fibonnaci(how_much):
	foo = 1
	if how_much == 1:
		numbers = [1]
	elif how_much == 2:
		numbers = [1,1]
	elif how_much > 2:
		numbers = [1,1]
		while foo < (how_much - 1):
			numbers.append(numbers[foo] + numbers[foo - 1])
			foo += 1
	return numbers



how_much = int(input('how much Fibonnaci numbers to generate? \n ><>>: '))
print(Fibonnaci(how_much))

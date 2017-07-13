__author__ = 'leohck'
#exercise 11
"""
Ask the user for a number and determine whether the number is prime or not.
"""

def Is_primary(number):
	classifier = 0
	for i in range(2,number):
		if number % i == 0:
		   classifier += 1
	if classifier > 0:
		return 'The number: %i not is primary'%number
	else:
		return 'The number: %i is primary'%number
 
number = int(input('Type any number and I will tell to you if is primary or not\n><>>: '))
print(Is_primary(number))
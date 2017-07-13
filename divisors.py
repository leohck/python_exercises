__author__ = 'leohck'

#exercise 4
"""
Create a program that asks the user for a number and 
then prints out a list of all the divisors of that number.
"""
number= int(input('Type a number:\n>>>: '))
divisors_list = []
for i in range(1,number+1):
	if number % i == 0:
		print(divisors_list.append(i))

print('all the divisors of that number...')
for i in divisors_list:
	print(i)
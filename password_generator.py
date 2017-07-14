__author__ = 'leohck'

#exercise 16

"""
Write a password generator in Python. 
Be creative with how you generate passwords - 
strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. 
the passwords should be random, 
generating a new password every time the user asks for a new password. 
Include your run-time code in a main method.

Extra:

Ask the user how strong they want their password to be. For weak passwords, 
pick a word or two from a list.
"""
from random import choice,sample

low = 'abcdefghijklmnopqrstuvwxiz'
upper = 'ABCDEFGHIJKLMNOPRSTUVWXYZ'
caracter = '!@#$%ˆ&*()_'
num = '0123456789'

weak_pass = ['upLOw3r245','low70UP102$','weakPASSw0rd','veryweak123','12345678']

def Gen_Pass():
	for word in range(0,3):
		password = sample(low,2)
		password += sample(caracter,2)
		password += sample(num,2)
		password += sample(upper,2)
		if word == 2:
			password += sample(caracter,2)
			password += sample(num,2)
			password += sample(upper,2)
			password += sample(low,2)
	password = ''.join(password)
	return password	

	
pass_type = str(input('Do You Want to generate a password weak or strong? \n ><>>: '))

while True:
	if pass_type == 'weak':
		password = choice(weak_pass)
		break
	elif pass_type == 'strong':
		password = Gen_Pass()
		break
	else:
		pass_type = str(input('please choose the type of password \n ><>>>: '))


print('Your password is: \n %s'%password)

while True:
	controller = str(input('Do You want to generate another password?\n if yes choose again the type: weak / strong \n if no type: n to exit\n ><>>: '))
	if controller == 'weak':
		password = choice(weak_pass)
		print('Your password is: \n %s'%password)
	elif controller == 'strong':
		password = Gen_Pass()
		print('Your password is: \n %s'%password)
	elif controller == 'n':
		break
	else:
		controller = str(input('please choose the type of password \n ><>>>: '))




	
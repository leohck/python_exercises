__author__ = 'leohck'
#exercise 9
"""
Generate a random number between 1 and 9 (including 1 and 9). 
Ask the user to guess the number, 
then tell them whether they guessed too low, too high, or exactly right.
"""
from random import randint
def Game(number,number_to_guess):
	attempts = 1
	while True:
		if number == number_to_guess:
			message = ('---YOU WON---')
			print('attempts: ',attempts)
			print(message)
		elif number < number_to_guess:
			number_check = number_to_guess - number
			if number_check >= 2:
				message = ('---too LOW---')
				print(message)
				number = int(input('Guess again...\n><>>: '))
				attempts += 1
			else:
				message = ('---LOW---')
				print(message)
				number = int(input('Guess again...\n><>>: '))
				attempts += 1
		elif number > number_to_guess:
			number_check = number_to_guess - number
			if number_check <= 2:
				message = ('---HIGH---')
				print(message)
				number = int(input('Guess again...\n><>>: '))
				attempts += 1
			else:
				message = ('--- too HIGH ---')
				print(message)
				number = int(input('Guess again...\n><>>: '))
				attempts += 1
		if message == ('---YOU WON---'):
			attempts = 1
			controller = str(input('Do you want to play again? Y/exit\n><>>>: '))
			if controller == 'exit':
				break
			else:
				number_to_guess = randint(0,10)
				number = int(input('Guess again...\n><>>: '))
	return message
print('---GUESS GAME---')
number_to_guess = randint(0,10)
user_number = int(input('Guess the random number...\n TIP: 0 ... 10\n><>>: '))
Game(user_number,number_to_guess)


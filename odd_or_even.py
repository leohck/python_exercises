__author__ = 'leohck'

#exercise 2
#Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.

print('Please type any number')
number = int(input('>>>: '))
odd_message = 'The number: %i is odd' %number
even_message = 'The number: %i is even' %number
if number % 2 == 0:
	print(even_message)
else:
	print(odd_message)

#extras:
"""
1.If the number is a multiple of 4, print out a different message.
2.Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
"""
#extra 1
multiple_4_message = 'The number: %(number) is multiple of 4 :)'
if number / 4 == 0:
	print(multiple_4_message)
else:
	print('The number: %i is not multiple of 4 :( ')

print('Now give me 2 numbers, first any number if you want, then one number to divide by the other number')
num = int(input('First number\n>>>: '))
check = int(input('Second number\n>>>: '))
result = check%num
if result == 0:
	print('The number: %i divides evenly into %i :)'%(check,num))
else:
	print('The number: %i  not divides evenly into %i  :('%(check,num))
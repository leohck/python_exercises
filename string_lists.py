__author__ = 'leohck'

#exercise 6
"""
Ask the user for a string and print out whether this string is a palindrome or not. 
(A palindrome is a string that reads the same forwards and backwards.)
"""
word = str(input('type a word\n>>>: '))

reverse_word = sentence[::-1]

if word == reverse_word:
	print('This word is a palindrome :)')
else:
	print('This word not is a palindrome :X')
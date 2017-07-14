__author__ = 'leohck'

#exercise 15

"""
Write a program (using functions!) 
that asks the user for a long string containing multiple words.
Print back to the user the same string, except with the words in backwards order.
"""



def Print_Back(word):
	return ' '.join(word.split(' ')[::-1])

word = str(input('Please type a sentence!\n ><>>: '))
reverse_word = Print_Back(word)
print('New sentence: %s'%reverse_word)
#######################----OR-----######################

word = str(input('Please type a sentence!\n ><>>: '))
split_word = word.split(' ')
reverse_split_word = split_word[::-1]
reverse_word = ' '.join(reverse_split_word)
print('Your sentence: %s'%word)
print('New sentence: %s'%reverse_word)
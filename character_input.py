__author__ = 'leohck'

#exercise 1
#Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.
act_year = 2017
print('What is your name?')
name = str(input('>>>: '))
print('Now please type your age...')
age = int(input('>>>: '))
turn_age = (100 - age) + act_year
message = '%s we are in %i and you will have 100 years old in %i'%(name,act_year,turn_age)        
print(message)

#extras:
"""
1.Add on to the previous program by asking the user for another number and printing out that many copies of the previous message.
2.Print out that many copies of the previous message on separate lines.
"""

# extra 1
print('How many times do you want to print te message ?')
times = int(input('>>>: '))
print(message*times)

#extra 2
for i in range(1,times+1):
	print(message)
         
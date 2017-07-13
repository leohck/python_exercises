__author__ = 'leohck'

#exercise 8
"""
Make a two-player Rock-Paper-Scissors game.
"""

def Game(player1,player2):
    if player1 == player2:
    	result = ('---DRAW---')
    elif player1 == 1 and player2 == 2:
    	result = ('---WINNER---\nPLAYER 2')
    elif player1 == 1 and player2 == 3:
    	result = ('---WINNER---\nPLAYER 1')
    elif player1 == 2 and player2 == 1:
    	result = ('---WINNER---\nPLAYER 1')
    elif player1 == 2 and player2 == 3:
    	result = ('---WINNER---\nPLAYER 2')
    elif player1 == 3 and player2 == 1:
    	result = ('---WINNER---\nPLAYER 2')
    elif player1 == 3 and player2 == 2:
    	result = ('---WINNER---\nPLAYER 1')
    return result

controller = 'y'
while controller != 'n':
	print('ROCK - PAPER - SCISSORS\n Type: 1 - ROCK / 2 - PAPER / 3 - SCISSORS')
	player1 = int(input('Player 1 turn...\n>>>: '))
	player2 = int(input('Player 2 turn...\n>>>: '))
	result = Game(player1,player2)
	print(result)
	controller = str(input('Do you want to play again? y/n\n>>>: '))
	if controller == 'n':
		print('END GAME')
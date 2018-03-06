# Game - Black Jack
# 
# Author(s) 
# 	- Eliakin del Rosario
# 
# Date
# 	- Started (3/6/2018)
#   - Last Modified (-/-/----)


import random 
from deck import Deck

def test_deck():
	deck = Deck()
	deck.build()
	deck.show()
	print('Shuffled...')
	deck.shuffle()
	deck.show()

test_deck()




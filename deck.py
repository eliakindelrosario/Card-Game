# Deck of Cards Class
# 
# Author(s) 
# 	- Eliakin del Rosario
# 
# Date
# 	- Started (2/22/2018)
#   - Last Modified (-/-/-)


import random

class Card(object):
	# Create a card object with a suit and a value
	def __init__(self, suit, value):
		self.suit = suit 
		self.value = value

	def show(self):
		# Display the value and suit of card
		print('{} of {}'.format(self.value, self.suit))
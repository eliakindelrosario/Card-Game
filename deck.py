# Deck of Cards Class
# 
# Author(s) 
# 	- Eliakin del Rosario
# 
# Date
# 	- Started (2/22/2018)
#   - Last Modified (3/6/2018)


import random

class Card(object):
	# Card object 
	# 	- Specifies a card's suit and value
	def __init__(self, suit, value):
		self.suit = suit 
		self.value = value

	def show(self):
		# Display the value and suit of the card
		print('{} of {}'.format(self.value, self.suit))

class Deck(object):
	# Deck object 
	# 	- Builds deck with 52 cards 
	# 	- Deck conatians 4 suits with 13 cards in each

	_CARD_SUITS = ['Spades', 'Clubs', 'Diamonds', 'Hearts']
	
	def __init__(self):
		self.cards = [] # Card container  
		self.build() 	# Generate deck upon initializing deck object

	def build(self):
		# create 13 cards for every suit available
		for s in self._CARD_SUITS:
			for v in range(1, 14):
				self.cards.append(Card(s,v)) # Use card object to create card 
				# print('{} of {}'.format(v, s))

	def show(self):
		# Display the suit and value of current card
		for c in self.cards:
			c.show()

	def shuffle(self):
		# Randomize the cards in the deck
		# Algorithm - Fisher–Yates shuffle 
		for i in range(len(self.cards)-1, 0, -1):
			r = random.randint(0, i) # pick random number that is to the left of the deck
			self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

	def draw(self):
		# Retun the top card from the deck
		return self.cards.pop()

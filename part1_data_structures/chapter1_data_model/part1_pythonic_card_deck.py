# Example 1-1. A deck as a sequence of playing cards
import collections
from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()
    
    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]
    
    # Implementing special methods allow you use them on an instance of your class
    def __len__(self):
        return len(self._cards)
    
    def __getitem__(self, position):
        return self._cards[position]

# Instantiate a card with Card class created with namedtuple method
beer_card = Card('7', 'diamonds')
beer_card

# Instantiate a deck of French cards
deck = FrenchDeck()

# Check amount cards in the deck beacuse __len__ method is implemented
len(deck)

# Reading specific cards from the deck
deck[0]
deck[-1]

# picking up a random card with alraedy built-in method "choice"
choice(deck)

# __get__item method let you slicing your deck as well because 
# it delegates to the [] operator
deck[:3] # take first 3 elements
deck[12::13] # start from 12th element and skipping 12 cards at a time

# with __get__ item method you can iterate over your deck
for card in deck:
    print(card)

#iterate in reverse
for card in reversed(deck):
    print(card)
# If a collection has no __contains__ method you can check presents 
# of cards in the deck with "in" operator
# it is working because our deck is iterable
Card('Q', 'hearts') in deck
Card('Q', 'beasts') in deck

# function to sort cards by suit in order spades(highest), hearts, diamonds, clubs
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

# Now we can list our deck in order of increasing rank:
for card in sorted(deck, key=spades_high):
    print(card)

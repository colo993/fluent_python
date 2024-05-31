# A Pythonic Card Deck

# Example 1-1. A deck as a sequence of playing cards
import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()
    
    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]
        
    def __len__(self):
        return len(self._cards)
    
    def __getitem__(self, position):
        return self._cards[position]

# Instantiate a card with Card class created with namedtuple method
beer_card = Card('7', 'diamonds')
beer_card

# Instantiate a deck of French cards
deck = FrenchDeck()

# Check amount cards in the deck
len(deck)

# Reading specific cards from the deck
deck[0]
deck[-1]


from random import shuffle
from card import Card

class Deck:

    def __init__(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.cards = [Card(suit, value) for suit in suits for value in values]

    def __repr__(self):
        return f"Deck of {self.count()} cards"

    def count(self):
        return len(self.cards)

    def _deal(self, number):
        if self.count() == 0:
            raise ValueError("All cards have been dealt")
        elif self.count() <= number:
            popped_items = []
            for num in range(0, len(self.cards)):
                popped_items.append(self.cards.pop())
            return popped_items
        else:
            popped_items = []
            for num in range(0, number):
                popped_items.append(self.cards.pop())
            return popped_items

    def shuffle(self):
        if self.count() < 52:
            raise ValueError("Only full decks can be shuffled")
        else:
            shuffle(self.cards)
            return self

    def deal_card(self):
        return self._deal(1)[0]

    def deal_hand(self, number):
        return self._deal(number)



my_deck = Deck()
print(my_deck)
my_deck.shuffle()
card = my_deck.deal_card()
print(card)
hand = my_deck.deal_hand(5)
print(hand)
print(my_deck)
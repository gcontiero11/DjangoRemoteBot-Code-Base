# from django.db import models
from enum import Enum

# Create your models here.
class CardSuit(Enum):
    HIDDEN = ("X", 0)
    DIAMONDS = ("D", 1)
    SPADES = ("S", 2)
    HEARTS = ("H", 3)
    CLUBS = ("C", 4)

    def __init__(self, symbol, ordinal_value):
        self.symbol = symbol
        self.ordinal_value = ordinal_value

    @property
    def value(self):
        return self.ordinal_value

    @staticmethod
    def of_symbol(symbol):
        for suit in CardSuit:
            if suit.symbol == symbol:
                return suit
        raise ValueError(f"Unknown suit symbol: {symbol}")

    def __str__(self):
        return self.symbol

class CardRank(Enum):
    HIDDEN = (0, 'X')
    FOUR = (1, '4')
    FIVE = (2, '5')
    SIX = (3, '6')
    SEVEN = (4, '7')
    QUEEN = (5, 'Q')
    JACK = (6, 'J')
    KING = (7, 'K')
    ACE = (8, 'A')
    TWO = (9, '2')
    THREE = (10, '3')

    def __init__(self, value, symbol):
        self._value = value
        self.symbol = symbol

    @property
    def value(self):
        return self._value

    def next(self):
        if self == CardRank.THREE:  
            return CardRank.FOUR
        elif self == CardRank.HIDDEN: 
            return CardRank.HIDDEN
        else:
            next_value = self._value + 1
            return CardRank(next_value)

    @staticmethod
    def of_symbol(symbol):
        for rank in CardRank:
            if rank.symbol == symbol:
                return rank
        raise ValueError(f"Unknown rank symbol: {symbol}")

    def __str__(self):
        return self.symbol


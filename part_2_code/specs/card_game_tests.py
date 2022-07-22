import unittest
from src.card import Card
from src.card_game import CardGame


class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.card_ace = Card("hearts", 1)
        self.card_not_ace = Card("hearts", 3)
        self.card_low_2 = Card("spades", 2)
        self.card_high_9 = Card("clubs", 9)
        self.cards = [
            self.card_ace,
            self.card_not_ace,
            self.card_low_2,
            self.card_high_9,
        ]

    # test ace
    def test_ace_True(self):
        self.assertEqual(True, CardGame.check_for_ace(self, self.card_ace))

    def test_ace_False(self):
        self.assertEqual(False, CardGame.check_for_ace(self, self.card_not_ace))

    # test highest
    def test_highest_card1_high(self):
        result = CardGame.highest_card(self, self.card_high_9, self.card_low_2).value
        self.assertEqual(9, result)

    def test_highest_card1_low(self):
        result = CardGame.highest_card(self, self.card_low_2, self.card_high_9).value
        self.assertEqual(9, result)

    # test total cards
    def test_cards_total(self):
        self.assertEqual(
            "You have a total of15", CardGame.cards_total(self, self.cards)
        )

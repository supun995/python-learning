import sys
import unittest
from unittest.mock import patch
from pathlib import Path

# sys.path.append(str(Path(__file__).parent.parent / 'playground'))


class TestCards(unittest.TestCase):

    def test_card(self):
        from playground.cards import Card

        self.assertEqual(str(Card('♠', '2', faceup=False)), '??')
        self.assertEqual(str(Card('♠', '2', faceup=True)), '2♠')

    @patch('playground.cards.random.shuffle')
    def test_deck(self, shuffle_mock):
        from playground.cards import Deck

        # By default the deck contains 52 cards.
        self.assertEqual(len(Deck()), 52)

        # The K♣ is at the end of the list and the
        # deal method takes from the end of the deck.
        self.assertEqual(str(Deck().deal()), 'K♣')

        # Ensure the shuffle method is calling the random.shuffle.
        Deck().shuffle()
        shuffle_mock.assert_called()


# If this code is being run as a script, test the game.
if __name__ == '__main__':
    print(unittest.main(verbosity=1, failfast=True))

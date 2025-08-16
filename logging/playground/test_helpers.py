import sys
import unittest
from unittest.mock import Mock, patch

from pathlib import Path

# sys.path.append(str(Path(__file__).parent.parent / 'playground'))

from blackjack import format_winner, prompt_for_bet, score
from cards import Card

###############################################################################
# Helper code to make it easier to create cards used for testing.
def card(rank, suit='♠'):
    ''' Helper function used to create cards for testing.
        we don't care about suits for our testing so setting a default of spade
    '''
    return Card(suit, rank)

def score_for_cards(cards):
    ''' Takes a string representing cards and calculates and returns the score. '''
    return score([card(c) for c in cards.split()])
###############################################################################

@patch('blackjack.clear_screen', lambda: None)
# Patch the default print callable for the entire class with an unused mock.
@patch('builtins.print', Mock())
class TestBlackjack(unittest.TestCase):

    # patch the builtin input function so that it always returns 100.
    @patch('builtins.input', Mock(return_value=100))
    def test_prompt_for_bet(self):
        ''' Prompt for bet. '''
        self.assertEqual(prompt_for_bet(1_000), 100)

    def test_score(self):
        ''' Score calculation. '''
        # check a couple of numeric cards
        self.assertEqual(score_for_cards('2 3'), 5)
        # check a couple of face cards
        self.assertEqual(score_for_cards('K Q'), 20)
        # check some cards with an ace
        self.assertEqual(score_for_cards('K A'), 21)
        self.assertEqual(score_for_cards('9 A'), 20)
        self.assertEqual(score_for_cards('3 A'), 14)
        # check a couple of cards with an ace to ensure the ace becomes a 1
        self.assertEqual(score_for_cards('K Q A'), 21)
        self.assertEqual(score_for_cards('K 9 3 A'), 23)


    def test_format_winner(self):
        self.assertTrue('Player wins!' in format_winner('player'))
        self.assertTrue('Dealer wins!' in format_winner('dealer'))


# If this code is being run as a script, test the game.
if __name__ == '__main__':
    print(unittest.main(verbosity=1, failfast=True))

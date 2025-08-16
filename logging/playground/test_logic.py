import sys
import unittest
from unittest.mock import Mock, patch
from pathlib import Path

# sys.path.append(str(Path(__file__).parent / 'playground'))

from blackjack import GameOver, Player, play_round, score
from cards import Card, Deck


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

    def setUp(self) -> None:
        # Always returns an 's'
        self.test_act_callable = Mock(return_value='s')
        # Always returns a 100
        self.test_bet_callable = Mock(return_value=100)

    def test_play_round_raises_game_over(self):
        player = Player()
        player.money = 0
        with self.assertRaises(GameOver):
            play_round(player, Player(), Deck(), self.test_act_callable, self.test_bet_callable)

    def test_play_round_player_wins(self):
        player = Player()
        dealer = Player()

        deck = Deck()
        # Replace the cards in the deck with 4 pre-defined cards.
        deck.cards = [card('K'), card('A'), card('K'), card('Q')]

        play_round(player, dealer, deck, self.test_act_callable, self.test_bet_callable)
        # Confirm that the player earned the correct amount of money for winning.
        self.assertEqual(player.money, 1200)

    def test_play_round_player_loses(self):
        player = Player()
        dealer = Player()

        deck = Deck()
        deck.cards = [card('K'), card('Q'), card('K'), card('A')]

        play_round(player, dealer, deck, self.test_act_callable, self.test_bet_callable)
        # Confirm that the player lost the correct amount of money.
        self.assertEqual(player.money, 900)


# If this code is being run as a script, test the game.
if __name__ == '__main__':
    print(unittest.main(verbosity=1, failfast=True))

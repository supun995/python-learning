import os
from cards import Card, Deck

import logging

logging.basicConfig(filename='blackjack.log', encoding='utf-8', level=logging.DEBUG)
logger = logging.getLogger('blackjack')


class GameOver(Exception):
    ''' An exception raised when the player is out of money. '''


class Player:
    ''' Represents a blackjack player - which includes a dealer. '''

    def __init__(self):
        self.money = 1_000
        self.cards = []


def prompt_for_bet(money: int) -> int:
    ''' Continuously prompt for a numeric bet until provided. '''
    try:
        wager = int(input(f'How much of your ${money} would you like to wager? '))
        logger.info(f'prompt_for_bet: {wager=}')
        return wager
    except ValueError:
        print('Your bet must be an integer. Example: 42')
        return prompt_for_bet(money)
    except:
        raise


def score(cards: list[Card]) -> int:
    ''' Calculate the score for the set of cards. '''
    logger.debug(f'score: {cards=}')
    scores = {
        'A': 11,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '10': 10,
        'J': 10,
        'Q': 10,
        'K': 10,
    }

    score = sum([scores[card.rank] for card in cards]) or 0
    # Adjust the score if needed to allow aces to be used as 1.
    for card in cards:
        if score >= 21 and card.rank == 'A':
            score -= 10

    logger.info(f'score: {score=}')
    return score


def format_winner(winner: str) -> str:
    ''' Format the message displayed to the winner and return the str. '''
    winner = f'{winner.title()} wins!'
    winner = f'{winner:@^80}'  # center text inside an 80 character space.
    return winner


def format_cards(player: Player, dealer: Player) -> str:
    ''' Displays the cards for the player and dealer. '''
    cards = f'{"dealer":-^80}\n'
    cards += f'{" ".join([str(card) for card in dealer.cards])}\n'
    cards += f'{"player":-^80}\n'
    cards += f'{" ".join([str(card) for card in player.cards])}\n'
    cards += f'{"total: {}".format(score(player.cards)): ^80}'
    return cards


def clear_screen():
    ''' Clear the terminal screen using either cls on Windows otherwise clear.

        The double pipe operator || on Linux and Windows is used to
        attempt the first command and fallback to the second.

        So cls||clear attempts cls and if a non-zero status code is returned clear is attempted.
    '''
    os.system('cls||clear')


def play_round(player: Player, dealer: Player, deck: Deck, action_callable: callable = input,
               bet_callable: callable = prompt_for_bet):
    ''' Play a single round of blackjack.

        Args:
            player          | The player
            dealer          | The dealer
            deck            | The deck of cards to use
            action_callable | Callable used to prompt a user for an action.
                            |> The callable must accept 1 positional str argument representing the prompt to display to a player.
                            |> The callable must return a str representing the symbol for the desired action.
                            |>  -----------------
                            |> | action | symbol |
                            |>  -----------------
                            |> |   hit  |    h   |
                            |> |  stand |    s   |
                            |>  -----------------
            bet_callable    | Callable used to prompt a user for their bet.
                            |> The callable must accept 1 positional int argument representing a player's available money.
                            |> The callable must return a positive int representing the bet.


        ------------------- Warning -------------------
        This function mutates the provided arguments
        and will leave them in a non-deterministic state.
        -----------------------------------------------
    '''
    # Step 1
    # Ensure the player has enough money to play. If not, game over!
    if player.money == 0:
        logger.info('play_round: GameOver')
        raise GameOver("Game over! You're bankrupt!")

    # Begin the round by resetting the clearing the player and dealer's cards.
    dealer.cards = []
    player.cards = []

    # STEP 2
    # The round opens by prompting the player for a bet.
    # Until we have a bet we can't do anything else.
    # Ensure that the player has enough money to place the bet.
    while (rounds_wager := bet_callable(player.money)) > player.money:
        print(f'please change your bet. you bet ${rounds_wager}. you only have ${player.money}.')

    logger.info(f'play_round: {rounds_wager=}')

    # STEP 3
    # Deal two cards for the dealer. One needs to be face up.
    dealer.cards = [deck.deal(), deck.deal(faceup=False)]
    # Deal two cards for the player
    player.cards = [deck.deal() for _ in range(2)]

    logger.debug(f'play_round: {dealer.cards=}')
    logger.debug(f'play_round: {player.cards=}')
    # Render the cards to the console.
    clear_screen()
    print(format_cards(player, dealer))

    # STEP 4
    # The player needs to determine their next action.
    # Will they hit or stand?
    # By typing an s they'll stand.
    # By typing an h they'll hit.
    # Anything else will be ignored.
    while (action := action_callable('pick your action: (h)it (s)tand > ')) != 's':
        logger.info(f'play_round: {action=}')

        if action == 'h':
            # take another card for the player
            player.cards.append(deck.deal())
            # Everytime a player's cards change we need to render the cards.
            clear_screen()
            print(format_cards(player, dealer))

    # STEP 5
    # The dealer in a real game would determine for themself if they want to hit or stand.
    # We're going to create some basic rules to simulate a real person as the dealer.
    # While the score of the dealer's hand is less than 17 keep taking cards.
    while score(dealer.cards) < 17:
        dealer.cards.append(deck.deal())

    logger.debug(f'play_round: {dealer.cards=}')

    # STEP 6
    # Determine who won by comparing scores.
    # if the player scored 21 then they win.
    # if the dealer scored more than 21 the player wins.
    # if the player scores higher than the dealer and they didn't go over 21 then the player wins.
    dealers_score = score(dealer.cards)
    players_score = score(player.cards)
    logger.info(f'play_round: {dealers_score=}')
    logger.info(f'play_round: {players_score=}')

    # Who won...
    # This logic does not fully align with the actual rules of blackjack.
    if (players_score == 21 or dealers_score > 21 or (players_score >= dealers_score and players_score <= 21)):
        player.money += rounds_wager * 2
        winner = 'player'
    else:
        player.money -= rounds_wager
        winner = 'dealer'

    logger.info(f'play_round: {winner=}')
    # STEP 7
    # Display all the cards, including the dealer's previously hidden cards.
    # First need to make them faceup.
    # Then the next time display is called it'll show all cards.
    for card in dealer.cards:
        card.faceup = True

    clear_screen()
    print(format_cards(player, dealer))
    # Inform the player who won.
    print(format_winner(winner))


def play():
    ''' Continuously play until the player stops the code. '''
    player = Player()
    dealer = Player()
    deck = Deck()

    # Loop forever unless the code is interrupted by CTRL+C
    while True:
        deck.shuffle()
        play_round(player, dealer, deck)


if __name__ == '__main__':
    try:
        play()
    except GameOver as go:
        print(go)
    except:
        logger.exception('game stopped unexpectedly.')
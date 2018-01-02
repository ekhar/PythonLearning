# Blackjack Text Based

import random


# Setup Bankroll

class Bankroll:
    def __init__(self, bet, money=0):
        self.bet = bet
        self.money = money

    def lose(self):
        money_lost = -self.bet
        self.money = self.money + money_lost

    def win(self):
        money_won = self.bet
        self.money = self.money + money_won

    def tie(self):
        pass


# Define Card Values
card_values = {
    'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6,
    'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10,
    'Queen': 10, 'King': 10, 'Ace': 1, '': 0
}

game_cards = [
    'Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
    'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'Ace'
]


# Determine Points Held by Each Player

class Players:
    def __init__(self, card1, card2, card3='', card4=''):
        self.card1 = card1
        self.card2 = card2
        self.card3 = card3
        self.card4 = card4

    def card1_value(self):
        return card_values[self.card1]

    def card2_value(self):
        return card_values[self.card2]

    def card3_value(self):
        return card_values[self.card3]

    def card4_value(self):
        return card_values[self.card4]

    def total_value(self):
        total_value = self.card1_value() + self.card2_value() + \
                      self.card3_value() + self.card4_value()
        return int(total_value)


# Give Dealer and Player 2 Cards

dcard1 = random.choice(game_cards)
dcard2 = random.choice(game_cards)
dcard3 = random.choice(game_cards)
dcard4 = random.choice(game_cards)

pcard1 = random.choice(game_cards)
pcard2 = random.choice(game_cards)
pcard3 = random.choice(game_cards)
pcard4 = random.choice(game_cards)

dealercards = Players(dcard1, dcard2)
playercards = Players(pcard1, pcard2)


# Start The Game

class Winlose:
    def __init__(self, wins=0, loss=0):
        self.wins = wins
        self.loss = loss

    def lossgain(self):
        self.loss += 1

    def wingain(self):
        self.wins += 1


record = Winlose()

name = input("Hello! My name is Computer. What is your name? ")

wager = int(input("Ok {}, let's play a game of blackjack. How much money would you like to wager? ".format(name) + '$'))

playerbank = Bankroll(wager)


def losingsequence():
    global replay
    playerbank.lose()
    record.lossgain()
    print("My score is {}, and your score is {}. This means that I win!".format(dealercards.total_value(),
                                                                                playercards.total_value()))
    print("You have lost ${}. Your total money is now ${}".format(wager, playerbank.money))
    print("You have lost {} games and won {} games.".format(record.loss, record.wins))
    replay = input('Would you like to play again? (yes/no)')


def winningsequence():
    global replay
    playerbank.win()
    record.wingain()
    print("My score is {} and your's is {}. This means that you win!".format(dealercards.total_value(),
                                                                             playercards.total_value()))
    print("You have won ${}. Your total money is now ${}".format(wager, playerbank.money))
    print("You have lost {} games and won {} games.".format(record.loss, record.wins))
    replay = input('Would you like to play again? (yes/no)')


def tiesequence():
    global replay
    playerbank.tie()
    print("I have {} points and you have {} points.".format(dealercards.total_value(), playercards.total_value()))
    print('Oh its a tie game! You have ${}, left, the same as before.'.format(playerbank.money))
    print("You have earned $0. Your total money is now ${}".format(playerbank.money))
    print("You have lost {} games and won {} games.".format(record.loss, record.wins))
    replay = input('Would you like to play again? (yes/no)')


def blackjacksequence():
    global replay
    playerbank.win()
    record.wingain()
    print("Wow BLACKJACK! You now have $ {} total on the night".format(playerbank.money))
    print("You have won ${}. Your total money is now ${}".format(wager, playerbank.money))
    print("You have lost {} games and won {} games.".format(record.loss, record.wins))
    replay = input('Would you like to play again? (yes/no)')


def blackjack():
    print('{}, here are your two face up cards: the {} of spades and the {} of diamonds '.format(name, pcard1, pcard2))

    print("My one faceup card is the {} of hearts".format(dcard1))

    if playercards.total_value() == 21:

        blackjacksequence()

    elif playercards.total_value() == 11 and pcard1 == 'Ace' or pcard2 == 'Ace':

        blackjacksequence()

    else:

        stayhit = input('Would you like to hit or stay? (hit/stay)? ')

        if stayhit == 'stay':
            print('My second card is the {} of clubs.'.format(dcard2))
            if playercards.total_value() < dealercards.total_value():
                losingsequence()

            elif playercards.total_value() > dealercards.total_value():
                winningsequence()

            elif playercards.total_value() == dealercards.total_value():
                tiesequence()

        elif stayhit == 'hit':
            dealercards.card3 = dcard3
            playercards.card3 = pcard3
            print(
                "Your cards are the {} of spades, the {} of diamonds, and the {} of spades. "
                "My two face up cards are the {} and the {}".format(pcard1, pcard2, pcard3, dcard1, dcard2)
            )
            if playercards.total_value() > 21:
                losingsequence()

            elif playercards.total_value() == 21:
                blackjacksequence()

            elif playercards.total_value() < 21 and playercards.card1_value() + \
                    playercards.card2_value() == 10 and pcard3 == 'Ace':
                blackjacksequence()

            elif playercards.total_value() < 21:

                stayhit = input('Would you like to hit or stay? (hit/stay)')

            if stayhit == 'stay':
                if playercards.total_value() > 21:
                    losingsequence()

                elif playercards.total_value() == 21:
                    blackjacksequence()

                elif playercards.total_value() < 21 and playercards.card1_value()\
                        + playercards.card2_value() == 10 and pcard3 == 'Ace':
                    blackjacksequence()

                elif playercards.total_value() < 21:

                    if dealercards.total_value() > 21:
                        winningsequence()

                    elif dealercards.total_value() > playercards.total_value():
                        losingsequence()

                    elif dealercards.total_value() < playercards.total_value():
                        winningsequence()

                    elif dealercards.total_value() == playercards.total_value():
                        tiesequence()

            elif stayhit == 'hit':

                playercards.card4 = pcard4
                dealercards.card4 = dcard4

                print("Your cards are the {} of spades, the {} of diamonds, the {} of diamonds, "
                      "and now the {} of clubs.".format(pcard1, pcard2, pcard3, pcard4))

                print("My face up cards are the {} of hearts, the {} of clubs, "
                      "and now the {} of hearts".format(dcard1, dcard2, dcard3, dcard4))

                if playercards.total_value() > 21:
                    losingsequence()

                elif playercards.total_value() == 21:
                    blackjacksequence()

                elif playercards.total_value() < 21 and playercards.card1_value() + \
                        playercards.card2_value() + pcard3 == 10 and pcard4 == 'Ace':
                    blackjacksequence()

                elif playercards.total_value() < 21:

                    if dealercards.total_value() > 21:
                        winningsequence()

                    elif dealercards.total_value() > playercards.total_value():
                        losingsequence()

                    elif dealercards.total_value() < playercards.total_value():
                        winningsequence()

                    elif dealercards.total_value() == playercards.total_value():
                        tiesequence()


blackjack()

while replay == 'yes':
    dcard1 = random.choice(game_cards)
    dcard2 = random.choice(game_cards)
    pcard1 = random.choice(game_cards)
    pcard2 = random.choice(game_cards)

    blackjack()

# Detect for Blackjack
# Hit or Settle Option
# Determine if Over/Under
# Another Hit/Settle Option if needed
# Determine Winner
# Update Bankroll

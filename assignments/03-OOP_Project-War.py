#####################################
### WELCOME TO YOUR OOP PROJECT #####
#####################################

# For this project you will be using OOP to create a card game. This card game will
# be the card game "War" for two players, you an the computer. If you don't know
# how to play "War" here are the basic rules:
#
# The deck is divided evenly, with each player receiving 26 cards, dealt one at a time,
# face down. Anyone may deal first. Each player places his stack of cards face down,
# in front of him.
#
# The Play:
#
# Each player turns up a card at the same time and the player with the higher card
# takes both cards and puts them, face down, on the bottom of his stack.
#
# If the cards are the same rank, it is War. Each player turns up three cards face
# down and one card face up. The player with the higher cards takes both piles
# (six cards). If the turned-up cards are again the same rank, each player places
# another card face down and turns another card face up. The player with the
# higher card takes all 10 cards, and so on.
#
# There are some more variations on this but we will keep it simple for now.
# Ignore "double" wars
#
# https://en.wikipedia.org/wiki/War_(card_game)

from random import shuffle

# Two useful variables for creating Cards.
SUITES = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
POINTS = {'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':10,'Q':10,'K':10,'A':11}

class Deck:
    """
    This is the Deck Class. This object will create a deck of cards to initiate
    play. You can then use this Deck list of cards to split in half and give to
    the players. It will use SUITE and RANKS to create the deck. It should also
    have a method for splitting/cutting the deck in half and Shuffling the deck.
    """
    cards = []

    def __init__(self):
        for suite in SUITES:
            for rank in RANKS:
                self.cards.append({'suite':suite,'rank':rank})

    def shuffle(self):
        shuffle(self.cards)

    def cut(self):
        return (self.cards[0:int(len(self.cards)/2)],self.cards[int(len(self.cards)/2):])



class Hand:
    '''
    This is the Hand class. Each player has a Hand, and can add or remove
    cards from that hand. There should be an add and remove card method here.
    '''
    def __init__(self, hand_cards):
        self.hand_cards = hand_cards

    def add_cards(self, cards):
        self.hand_cards.append(cards)

    def draw_card(self):
        return self.hand_cards.pop(0)

    def __len__(self):
        return len(self.hand_cards)

    def __str__(self):
        return str(self.hand_cards)



class Player:
    """
    This is the Player class, which takes in a name and an instance of a Hand
    class object. The Player can then play cards and check if they still have cards.
    """
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def play_cards(self, num_of_cards):
        cards_played = []
        for i in range(0,num_of_cards):
            cards_played.append(self.hand.draw_card())
        return cards_played

    def check_cards(self):
        return len(self.hand)



######################
#### GAME PLAY #######
######################
def main():
    print("Welcome to War, let's begin...\n")

    name1 = input('What is your name?\n')
    name2 = 'GladOS'

    deck = Deck()
    deck.shuffle()

    cut_deck = deck.cut()

    player1 = Player(name1,Hand(cut_deck[0]))
    player2 = Player(name2,Hand(cut_deck[1]))

    print('Deck has been shuffled and cards have been dealt.\n')

    while True:
        task = input('\nHey {}, what do you want to do? Type "draw" to draw a card and play a round or "check" to check your current number of cards. You can also type "exit" to leave the game.\n'.format(player1.name))

        if task == 'exit':
            break

        if task != 'draw' and task != 'check':
            print('Not a valid input!')
            continue

        if task == 'check':
            print('You currently have {} cards left.\n'.format(player1.check_cards()))
            continue

        if task == 'draw':
            cards1 = player1.play_cards(1)
            cards2 = player2.play_cards(1)
            print('\n{} played a {} of {}.'.format(player1.name,cards1[0]['rank'],cards1[0]['suite']))
            print('\n{} played a {} of {}.'.format(player2.name,cards2[0]['rank'],cards2[0]['suite']))

            if POINTS[cards1[0]['rank']] > POINTS[cards2[0]['rank']]:
                print('\n{} wins this round!'.format(player1.name))
                player1.hand.add_cards(cards1)
                player1.hand.add_cards(cards2)
            elif POINTS[cards1[0]['rank']] < POINTS[cards2[0]['rank']]:
                print('\n{} wins this round!'.format(player2.name))
                player2.hand.add_cards(cards1)
                player2.hand.add_cards(cards2)

            else:
                print("\nNOW IT'S WAR!!")
                for i in range(0,4):
                    cards1.append(player1.play_cards(1)[0])
                    cards2.append(player2.play_cards(1)[0])
                print('\n{} played a {} of {}.'.format(player1.name,cards1[4]['rank'],cards1[4]['suite']))
                print('\n{} played a {} of {}.'.format(player2.name,cards2[4]['rank'],cards2[4]['suite']))

                if POINTS[cards1[4]['rank']] > POINTS[cards2[4]['rank']]:
                    print('\n{} wins the war!'.format(player1.name))
                    player1.hand.add_cards(cards1)
                    player1.hand.add_cards(cards2)
                elif POINTS[cards1[4]['rank']] < POINTS[cards2[4]['rank']]:
                    print('\n{} wins the war!'.format(player2.name))
                    player2.hand.add_cards(cards1)
                    player2.hand.add_cards(cards2)
                else:
                    print('\nThe war is over. Nobody wins, only death and sorrow remain..')
    # Use the 3 classes along with some logic to play a game of war!

if __name__ == '__main__':
    main()

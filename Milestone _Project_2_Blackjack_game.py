# Developed by Farid Zarbaliyev (@sehrbaz) as Milestone Project 2 - Python Bootcamp
import random

suits = ['♥', '♦', '♠', '♣']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10',
         'J', 'Q', 'K', 'A']
values = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7,
          '8':8, '9':9, '10':10, 'J':10,
         'Q':10, 'K':10, 'A':11}

playing = True


class Card(object):

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + self.suit


class Deck(object):
    """
    Card deck of 52 cards
    """
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))


    def __str__(self):
        deckviz = ""
        for card in self.deck:
            deckviz += " | " + card.__str__()
        return deckviz


    def shuffle(self):
        random.shuffle(self.deck)


    def deal(self):
        card = self.deck.pop()
        return card


class Hand(object):

    def __init__(self):
        self.cards = []
        self.values = 0
        self.aces= 0

    def add_card(self, card):
        self.cards.append(card)
        self.values += values[card.rank]

    def adjust_for_ace(self):
        if self.values > 21 and self.aces:
            self.values -= 10
            self.aces -= 1


class Chips(object):
    def __init__(self):
        self.total = 100
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


def take_bet(chips):
    while True:
        try:
            chips.bet = int(input("How much would you like to bet: "))
            if chips.bet <= chips.total:
                pass
            else:
                raise Exception("not enough money")
        except ValueError:
            print("Wrong type, integers only")
        except:
            print("You don't have that much money")
        else:
            break


def hit(deck, hand):
    hit_deal = deck.deal()
    hit_hand = hand.add_card(hit_deal)
    hand.adjust_for_ace()



def hit_or_stand(deck,hand):
    global playing
    while playing:
        player_action = str(input("You want to hit or bet, h to hit, s to stand: "))
        if player_action == 'h':
            hit(deck, hand)
        elif player_action == 's':
            playing = False
        else:
            print("Wrong input, h to hit, s to stand")
            continue
        break




def show_some(player, dealer):
    player_cards = " | "
    dealer_cards = " | XX | "
    dealer = dealer.copy()
    for card in player:
        player_cards += card.__str__() + " | "
    del dealer[0]
    for card in dealer:
        dealer_cards += card.__str__() + " | "

    print("Player hand is:", player_cards, "Value:", player_hand.values)
    print("Dealer hand is:", dealer_cards)

def show_all(player,dealer):
    player_cards = " | "
    dealer_cards = " | "

    for card in player:
        player_cards += card.__str__() + " | "
    for card in dealer:
        dealer_cards += card.__str__() + " | "

    print("Player hand is:", player_cards, "Value:", player_hand.values)
    print("Dealer hand is:", dealer_cards, "Value:", dealer_hand.values)


def player_busts(player,dealer,chips):
    print('you loose')
    player_chips.lose_bet()

def player_wins(player,dealer,chips):
    print('you win!')
    player_chips.win_bet()

def dealer_busts(player,dealer,chips):
    print("Dealer busts, you win!")
    player_chips.win_bet()

def dealer_wins(player,dealer,chips):
    print("You loose, dealer wins")
    player_chips.lose_bet()

def push(player,dealer):
    print('The game is tie')

if __name__ == "__main__":
    player_chips = Chips()
    print('Your total chips', player_chips.total)
    while True:
        print('The new game started')
        deck = Deck()
        deck.shuffle()
        player_hand = Hand()
        dealer_hand = Hand()
        for i in range(2):
            player_hand.add_card(deck.deal())
            dealer_hand.add_card(deck.deal())
        take_bet(player_chips)

        show_some(player_hand.cards, dealer_hand.cards)

        while playing:
            hit_or_stand(deck, player_hand)
            show_some(player_hand.cards, dealer_hand.cards)

            if player_hand.values > 21:
                player_busts(player_hand, dealer_hand, player_chips)
                break

        if player_hand.values <= 21:
            while dealer_hand.values < 17:
                hit(deck, dealer_hand)

            show_all(player_hand.cards, dealer_hand.cards)
            if dealer_hand.values > 21:
                dealer_busts(player_hand, dealer_hand, player_chips)

            elif dealer_hand.values > player_hand.values:
                dealer_wins(player_hand, dealer_hand, player_chips)

            elif dealer_hand.values < player_hand.values:
                player_wins(player_hand, dealer_hand, player_chips)

            else:
                push(player_hand, dealer_hand)

        print('Your total chips', player_chips.total)
        again = str(input('Do you want to continue? y for yes, n for no: '))
        if again == 'n':
            print('Burn in hell, goodbye :)')
            break
        elif again == 'y':
            playing = True
            continue

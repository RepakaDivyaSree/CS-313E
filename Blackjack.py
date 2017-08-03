#  File: Blackjack.py

#  Description: program to play blackjack

#  Student's Name: Eun Seo

#  Student's UT EID: es29857

#  Partner's Name: Adam Roach

#  Partner's UT EID: abr875

#  Course Name: CS 313E

#  Unique Number: 50945

#  Date Created: 02/10/2016

#  Date Last Modified: 02/11/2016

import random

class Card (object):
  RANKS = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)

  SUITS = ('C', 'D', 'H', 'S')

  def __init__ (self, rank = 12, suit = 'S'):
    if (rank in Card.RANKS):
      self.rank = rank
    else:
      self.rank = 12

    if (suit in Card.SUITS):
      self.suit = suit
    else:
      self.suit = 'S'

  def __str__ (self):
    if (self.rank == 1):
      rank = 'A'
    elif (self.rank == 13):
      rank = 'K'
    elif (self.rank == 12):
      rank = 'Q'
    elif (self.rank == 11):
      rank = 'J'
    else:
      rank = str (self.rank)
    return rank + self.suit

  def __eq__ (self, other):
    return (self.rank == other.rank)

  def __ne__ (self, other):
    return (self.rank != other.rank)

  def __lt__ (self, other):
    return (self.rank < other.rank)

  def __le__ (self, other):
    return (self.rank <= other.rank)

  def __gt__ (self, other):
    return (self.rank > other.rank)

  def __ge__ (self, other):
    return (self.rank >= other.rank)

class Deck (object):
  def __init__ (self):
    self.deck = []
    for suit in Card.SUITS:
      for rank in Card.RANKS:
        card = Card (rank, suit)
        self.deck.append (card)

  def shuffle (self):
    random.shuffle (self.deck)

  def deal (self):
    if (len(self.deck) == 0):
      return None
    else:
      return self.deck.pop(0)

class Player (object):
  # cards is a list of card objects
  def __init__ (self, cards):
    self.cards = cards
    self.bust = False

  # when a player hits append a card
  def hit (self, card):
    self.cards.append (card)

  # gives a string of the player's cards seperated by a space
  def get_cards (self):
    hand_str = ''
    for card in self.cards:
      hand_str += str(card) + ' '

    return hand_str

  def get_points (self):
    count = 0
    for card in self.cards:
      if card.rank > 9:
        count += 10
      elif card.rank == 1:
        count += 11
      else:
        count += card.rank

    # deduct 10 if Ace is there and and needed as 1
    for card in self.cards:
      if count <= 21:
        break
      elif card.rank == 1:
        count = count - 10

    return count

  def busted (self):
    self.bust = True

class Dealer(Player):
  def __init__ (self, cards):
    # superclass Player
    super(Dealer, self).__init__(cards)

  # shows the dealer's first card as a string
  def get_first_card (self):
    card_str = str(self.cards[0])
    return card_str



class Blackjack(object):
  def __init__ (self, num_players):
    self.deck = Deck()  # create a deck
    self.deck.shuffle()
    self.players = []
    numcards_in_hand = 2

    for i in range (num_players):
      # start dealing out hands
      hand = []
      for j in range (numcards_in_hand):
        hand.append (self.deck.deal())
      self.players.append (Player(hand))

    # add the Dealer's hand to the game
    dealer_hand = []
    for j in range (numcards_in_hand):
      dealer_hand.append (self.deck.deal())
    self.dealer = (Dealer(dealer_hand))


  
  # play a game of Blackjack
  def play (self):
    print()
    # print out each player's cards and points
    for i in range (len(self.players)):
      print('Player ' + str(i+1) + ": " + self.players[i].get_cards() + "- " + str(self.players[i].get_points()) + " points")
      
    # print out the dealer's cards and points

    print('Dealer: ' + self.dealer.get_first_card())
    print()

    # let each player have a turn
    for i in range(len(self.players)):
      player = self.players[i]
      # ask user for hit (y/n)
      answer = 'y'
      while answer != 'n' and player.get_points() < 21:
        answer = (input("Player " + str(i+1) + ", do you want to hit? [y / n]: "))
        if (answer == 'y'):
          player.hit(self.deck.deal())
          print('Player ' + str(i+1) + ": " + self.players[i].get_cards() + "- " + str(self.players[i].get_points()) + " points")

      # if the player is over 21 points, he busts
      if player.get_points() > 21:
        player.busted()

      print()

    # play the dealer's hand then print it
    while (self.dealer.get_points() < 17):
      self.dealer.hit(self.deck.deal())

    print('Dealer: ' + self.dealer.get_cards() + "- " + str(self.dealer.get_points()) + " points")

    # check whether the dealer busted, set accordingly
    if self.dealer.get_points() >= 21:
      self.dealer.busted()

    print()

    # make a list of the players who are still standing
    standing = []
    for player in self.players:
      if not player.bust:
        standing.append(player)

    # check everyone's points and say who wins or ties
    if self.dealer.bust:
      for i,player in enumerate(self.players):
        if player in standing:
          print('Player', str(i+1), 'wins')
        else:
          print('Player', str(i+1), 'loses')

    elif not self.dealer.bust:
      for i,player in enumerate(self.players):
        if player in standing:
          if (player.get_points() > self.dealer.get_points()):
            print('Player', str(i+1), 'wins')
          elif player.get_points() == self.dealer.get_points():
            print('Player', str(i+1), 'ties')
          else:
            print('Player', str(i+1), 'loses')
        else:
          # players in bust
          print('Player', str(i+1), 'loses')

    print()

  # does the player have 21 points or not
  def has_blackjack (self):
    return (len(self.cards) == 2) and (self.get_points() == 21)



def main():
  # prompt user to enter the number of players
  num_players = int (input ('Enter number of players: '))
  

  while ((num_players < 1) or (num_players > 6)):
    num_players = int (input ('Enter number of players: '))

  # create a blackjack game object
  game = Blackjack(num_players)
  
  game.play()



main()
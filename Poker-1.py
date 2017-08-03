#  File: Poker.py

#  Description: program to play poker

#  Student's Name: Eun Seo

#  Student's UT EID: es29857

#  Partner's Name: Marion Milloy

#  Partner's UT EID: mm69994

#  Course Name: CS 313E

#  Unique Number: 50945

#  Date Created: 02/10/2016

#  Date Last Modified: 02/10/2016


import random
class Card (object):
  RANKS = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)
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
    if (self.rank == 14):
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
      # return last card?
      return self.deck.pop(0)

class Poker (object):
  # all functions under classes are methods
  # methods = functions defined under a class
  # self is a tag that allows you to have access to the class' methods
  def __init__ (self, num_players):
    self.deck = Deck()  # create a deck
    self.deck.shuffle()
    self.players = []
    numcards_in_hand = 5

    for i in range (num_players):
      # start dealing out hands
      hand = []
      for j in range (numcards_in_hand):
        hand.append (self.deck.deal())
      self.players.append (hand)


  def play (self):
    # sort the hands of each player and print
    for i in range (len(self.players)):
      sortedHand = sorted (self.players[i], reverse = True)
      self.players[i] = sortedHand
      hand = ''
      for card in sortedHand:
        hand = hand + str (card) + ' '
      print ('Player ' + str (i + 1) + " : " + hand)

    # determine the each type of hand and print
    points_hand = []  # create list to store points for each hand

  # determine if a hand is a royal flush
  def is_royal (self, hand):
    same_suit = True
    for i in range (len(hand) - 1):
      same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)

    if (not same_suit):
      return False

    # only reach here if same_suit is true
    rank_order = True
    for i in range (len(hand)):
      rank_order = rank_order and (hand[i].rank == 14 - i)

    return (same_suit and rank_order)


  # determine if a hand is straight flush
  def is_straight_flush (self, hand):
    # check if first card starts with A
    for i in range (len(hand) - 1):
      if (hand[i].rank == 14):
        return False

    same_suit = True
    for i in range (len(hand) - 1):
      same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)

    if (not same_suit):
      return False
    rank_order = True

    for i in range (len(hand) - 1):
      rank_order = rank_order and (hand[i].rank == (hand[i + 1].rank + 1))
    return (same_suit and rank_order)

  # If there are two straight flushes, then which ever hand has the highest card value wins. In the above example, Hand 2 wins.

  def is_four_kind (self, hand):
    if (hand[0].rank == hand[1].rank) and (hand[1].rank == hand[2].rank) and (hand[2].rank == hand[3].rank):
      return True
    elif (hand[1].rank == hand[2].rank) and (hand[2].rank == hand[3].rank) and (hand[3].rank == hand[4].rank):
      return True
    else:
      return False
  # In the event of a tie the hand that has highest ranking four of a kind cards wins. In the above example, Hand 2 wins.

  def is_full_house (self, hand):
    if (hand[0].rank == hand[1].rank) and (hand[1].rank == hand[2].rank):
      if (hand[3].rank == hand[4].rank):
        if (hand[0].rank != hand[3].rank):
          return True
        else:
          return False
      else:
        return False

    elif (hand[2].rank == hand[3].rank) and (hand[3].rank == hand[4].rank):
      if (hand[0].rank == hand[1].rank):
        if (hand[2].rank == hand[0].rank):
          return False
        else:
          return True
      else:
          return False
    else:
      return False
  # If there are two full houses, then the hand that has the higher ranking cards for the three of a kind wins. In the above example, Hand 2 wins.

  def is_flush (self, hand):
    for i in range (0, len(hand)-1):
      if (hand[i].suit == hand[i + 1].suit):
        return True
      else:
        return False
    # In the event of two flushes, the one with the highest ranking card wins. In the above example, Hand 1 wins

  def is_straight (self, hand):
    # check if 5 cards in numerical order
    for i in range (0, len(hand)-1):
      if (hand[i].rank == (hand[i+1].rank + 1)):
        return True
      else:
        return False

    # When there are two straight hands, then the one with the highest ranking card wins. In the above example, Hand 2 wins.


  def is_three_kind (self, hand):
    if (hand[0].rank == hand[1].rank) and (hand[1].rank == hand[2].rank):
      if (hand[3].rank != hand[4].rank):
        return True
      else:
        return False

    elif (hand[1].rank == hand[2].rank) and (hand[2].rank == hand[3].rank):
      if (hand[0].rank != hand[4].rank):
        return True
      else:
        return False

    elif (hand[2].rank == hand[3].rank) and (hand[3].rank == hand[4].rank):
      if (hand[0].rank != hand[1].rank):
        return True
      else:
        return False
    else:
      return False


  def is_two_pair (self, hand):
    if (hand[0].rank == hand[1].rank) and (hand[2].rank == hand[3].rank):
      if (hand[0].rank != hand[4].rank) and (hand[2].rank != hand[4].rank):
        return True
      else:
        return False
    else:
      return False
    ...

  # determine if a hand is one pair
  def is_one_pair (self, hand):
    for i in range (len(hand) - 1):
      if (hand[i].rank == hand[i + 1].rank):
        return True
    return False


  def is_high_card (self, hand):
    # return hand with highest rank, or very first card
    return hand[0].rank




def main():
  # prompt user to enter the number of players
  num_players = int (input ('Enter number of players: '))
  print()
  while ((num_players < 2) or (num_players > 6)):
    num_players = int (input ('Enter number of players: '))

  # create the Poker object
  game = Poker (num_players)

  # play the game (poker), sorts and prints out hand
  game.play()

  # add up total points
  hand_type = []
  pt_list = []
  for i in range (num_players):
    # create a new list to hold all of the players' total points
    # current player's current hand
    players_hand = game.players[i]
    if (game.is_royal(players_hand)):
      pt_list.append(10)
      hand_type.append('Royal Flush')
    elif (game.is_straight_flush(players_hand)):
      pt_list.append(9)
      hand_type.append('Straight Flush')
    elif (game.is_four_kind(players_hand)):
      pt_list.append(8)
      hand_type.append('Four of a Kind')
    elif (game.is_full_house(players_hand)):
      pt_list.append(7)
      hand_type.append('Full House')
    elif (game.is_flush(players_hand)):
      pt_list.append(6)
      hand_type.append('Flush')
    elif (game.is_straight(players_hand)):
      pt_list.append(5)
      hand_type.append('Straight')
    elif (game.is_three_kind(players_hand)):
      pt_list.append(4)
      hand_type.append('Three of a Kind')
    elif (game.is_two_pair(players_hand)):
      pt_list.append(3)
      hand_type.append('Two Pair')
    elif (game.is_one_pair(players_hand)):
      pt_list.append(2)
      hand_type.append('One Pair')
    elif (game.is_high_card(players_hand)):
      pt_list.append(1)
      hand_type.append('High Card')

  print()

  for i in range(num_players):
    print ("Player %d : %s" %(i+1, hand_type[i]) )

  final_points = []
  for i in range(num_players):
    # for each card in player's hand
    c1 = game.players[i][0].rank
    c2 = game.players[i][1].rank
    c3 = game.players[i][2].rank
    c4 = game.players[i][3].rank
    c5 = game.players[i][4].rank

    h = pt_list[i]

    players_final_points = h * 13**5 + c1 * 13**4 + c2 * 13**3 + c3 * 13**2 + c4 * 13 + c5

    final_points.append(players_final_points)

  tie_list = []
  player_number = 1
  winner = final_points[0]
  for i in range(num_players):
    if (final_points[i] > winner):
      tie_list = []
      winner = final_points[i]
      player_number = i + 1
    elif (final_points[i] == winner):
      tie_list.append(i + 1)

  if (len(tie_list) > 1):
    for i in range(len(tie_list)):
      print("Player %d ties." %(tie_list[i]), '\n')

  print()

  print("Player %d wins." %(player_number))


main()

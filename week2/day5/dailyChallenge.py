# Exercise 1: Quizz
# Answer the following questions:

'''What is a class?'''
# A class is a blueprint for the creation of instances (or objects) sharing its attributes
#                  and functions.

'''What is an instance?'''
# An instance is an object that has features like attributes and functions determined by
#                      its class.

''' What is encapsulation? '''
# It is bundling related data and the methods that operate on that data into a class
#                        and controlling access to that data from the outside.

''' What is abstraction? '''
# It is transcending without too much worry about how something works and just using it.
#                      In Python, for example it is giving access to things a user is concerned about and
#                      hiding those he does not need to know.

'''What is inheritance?'''
#  It allows one class (child) to inherit attributes and methods from its "parent" class,
#                      while at the same time being able to have its own features, for code reuse purposes.

''' What is multiple inheritance?'''
#  It allows children classes to inherit attributes and methods from its "parent"
#                               and "grandparent" classes,  while at the same time being able to have its own
#                               features, for code reuse purposes.

''' What is polymorphism?'''
# It enables you to have different objects responding to the same command in their own
#                      specific way (e.g. rectangles, circles, triangles are instances of the class "Shape"
#                      and they all can share a method called "calculate_area", calculated in their own way.)

''' What is method resolution order or MRO?'''
#  It is is the rulebook that Python uses to decide which method to run
#                                      when you call a method that exists in multiple parent classes.
#                                      1) A child class's method is always prioritized over a parent class's
#                                         method ( depth-first rule).
#                                      2) If multiple parents exist, their order in the class definition
#                                         matters (left-to-right rule).)


# Exercise 2: Create a deck of cards class
import random
suits = ["Hearts", "Diamonds", "Clubs", "Spades"]  # class attributes, valid for Card in general
# class attributes, valid for Card in general
values = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]


class Card():

    def __init__(self, suit, value):
        if suit not in suits:
            raise ValueError(f"Invalid suit: {suit}")
        if value not in values:
            raise ValueError(f"Invalid value: {value}")
        self.suit = suit  
        self.value = value

    def __str__(self):
        return f"A {self.value} of {self.suit}"


class Deck():
    def __init__(self):
        self.cards = []      #collects the cards in an empty list
        self._build_deck()   # we create a helper function to fill the deck (self.cards empty list)

    def _build_deck(self):        # defining the helper function "build_deck()
        self.cards = [Card(suit, value)
                      for suit in suits for value in values]
        # creates every possible card by combining each suit with each value
        # each Card(suit, value) is added to the list
        # nested loop inside a list comprehension -->
        # after all loops finish, you get a list of 52 Card objects

    def shuffle(self):
        if len(self.cards) != 52:            # ensure deck has all 52 cards before shuffling
            self._build_deck()
        random.shuffle(self.cards)

    def deal(self):
        if len(self.cards) == 0:
            raise IndexError("Cannot deal from an empty deck")
        # if there are cards, it removes the last card from the list and returns it
        return self.cards.pop()


deck1 = Deck()   # we create a deck intance
deck1.shuffle()  # we shuffle it so the cards are in random order

print("Dealing 5 cards:")
for _ in range(5):          # _ indicates a placeholder in the range 
    card = deck1.deal()     # we call the deal() function to return the last card from the list
    print(card)             # we print the card in question

print(f"Cards left in deck: {len(deck1.cards)}")

deck2 = Deck()
deck2.shuffle()

print("Dealing 10 cards")
for _ in range(10):
    card = deck2.deal()         
    print(card)

print(f"Cards left in deck: {len(deck2.cards)}")

"""
Instructions
In this exercise you are going to implement some rules of Blackjack, such as the way the game is played and scored.

Note : In this exercise, A means ace, J means jack, Q means queen, and K means king. Jokers are discarded. A standard French-suited 52-card deck is assumed, but in most versions, several decks are shuffled together for play.

Task 1
Calculate the value of a card

In Blackjack, it is up to each individual player if an ace is worth 1 or 11 points (more on that later). Face cards (J, Q, K) are scored at 10 points and any other card is worth its "pip" (numerical) value.

Define the value_of_card(<card>) function with parameter card. The function should return the numerical value of the passed-in card string. Since an ace can take on multiple values (1 or 11), this function should fix the value of an ace card at 1 for the time being. Later on, you will implement a function to determine the value of an ace card, given an existing hand.

Task 2
Determine which card has a higher value

Define the higher_card(<card_one>, <card_two>) function having parameters card_one and card_two. For scoring purposes, the value of J, Q or K is 10. The function should return which card has the higher value for scoring. If both cards have an equal value, return both. Returning both cards can be done by using a comma in the return statement:
An ace can take on multiple values, so we will fix A cards to a value of 1 for this task.

Task 3
Calculate the value of an ace
As mentioned before, an ace can be worth either 1 or 11 points. Players try to get as close as possible to a score of 21, without going over 21 (going "bust").

Define the value_of_ace(<card_one>, <card_two>) function with parameters card_one and card_two, which are a pair of cards already in the hand before getting an ace card. Your function will have to decide if the upcoming ace will get a value of 1 or a value of 11, and return that value. Remember: the value of the hand with the ace needs to be as high as possible without going over 21.

Hint: if we already have an ace in hand then its value would be 11.

Task 4
Determine a "Natural" or "Blackjack" Hand

If the first two cards a player is dealt are an ace (A) and a ten-card (10, K, Q or J), giving a score of 21 in two cards, the hand is considered a natural or blackjack.

Define the is_blackjack(<card_one>, <card_two>) function with parameters card_one and card_two, which are a pair of cards. Determine if the two-card hand is a blackjack, and return the boolean True if it is, False otherwise.

Note : The score calculation can be done in many ways. But if possible, we'd like you to check if there is an ace and a ten-card in the hand (or at a certain position), as opposed to summing the hand values.

Task 5
Splitting pairs

If the players first two cards are of the same value, such as two sixes, or a Q and K a player may choose to treat them as two separate hands. This is known as "splitting pairs".

Define the can_split_pairs(<card_one>, <card_two>) function with parameters card_one and card_two, which are a pair of cards. Determine if this two-card hand can be split into two pairs. If the hand can be split, return the boolean True otherwise, return False

Task 6
Doubling down

When the original two cards dealt total 9, 10, or 11 points, a player can place an additional bet equal to their original bet. This is known as "doubling down".

Define the can_double_down(<card_one>, <card_two>) function with parameters card_one and card_two, which are a pair of cards. Determine if the two-card hand can be "doubled down", and return the boolean True if it can, False otherwise.
"""


def value_of_card(card):
    if card.isdigit():
        return int(card)
    elif card == "K" or card == "J" or card =="Q":
        return 10
    elif card == "A":
        return 1
    else:
         return False

def higher_card(card_one, card_two):
    value_one = value_of_card(card_one)
    value_two = value_of_card(card_two)

    if value_one > value_two:
        return card_one
    elif value_one < value_two:
        return card_two
    else:
        return card_one, card_two


def value_of_ace(card_one, card_two):
    value_one = value_of_card(card_one)
    value_two = value_of_card(card_two)
    if "A" in card_one:
        value_one = 10
    if "A" in card_two:
        value_two = 10
    
    if value_one + value_two <= 10:
        ace_value = 11
    else:
        ace_value = 1
    return ace_value
    

  
       


def is_blackjack(card_one, card_two):
    value_one = value_of_card(card_one)
    value_two = value_of_card(card_two)
    if "A" in card_one and value_two == 10:
        return True
    elif value_one == 10 and "A" in card_two:
        return True
    else:
        return False


def can_split_pairs(card_one, card_two):
    value_one = value_of_card(card_one)
    value_two = value_of_card(card_two)

    if value_one == value_two:
       return True
    else:
       return False


def can_double_down(card_one, card_two):
    value_one = value_of_card(card_one)
    value_two = value_of_card(card_two)

    if value_one + value_two == 9 or value_one +value_two == 10 or value_one + value_two == 11:
        return True
    else:
        return False


value_of_ace('A', '2')
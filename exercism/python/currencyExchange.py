"""
Instructions
Your friend Chandler plans to visit exotic countries all around the world. Sadly, Chandler's math skills aren't good. He's pretty worried about being scammed by currency exchanges during his trip - and he wants you to make a currency calculator for him. Here are his specifications for the app:

Task 1
Estimate value after exchange
Create the exchange_money() function, taking 2 parameters:
budget : The amount of money you are planning to exchange.
exchange_rate : The amount of domestic currency equal to one unit of foreign currency.
This function should return the value of the exchanged currency.
Note: If your currency is USD and you want to exchange USD for EUR with an exchange rate of 1.20, then 1.20 USD == 1 EUR.

Task 2
Calculate currency left after an exchange
Create the get_change() function, taking 2 parameters:
budget : Amount of money before exchange.
exchanging_value : Amount of money that is taken from the budget to be exchanged.
This function should return the amount of money that is left from the budget.

Task 3
Calculate value of bills
Create the get_value_of_bills() function, taking 2 parameters:
denomination : The value of a single bill.
number_of_bills : Amount of bills you received.
This exchanging booth only deals in cash of certain increments. The total you receive must be divisible by the value of one "bill" or unit, which can leave behind a fraction or remainder. Your function should return only the total value of the bills (excluding fractional amounts) the booth would give back. Unfortunately, the booth gets to keep the remainder/change as an added bonus.

Task 4
Calculate number of bills
Create the get_number_of_bills() function, taking budget and denomination.
This function should return the number of currency bills that you can receive within the given budget. In other words: How many whole bills of currency fit into the amount of currency you have in your budget? Remember -- you can only receive whole bills, not fractions of bills, so remember to divide accordingly. Effectively, you are rounding down to the nearest whole bill/denomination.
Calculate leftover after exchanging into bills
Create the get_leftover_of_bills() function, taking budget and denomination.
This function should return the leftover amount that cannot be exchanged from your budget given the denomination of bills. It is very important to know exactly how much the booth gets to keep.

Task 5
Calculate leftover after exchanging into bills
Create the get_leftover_of_bills() function, taking budget and denomination.
This function should return the leftover amount that cannot be exchanged from your budget given the denomination of bills. It is very important to know exactly how much the booth gets to keep.

Task 6
Calculate value after exchange
Create the exchangeable_value() function, taking budget, exchange_rate, spread, and denomination.
Parameter spread is the percentage taken as an exchange fee, written as an integer. It needs to be converted to decimal by dividing it by 100. If 1.00 EUR == 1.20 USD and the spread is 10, the actual exchange rate will be: 1.00 EUR == 1.32 USD because 10% of 1.20 is 0.12, and this additional fee is added to the exchange.
This function should return the maximum value of the new currency after calculating the exchange rate plus the spread. Remember that the currency denomination is a whole number, and cannot be sub-divided.
Note: Returned value should be int type.
"""

import math
#Task 1 
def exchange_money(budget,exchange_rate):
    budget = float(budget)
    exchange_rate= float(exchange_rate)
    exchanged_currency = round(budget / exchange_rate),2
    return exchanged_currency

#Task 2
def get_change(budget,exchanging_value):
    budget = float(budget)
    money_left = budget - exchanging_value
    return money_left

#Task 3 
def get_value_of_bills(denomination,number_of_bills):
    if (number_of_bills % denomination) == 0:
        value = denomination * number_of_bills
        return value
    else:
        value = math.floor(denomination * number_of_bills)
        return value
    
#Task 4
def get_number_of_bills(budget, denomination):
    budget = float(budget)
    amount_currency = budget / denomination
    amount_currency = math.floor(amount_currency)
    return amount_currency

#Task 5
def get_leftover_of_bills(budget, denomination):
    budget = float(budget)
    leftover = budget % denomination
    return leftover

#Task 6
def exchangeable_value(budget, exchange_rate, spread, denomination):
    spread_decimal = spread / 100
    actual_exchange_rate = exchange_rate + (exchange_rate * spread_decimal)
    max_value = int((budget / actual_exchange_rate) // denomination) * denomination
    return max_value
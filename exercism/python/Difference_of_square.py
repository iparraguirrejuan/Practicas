"""Instructions
Find the difference between the square of the sum and the sum of the squares of the first N natural numbers.

The square of the sum of the first ten natural numbers is (1 + 2 + ... + 10)² = 55² = 3025.

The sum of the squares of the first ten natural numbers is 1² + 2² + ... + 10² = 385.

Hence the difference between the square of the sum of the first ten natural numbers and the sum of the squares of the first ten natural numbers is 3025 - 385 = 2640.

You are not expected to discover an efficient solution to this yourself from first principles; research is allowed, indeed, encouraged. Finding the best algorithm for the problem is a key skill in software engineering."""

def square_of_sum(number):
    number_array = list(range(1,number+1))
    suma_array = sum(number_array)
    square = suma_array**2
    return square
    


def sum_of_squares(number):
    number_array = list(range(1,number+1))
    squared_numbers= [i ** 2 for i in range(len(number_array)+1)]
    sum_square = sum(squared_numbers)
    return sum_square
    


def difference_of_squares(number):
    diff = square_of_sum(number) - sum_of_squares(number)
    return diff


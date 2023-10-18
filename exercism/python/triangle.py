"""
Determine if a triangle is equilateral, isosceles, or scalene.

An equilateral triangle has all three sides the same length.

An isosceles triangle has at least two sides the same length. (It is sometimes specified as having exactly two sides the same length, but for the purposes of this exercise we'll say at least two.)

A scalene triangle has all sides of different lengths."""

def equilateral(sides):
    a,b,c = sides
    if a  != 0 and b != 0 and c != 0:
        if a + b >= c and b + c >= a and a + c >= b:
            if a == b and b == c:
                return True
            else:
                return False
        else:
            return False    
    else:
        return False

def isosceles(sides):
    a,b,c = sides
    if a  != 0 and b != 0 and c != 0:
        if a + b >= c and b + c >= a and a + c >= b:
            if a == b or a == c or b == c:
                return True
            else:
                return False
        else:
            return False    
    else:
        return False

def scalene(sides):
    a,b,c = sides
    if a  != 0 and b != 0 and c != 0:
        if a + b >= c and b + c >= a and a + c >= b:
            if a != b and a != c and b != c:
                return True
            else:
                return False
        else:
            return False    
    else:
        return False
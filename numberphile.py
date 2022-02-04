from turtle import Turtle, Screen, exitonclick
from random import choice
from decimal import Decimal, getcontext
from pi_million import pi
from golden_ratio import phi

colors = ['red', 'green', 'blue', 'black']

screen = Screen()
screen.screensize(3840, 2160)

sam = Turtle()
# Set a random color
sam.color(choice(colors))
sam.pensize(2)
sam.speed(97)
sam.shape('classic')

def drawer(angle, paces):
    """Draw something given the angle and number of steps forward"""
    sam.left(angle)
    sam.forward(paces)

"""Base is the number of sides of a polygon, e.g, base 3 = a triangle, base 4 = a square """
def numberphile_one(range_num):
    """Draw a simple pattern"""
    for x in range(range_num):
        sam.color(choice(colors))
        drawer(x*1.0456,5)
        print(x)

def numberphile_pi(base, range_num):
    """Draw pattern given the base and the range using the digits of pi as a way to vary the angle"""
    xs = pi[:range_num+1]
    y = 0
    for x in xs:
        try:
            drawer(int(x)/base*360,7)
        except:
            pass
        print(y)
        y += 1

def numberphile_phi(base, range_num):
    """Draw pattern given the base and the range using the digits of phi as a way to vary the angle"""
    xs = phi[:range_num+1]
    y = 0
    for x in xs:
        try:
            drawer(int(x)/base*360,7)
        except:
            pass
        print(y)
        y += 1

def numberphile_fraction(numerator, denominator ,base, range_num):
    """Draw pattern given the base and the range using the digits of a fraction(numerator/denominator) as a way to vary the angle"""
    getcontext().prec = range_num+1
    num = Decimal(numerator) / Decimal(denominator)
    num = "{0}".format(num)
    xs = str(num)
    xs = num[:range_num+1]
    y = 0
    for x in xs:
        try:
            drawer(int(x)/base*360,1.5)
        except:
            pass
        print(y)
        y += 1

# numberphile_one(20000)
# numberphile_pi(3, 20000)
# numberphile_fraction(1, 7, 10, 10000)
numberphile_phi(4, 20000)

# Exit on click after drawing
exitonclick()

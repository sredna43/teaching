# As you've seen and done, functions can be made to return values. This is super useful.

import math

def f(x):
    return x ** x

def g(x):
    return x + 10

def h(x):
    return math.sqrt(x)

print(f(g(5))) # what will this print?
print(f(h(5))) # how about this?


# If this feels like a throwback to algebra or calculus, that's a good thing.
# Computer science is born from mathematics, and as such there is an incredible amout of overlap.

# Aside: Unreachable code

def bad_function():
    print("reachable")
    return
    print("unreachable")

# If you were to run this code, based upon the inherent hints, what do you suspect the outcome will be?
# More importantly, why?

# A great usecase of functions is to create your very own boolean operations. Here's an example as an exercise:

# Exercise: Create a function that takes in x and y and returns a boolean representing whether or not x is evenly divisible by y

def is_divisible(x, y):
    pass

print(is_divisible(10,5)) # True
print(is_divisible(10,3)) # False
# Let's talk about the modulus operator real quick, then get into conditionals.

# Basically, the modulus operator (%) gives you the remainder of two numbers after they've been divided by one another.
# That's a bit tricky to write and understand, here's an example.

# What do you think the output will be? Remember: the % is the modulus operator
print(5 % 3)
print(14 % 4)

# Cool, that's that. Real quick, write a function that takes in a time in 24hr format and converts it to 12hr format

def time_converter(hour, minute):
    pass # Replace this with your code! (Pass is a way to write a function that does nothing, or returns nothing. You'll see why this can be useful later.)


# Booleans! Boo!

# A boolean is simply a True/False expression. Here are some examples:
print(5 == 4) # False
print(5 == 5) # True

# Note the double equals sign, why do you think we need this rather than a single equals sign? Hint: variables

# Here are some more useful operators that result in boolean (T/F) expressions
x = 1
y = 2

print(x == y) # False
print(x != y) # True
print(x > y) # False
print(x < y) # True
print(x >= y) # False
print(x <= y) # True

# Note: there is no such thing as => or =<, and ! is a "negator". In this case, it means "not equal to"

print(not True) # False
print(not False) # True


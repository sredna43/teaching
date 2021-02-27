# Conjunction junction, what's your function?

# Believe it or not, you've already used some functions in python! Can you guess what they are?
# Here's a hint...

print("This is actually a function!")
print(type("And this is a function inside a function, whoa!"))

# As you probably guessed, we can make our own functions! Here's two:

def print_truth():
    print("Anders is super cool and awesome,")
    print("and everybody really likes him.")

def print_lies():
    print("Deidree is always on time,")
    print("and never has to change plans last minute.")

# note the indented lines, this is how we tell python what's contained in our functions... you'll see more of this later.

# We can call these functions by their name followed by parenthesis like this (Note: these are no longer indented, so not part of our functions):
print_truth()
print_lies()

# We can even call functions inside of functions like this:
def print_truths_and_lies():
    print_truth()
    print_lies()

# And call the function like this:
print_truths_and_lies()

# Python has plenty of built in math functions as well, some that you may find very useful! They come as a part of what's called a module.
# Modules have to be imported before we can use them. Here's how to do that. (Note: Modules are really just other files that people have made.)

import math

# Here's how you find the square root of a number:
print(math.sqrt(25))


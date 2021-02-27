# Now that we've seen some functions, you might be wondering about the parenthesis, and what they do.

# In a function definition, there are 3 main parts. The 'def' which tells the interpreter that this is a function definition,
# the name, which is what you'll use to call the function later on in the program, and the arguments.

# The arguments are objects that you can pass into a function, that then get used as parameters inside the function. A bit meta, let's look.

# definition, name, arguments
def my_function(arg1, arg2):
    print("Argument 1 is:", arg1)
    print("Argument 2 is:", arg2)

my_function("some text", 5)

# Notice the mixture of integers and strings? This actually doesn't cause a problem with python since python uses what's called 

# DUCK TYPING :))))

# If it looks like a duck, and quacks like a duck, chances are it's a duck!

# What this means is that you don't have to tell python ahead of time what kind of variable it should expect in a function like you'd have
# to in other languages. However, this can lead to issues where you may think you're passing one type of argument but you actually need another!


# Here's your challenge, write a function from scratch that takes in one argument, and prints it out three times on the same line.
# This is what it should look like: some_function("word") >> word word word


# Functions can also be used to return values, to be used later in the program, like this.

def vowel_swapper(phrase, old_vowel, new_vowel):
    return phrase.replace(old_vowel, new_vowel)

food = vowel_swapper("I like to eat apples and bananas", "a", "o")
print(food)


# Here's another fun challenge for you:
# Write a function that draws a grid like the following (without the quotes):
'''
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
'''
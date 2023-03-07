# Why would you ever want to use a conditional statement?

# Well, I know the concept of logic is a tricky one for you............. but it's important in programming!
# Let's say you want to run some piece of code, but you only want to run it if some condition is met.

# Here's a quick example:
def weather_checker(weather):
    good_weather = ["sunny", "partly cloudy", "calm"]

    if weather in good_weather:
        print("The weather is nice today!")
    else:
        print("The weather is not nice today.")

weather_checker("rainy")
weather_checker("sunny")

# Now, there are some things going on here that you haven't seen yet. First, is the 'in' operator.
# In python, we have lists. You saw a super quick intro to them in the 7th file of lesson 1.
# One of the ways we can check to see if a list contains a certain item is to use the 'in' operator as you just saw!

# Another thing you saw above, is an 'if, else' statement. I find these to be pretty self-explanatory, but note the syntax anyways.

# Let's look at chained conditional statements. Wtf is that, you're wondering... let's find out!
x = 5

if x > 5:
    print("x > 5")
elif x < 5:
    print("x < 5")
elif x == 4:
    print("x = 4")
elif x == 5:
    print("x = 5")
else: # Catch-all, might not be needed!
    print("wtf")

# As you can see, we have a funky thing called 'elif'. This is short for... you guessed it, else if!
# Again, self explanatory but good to know. Just know that you can have an unlimited number of elif statements!

# You can also have nested if statements as you might have guessed. Also can be unlimited.

if x == 5:
    if 3 == 3:
        if "sky" == "blue":
            print("not here")
        else:
            print("here!")
    else:
        print("math is broken")
else:
    print("what is life")

# Exercise: There's a theory in mathematics called "Fermat's Last Theorem" (some fun history about the name)
# Basically, it goes like this (^ means exponent): There are no positive integers a, b, and c such that a^n + b^n = c^n
# for any values of n greater than 2. For example, 2^3 + 3^3 != 2^3

# Your task, is to write a program that takes in a,b,c and n as arguments and check if a^n+b^n=c^n.

print(3**2 == 9) # True, ** is how you do exponents in python

def check_fermat(a, b, c, n):
    pass # Your code goes here
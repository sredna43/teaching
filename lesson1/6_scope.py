# So, you've seen variables and you've seen functions. How do the two work together? When can you use them? Let's take a closer look.

# One of the most important concepts to understand when it comes to writing programs is scope. Rather than explain through words, let's
# look at a concrete example of how scope can affect our programming.

variable = 10

def func(x):
    print(x + variable)

func(5)

# The thing to notice here is that even though variable is declared outside of the function, it can still be used inside the function.
# This is because variable has been created in the "global" scope with respect to this file/program whichever way you'd like to think of it.

# However, this does not go both ways. There is a hierarchy of scopes in python and in all languages.

def func2():
    x = 10
    print(x)

# This print statement will not work, can you figure out why?
# print(x)

func2()


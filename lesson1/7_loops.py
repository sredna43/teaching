# What if you want python to do something 50 times but you're too lazy to type out 50 lines of code? Loops are your answer. Observe.

for i in range(50):
    print(i)

# (prints 0-49)

# Here we used the range() function to specify where we want to start our loop and end our loop.
# That's basically all I wanted to show you with loops for now. Just know that by default the range(n) function by default goes from 0 to n-1

# Quick intro to lists

my_list = []

for i in range(1,51):
    my_list.append(i)

print(my_list)

# Now you know the basics of lists ;)

for i in range(51, 1, -1):
    print(i)

# What's going on here???
# The range function can take up to three variables. They are (in order) start, stop, and step. Where to start, where to stop, how to step.

# Write a loop that prints the odd numbers from 1-51 inclusive.
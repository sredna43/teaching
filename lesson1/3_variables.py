# Hello and welcome to an introduction to variables! What is a variable? It's something that's value is... variable.

# Here's an example!

name = "Deidree"
print(name)

# What do you think the output will be? Check it!

# In the previous example, the variable "name" is assigned to a "string", which is just a fancy name for a list of characters.

# In this example, the variable "number" is assigned to an "integer", which you should remember from math class ;)
number = 10
print(number * number)

# What if we weren't sure about what type a variable is? We can always ask the interpreter
print(type(name))
print(type(number))

# The type() function let's us check the type of an "object". An object can be many things, in this case it's a variable!

# Here's a challenge for you:
# What will be the output of the following line of code? Uncomment it and run the file to find out :)

# print(number/4)

# Python allows you to perform what's called "type casting". This is what that looks like:

type_cast = int(10/3)

# Take a guess as to what the next line of code does, then uncomment it and run the program!

# print(type_cast)

# Were you right? Were you wrong? Why?


# You may have noticed that the variable names I used here all start with a letter, and don't contain fancy symbols.
# Here are some variable names that are very much illegal in python, can you guess why?

# @nders = 'awesome'
# 23pandas = 'sitting in a tree'
# what% = 75.3
# my-variable = 10
# lambda = 10

# Ok... the first three make sense. No special characters allowed, nor can a variable start with a number. But what about the last two?
# my-variable doesn't work because the hyphen ( - ) is treated as a minus sign.
# lambda is a keyword in python. Python has many keywords, here's the list! (No, I don't have this list memorized.)

'''
False	await	else	import	pass
None	break	except	in	raise
True	class	finally	is	return
and	continue	for	lambda	try
as	def	from	nonlocal	while
assert	del	global	not	with
async	elif	if	or	yield
'''

# Here are some variable names that DO work:

lambda2 = 6
anders_rules = True
DeidreeDrools = True
s3xy4u = 'yees'


# Here's a fun challenge for you! This code, doesn't work... can you fix it?

# 1x = 1
# 2x = 2
# print(1x + 2x) # Should print 3
# print(1x2x) # Should print 2
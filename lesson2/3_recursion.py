# Now, we're getting into some real hardcore programming. Recursion!!! Recursion is awesome.

# Basically, recursion means that a function is used to call itself... Let's make sure we talk about this.

# Here's an example, try to see if you can figure out what's going on here!

def f(x):
    print(x)
    if x == 0:
        return
    f(x-1) # This step is the recursion

print(f(5))

# Note the if statement with the empty return at the end. An empty return is a way to stop a function from running.
# If we didn't have that here, this program would never be able to end! (This generally results in an error of some sort).

# Recursive functions need to have what's called a 'base case'. This is simply the case where the function no longer recurses (x == 0 in our example).

# Challenge 1: create a function that takes an integer n as an argument and recursively prints out the first n digits of the fibonacci sequence.

# hint: The Fibonacci sequence is formally defined by F(n) = F(n-1) + F(n-2), F(0) = 1, F(1) = 1

def fib(n):
    pass

x = fib(8) # 1, 1, 2, 3, 5, 8, 13, 21
print(x)


# Challenge 2: create a function that takes in an integer n as an argument and returns n factorial.
# hint: Factorial numbers are defined as such: n! = n * (n-1) * (n-2) * ... * 1

def factorial(n):
    pass

x = factorial(9) # 362880
print(x)



# bonus: fix your function so that the following call won't break anything.
print(factorial(4.5))
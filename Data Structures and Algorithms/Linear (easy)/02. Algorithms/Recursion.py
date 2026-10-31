# recursion -> A function calling itself... again it is not an algorithm

def eat(count):
    # base case -> when to stop
    if count == 0:
        print("Hand is empty")
        return
    print(f"I have {count} mangoes... eating one")
    
    # recursion call -> what will i call
    eat(count-1)

eat(4)


# factorial -> time = n and space = n

def factorial(n):
    if(n <= 1): return 1

    return n * factorial(n-1)

print(factorial(5))


# fibonacci -> time = 2^n  and space = n (stack)

def fibonacci(n):    
    if(n <= 1):
        return n

    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(5))
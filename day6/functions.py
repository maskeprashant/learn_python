def greet(name):
    return f"Hello, {name}!"

def add(a,b):
    return a+b


def factorial(n):
    if n == 0 or n ==1:
        return 1
    else:
        return n * factorial(n-1)
    

def is_even(num):
    return num % 2 == 0

print(greet("Alice"))
print("Addition of 5 and 3 is:", add(5,3))
print("Factorial of 5 is:", factorial(5))
print("Is 4 even?", is_even(4))
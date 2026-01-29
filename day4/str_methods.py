# String methods in Python
# conctnation

greeting = "Hello"
name = "Alice"

message = greeting + " " + name + "!"
print(message)  # Output: Hello Alice!

# upper() and lower() methods
print(greeting.upper())  # Output: HELLO
print(name.lower())      # Output: alice

# slicing
message = "Hello, world!"
        #  01234567890123

print(message[0:5])  # Output: Hello
print(message[7:12]) # Output: world

# find method

index = message.find("world")
print(f"'world' found at index: {index}")  # Output: 'world'

str = "this is wonderful world"
print(str.find("wonderful"))

for i in str:
    print(i)

str_ar = str.split(" ")
for st in str_ar:
    print(st)

    fruit = "abcdefghijklmnioprstuvwxyz"

    print(fruit[:10])
    print(fruit[10:])
    print(fruit[::-1])
    fruit="banana"
    print(fruit)
    fruit = fruit[0].upper() + fruit[1:]
    print(fruit)
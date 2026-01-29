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

    # stratswith and endswith

name="Prashant"
print(name.startswith('P'))
print(name.endswith('ant'))

cap_name = name.upper();
print(cap_name)
print(cap_name[0]+cap_name[1:].lower())

count = "I have 4 apples and 5 bananas"
count = count.replace("apple","mangoe")
count = count.replace("4","5")
print(count)

name = input("Enter your name: ")
name = name.replace("a","4")
name = name.replace("b","8")
name = name.replace("e","3")
name = name.replace("i","1")
name = name.replace("o","0")
name = name.replace("s","5")
name = name.replace("t","7")

print(name)
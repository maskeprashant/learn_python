def sum(a,b):
    return a+b

def sum2(list_of_numbers):
    total = 0
    for num in list_of_numbers:
        total += num
    return total

print("Sum of 3 and 5 is:", sum(3,5))
print("Sum of [1,2,3,4,5] is:", sum2([1,2,3,4,5]))

def sum3(*args):
    total = 0
    for num in args:
        total += num
    return total
print("Sum of 1,2,3,4,5,6,8.5,-3,9 is:", sum3(1,2,3,4,5,6,8.5,-3,9))

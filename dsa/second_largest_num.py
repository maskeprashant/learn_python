
def calculate_second_largest(numbers):
    if len(numbers) < 2:
        return "List must contain at least two distinct numbers"
    
    first=second=float('-inf')
    for el in numbers:
        if el > first:
            second = first
            first = el 
        elif first < el < second:
            second = el
        
    if second == float('-inf'):
        return "all values must not same"
    
    print(second)

calculate_second_largest([3,4,5,9,2])

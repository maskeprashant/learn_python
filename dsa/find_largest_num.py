
def find_largeset_num(list):
    largest_num=0

    for el in list:
        if el > largest_num:
            largest_num = el
    
    return largest_num

result = find_largeset_num([1,2,4,2,1,6,5,9,5])
print(result)

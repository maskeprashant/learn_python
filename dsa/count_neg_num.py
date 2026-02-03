
def count_neg_num(arr):
    for el in arr:
        if el < 0:
            return "Found negative number in given list"
            break
    return "No Negative number"

result = count_neg_num([1,2,-3,4,5,6])
print(result)

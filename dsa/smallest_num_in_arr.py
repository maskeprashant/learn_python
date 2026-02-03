
def find_smallest_num_in_list(arr):
    smallest_num = arr[0]
    for el in arr:
        if el < smallest_num:
            smallest_num = el
            
    return smallest_num

result = find_smallest_num_in_list([11,12,3,4,5,6,11])
print(result)
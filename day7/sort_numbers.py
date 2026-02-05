def soft_numbers(num_list):
    return sorted(num_list, reverse=True)

result = soft_numbers([5,3,8,6,2,7,4,1])
print(result)

#  manual sorting

def manually_sort_list(num_list):
    l = len(num_list)

    for i in range(0,l):
        for j in range(0, l-i-1):
            if(num_list[j] > num_list[j+1]):
                num_list[j], num_list[j+1] = num_list[j+1], num_list[j]
    print(num_list)

manually_sort_list([12,4,6,3,8,11])

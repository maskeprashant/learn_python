
def reverse_int(num):
    print(f"Given number is : {num}")
    revrsed_num=0

    while(num > 0):
        temp = num % 10
        revrsed_num = revrsed_num * 10 + temp
        num = num //10
        if(num ==0):
            break

    print(f"Reversed number: {revrsed_num}")

reverse_int(123)


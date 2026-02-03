
def check_palindrome_number(num):
    num_str = str(num)
    str_len = len(num_str)

    for el in range(str_len):
        print(num_str[el], num_str[str_len - el -1])
        if(num_str[el] != num_str[str_len - el -1]):
            return "not palindrome number"
            break

    return "palindrome number"

print(check_palindrome_number(12212))
    
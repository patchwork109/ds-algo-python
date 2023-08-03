num = -43895
num2 = 67

def integer_to_string(num):
    if num == 0:
        return "0"

    is_negative = False
    if num < 0:
        is_negative = True
        num = abs(num)

    # List to map digits to their character representations
    digit_to_char = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    str_of_ints = []
    while num > 0:
        digit = num % 10
        str_of_ints.append(digit_to_char[digit])
        num //= 10

    if is_negative:
        str_of_ints.append("-")

    concatenated_result = ''.join(str_of_ints)
    result = concatenated_result[::-1]

    return result

print(integer_to_string(num))
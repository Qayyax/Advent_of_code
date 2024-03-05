def string_to_num(txt):
    nums = {
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }
    # Convert key in txt to value of nums
    # and append it to txt in it's occurence
    for word, num in nums.items():
        txt = txt.replace(word, word + str(num) + word)
    return txt


def two_num(txt):
    digits = []
    text = string_to_num(txt)
    # Getting decimal value
    for char in text:
        if char.isdecimal():
            digits.append(char)
    if len(digits) == 0:
        return 0
    elif len(digits) > 1:
        return digits[0] + digits[-1]
    else:
        return digits[0] + digits[0]


# Testing the function on the file.txt
with open('file.txt', 'r') as file:
    count = []
    for line in file:
        num = two_num(line)
        count.append(int(num))
    print(sum(count))

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
    for word, num in nums.items():
        txt = txt.replace(word, word + str(num) + word)
    return txt


def two_num(txt):
    digits = []
    text = string_to_num(txt)
    for char in text:
        if char.isdecimal():
            digits.append(char)
    if len(digits) == 0:
        return 0
    elif len(digits) > 1:
        return digits[0] + digits[-1]
    else:
        return digits[0] + digits[0]


with open('file.txt', 'r') as file:
    count = []
    for line in file:
        num = two_num(line)
        count.append(int(num))
    print(sum(count))

# 29, 83, 13, 24, 42, 14, and 76
# print(two_num("treb7uchet"))
# """
# two1nine
# eightwothree
# abcone2threexyz
# xtwone3four
# 4nineeightseven2
# zoneight234
# 7pqrstsixteen
# """
#
# print(two_num("two1nine"))
# print(two_num("eightwothree"))
# print(two_num("abcone2threexyz"))
# print(two_num("xtwone3four"))
# print(two_num("4nineeightseven2"))
# print(two_num("zoneight234"))
# print(two_num("7pqrstsixteen"))
# # #
# print(string_to_num("two1nine"))
# print(string_to_num("eightwothree"))
# print(string_to_num("abcone2threexyz"))
# print(string_to_num("xtwone3four"))
# print(string_to_num("4nineeightseven2"))
# print(string_to_num("zoneight234"))
# print(string_to_num("7pqrstsixteen"))

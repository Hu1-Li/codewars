# coding=utf-8
def parse_int(string: str):
    # clean
    s = string.replace(" and ", " ").replace("-", " ")
    # word to number mapping
    mapping = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "ten": 10,
        "eleven": 11,
        "twelve": 12,
        "thirteen": 13,
        "fourteen": 14,
        "fifteen": 15,
        "sixteen": 16,
        "seventeen": 17,
        "eighteen": 18,
        "nineteen": 19,
        "twenty": 20,
        "thirty": 30,
        "forty": 40,
        "fifty": 50,
        "sixty": 60,
        "seventy": 70,
        "eighty": 80,
        "ninety": 90,
        "hundred": 100,
        "thousand": 1000,
    }
    words = s.split()
    numbers = [mapping.get(word) for word in words]
    total = 0
    tmp = 0
    for number in numbers:
        if number == 100 or number == 1000:
            if total > number:
                total += tmp * number
            else:
                total = (total + tmp) * number
            tmp = 0
        else:
            tmp += number
    if tmp > 0:
        total += tmp
    return total

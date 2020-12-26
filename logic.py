import random
from pprint import pprint

max_card_nums = 15
card = [
    [],
    [],
    []
]


def generate_card_strings():
    card = []
    for string in range(1, 4):
        a = 1
        b = 10
        line = []
        for item in range(1, 10):
            number = random.randint(a, b)
            line.append(number)
            a += 10
            b += 10
        i = 4
        while i > 0:
            x = random.randint(0, 8)
            if line[x] == None:
                if x == 8:
                    j = 1
                    while not line[int(x)-j]:
                        line[int(x)-j] = None
                        j+=1
                else:
                    line[int(x)+1] = None
            else:
                line[x] = None
            i -= 1
        card.append(line)
    return card


def validate_card():
    card = generate_card_strings()
    # common = set(card[0]) & set(card[1]) & set(card[2])
    common1 = set(card[0]) & set(card[1])
    common2 = set(card[1]) & set(card[2])
    common3 = set(card[0]) & set(card[2])
    # print(common1)
    # print(common2)
    # print(common3)
    set1 = common1 == common2
    set2 = common2 == common3
    set3 = common1 == common3

    if set1 and set2 and set3:
        return card
    else:
        return validate_card()

pprint(validate_card())

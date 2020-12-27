import random
from pprint import pprint

max_card_nums = 15

def generate_card():
    '''
    Creating card. Line by line.
    :return:
    '''
    card = []
    for string in range(1, 4):
        a = 1
        b = 10
        line = []
        for item in range(1, 10):
            # generating numbers in card line
            number = random.randint(a, b)
            line.append(number)
            a += 10
            b += 10
        i = 4
        while i > 0:
            x = random.randint(0, 8)
            # genegating random None and checking its indexes,
            if line[x] == 0:
                if x == 8:
                    j = 1
                    while not line[int(x)-j]:
                        line[int(x)-j] = 0
                        j+=1
                else:
                    line[int(x)+1] = 0
            else:
                line[x] = 0
            i -= 1
        # check if zeros less than 4 ==> replace max to 0
        if line.count(0) < 4:
            line[line.index(max(line))] = 0
        card.append(line)
    return card


def validate_card():
    '''
    Validating that card has no same numbers in rows
    :return: validated card
    '''
    plain_card = []
    card = generate_card()
    common1 = set(card[0]) & set(card[1])
    common2 = set(card[1]) & set(card[2])
    common3 = set(card[0]) & set(card[2])
    set1 = common1 == common2
    set2 = common2 == common3
    set3 = common1 == common3

    if set1 and set2 and set3:
        # make card a one line list to further easy poping
        plain_card.extend(card[0])
        plain_card.extend(card[1])
        plain_card.extend(card[2])
        # deleting zeros
        for item in sorted(plain_card):
            if item == 0:
                plain_card.remove(item)
        # return sorted(plain_card)
        return card
    else:
        return validate_card()

pprint(validate_card())

class Player:
    pass
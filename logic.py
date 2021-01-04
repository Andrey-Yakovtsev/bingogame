import random
import time


class Player:

    def generate_card(self):
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

    def validate_card(self):
        '''
        Validating that card has no same numbers in rows
        :return: validated card
        '''
        card = self.generate_card()
        common1 = set(card[0]) & set(card[1])
        common2 = set(card[1]) & set(card[2])
        common3 = set(card[0]) & set(card[2])
        set1 = common1 == common2
        set2 = common2 == common3
        set3 = common1 == common3

        if set1 and set2 and set3:
            return card     # card 9x3
        else:
            return self.validate_card()

def plainify_card(card):
    '''
    Deleting sub-levels and zeros from card.
    :return: single leveled list without zeros
    '''
    plain_card = []
    # make card a one line list to further easy poping
    plain_card.extend(card[0][0])
    plain_card.extend(card[0][1])
    plain_card.extend(card[0][2])
    # deleting zeros
    for item in sorted(plain_card):
        if item == 0:
            plain_card.remove(item)
    return sorted(plain_card)   # plain card

def get_user_answer():
    answer = str(input(f'У вас есть показанное число? Ответы: Y / N  '))
    time.sleep(3)
    if not answer:
        return False
    elif answer == 'Y' or 'y':
        return True
    else:
        return False

def get_number_from_bag():
    numbers_bag = list(range(1, 91))
    while len(numbers_bag) > 0:
        number = numbers_bag.pop(random.randint(0, (len(numbers_bag)-1)))
        yield number






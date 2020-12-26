import random

max_card_nums = 15
card = [
    [],
    [],
    []
]
for string in range(1, 4):
    def generate_card_string():
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
        return line
    print(generate_card_string())
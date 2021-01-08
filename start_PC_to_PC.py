import time
from pprint import pprint
import threading

from logic import Player, get_number_from_bag, plainify_card, get_user_answer, pc_players_threads, human_players_threads

human_players_count = 1     # int(input('Введите количество людей: '))
pc_players_count = 1    # int(input('Введите количество компьютерных соперников: '))

humans_cards = []
for i in range(1, (human_players_count + 1)):
    human_player = Player()
    humans_cards.append(human_player.validate_card())


pprint("Ваша Карточка")
pprint(humans_cards)
plain_human_card = plainify_card(humans_cards)

pc_cards = []
for i in range(1, (pc_players_count + 1)):
    pc_player = Player()
    pc_cards.append(pc_player.validate_card())

pprint("Карточка компьютера")
pprint(pc_cards)
plain_pc_card = plainify_card(pc_cards)


for item in get_number_from_bag():
    print(f'ВЫПАЛО ЧИСЛО ==> {item}')
    time.sleep(0.3)
    try:
        plain_human_card.remove(item)
    except:
        ValueError
    try:
        plain_pc_card.remove(item)
    except:
        ValueError
    if len(plain_human_card) == 0:
        print('Люди победили')
        break
    elif len(plain_pc_card) == 0:
        print('Машины победили')
        break
    print("Осталось чисел на карточке ЧЕЛОВЕКА  ==>", len(plain_human_card))
    print("Осталось чисел на карточке PC ==>", len(plain_pc_card))



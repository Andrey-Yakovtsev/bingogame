import time
from pprint import pprint

from logic import Player, get_number_from_bag, plainify_card, get_user_answer


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
    # answer = str(input(f'У вас есть число {item}? Ответы: Y / N  '))
    # time.sleep(0.3)
    # if answer == 'Y' or 'y':
    # print(get_user_answer())
    try:
        plain_human_card.remove(item)
    except:
        ValueError
    # else:
    #     continue
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
    print("Human ==>", len(plain_human_card))
    print("PC ==>", len(plain_pc_card))
'''
 Достаем число
 Проверяем есть ли оно в карточках игроков. Как тут задействовать человека?
 - выводим карточку игроков поочередно и если это человек - даем 3 секунды на да/нет
 Если есть, то попаем из списка.
 Проверяем длину списка.
 Если список пустой, игрок выиграл. Конец игры

 Создать:
 Экземпляр игрока
 У него экземпляр карточки
 У карточки д.б. метод ПОП - для проверки и удаления числа
 Если карточка пустая - игрок выиграл
print(item)
'''

'''
if item in card:
    card.pop(item)
else:
    continue
if len(card) == 0:
    print(f'Игрок {player} победил!')
'''

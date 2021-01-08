import time
from pprint import pprint
import threading

from logic import Player, get_number_from_bag, plainify_card, get_user_answer, pc_players_threads, human_players_threads



if __name__ == "__main__":
    human_players_count = 2     # int(input('Введите количество людей: '))
    pc_players_count = 5    # int(input('Введите количество компьютерных соперников: '))

    pc_players_threads(pc_players_count)
    human_players_threads(human_players_count)
    print(threading.active_count())
    print(threading.main_thread())


    for item in get_number_from_bag():
        print(f'ВЫПАЛО ЧИСЛО ==> {item}')
        time.sleep(0.3)
        """
        Присоседиться к потокам как???
        """
        # try:
        #     plain_human_card.remove(item)
        # except:
        #     ValueError
        # try:
        #     plain_pc_card.remove(item)
        # except:
        #     ValueError
        # if len(plain_human_card) == 0:
        #     print('Люди победили')
        #     break
        # elif len(plain_pc_card) == 0:
        #     print('Машины победили')
        #     break
        # print("Осталось чисел на карточке ЧЕЛОВЕКА  ==>", len(plain_human_card))
        # print("Осталось чисел на карточке PC ==>", len(plain_pc_card))


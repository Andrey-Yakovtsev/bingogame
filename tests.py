from logic import plainify_card, get_number_from_bag, Player
from unittest import TestCase

class BingoTests(TestCase):
    # проверяем, что в карточка == список. В ней 15 номеров, 3 ряда, по 5 номеров больше нуля в каждом
    @classmethod
    def setUpClass(cls):
        cls.player = Player()
        cls.card = cls.player.generate_card()
        cls.valid_card = cls.player.validate_card()

    def test_card_in_not_empty(self):
        self.assertIsNotNone(self.card)

    def test_card_is_list_type(self):
        self.assertIsInstance(self.card, list,)

    def test_card_has_3_lines(self):
        self.assertEqual(len(self.card), 3)

    def test_card_line_is_9_len(self):
        for i in range(3):
            self.assertEqual(len(self.card[i]), 9)

    def test_card_has_4_zeroes(self):
        for i in range(3):
            self.assertEqual(self.valid_card[i].count(0), 4)

    def test_card_is_plain(self):
        for i in self.valid_card:
            self.assertIsNot(i, 0)

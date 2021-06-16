import unittest

from dec_patt_solution import *

hero = Hero()

class TestHero(unittest.TestCase):
    def test_hero_get_stats(self):
        cases = [{'HP': 128,
                'MP': 42, 'SP': 100, 'Strength': 15,
                'Perception': 4, 'Endurance': 8,
                'Charisma': 2, 'Intelligence': 3,
                'Agility': 8, 'Luck': 1}
                ]

        for case in cases:
            for k, v in case.items():
                with self.subTest(x=v):
                    self.assertEqual(hero.get_stats()[k], v)

    def test_hero_stats(self):
        cases = [{'HP': 128,
                'MP': 42, 'SP': 100, 'Strength': 15,
                'Perception': 4, 'Endurance': 8,
                'Charisma': 2, 'Intelligence': 3,
                'Agility': 8, 'Luck': 1}
                ]

        for case in cases:
            for k, v in case.items():
                with self.subTest(x=v):
                    self.assertEqual(hero.stats[k], v)

    def test_hero_get_neg(self):
        case = []
        with self.subTest(x=case):
            self.assertEqual(hero.get_negative_effects(), case)

    def test_hero_get_pos(self):
        case = []
        with self.subTest(x=case):
            self.assertEqual(hero.get_positive_effects(), case)

class TestBerserk(unittest.TestCase):
    brs1 = Berserk(hero)
    brs2 = Berserk(brs1)

    def test_berserk_get_stats(self):
        cases = [
                {'HP': 178,
                'MP': 42, 'SP': 100, 'Strength': 22,
                'Perception': 1, 'Endurance': 15,
                'Charisma': -1, 'Intelligence': 0,
                'Agility': 15, 'Luck': 8},
                {'HP': 228,
                'MP': 42, 'SP': 100, 'Strength': 29,
                'Perception': -2, 'Endurance': 22,
                'Charisma': -4, 'Intelligence': -3,
                'Agility': 22, 'Luck': 15}
                ]
        for case in cases:
            for k, v in case.items():
                with self.subTest(x=v):
                    if case == cases[0]:
                        self.assertEqual(brs1.stats[k], v)
                    elif case == cases[1]:
                        self.assertEqual(brs2.stats[k], v)

    def test_berserk_neg_effects(self):
        case = []
        with self.subTest(x=case):
            self.assertEqual(brs1.get_negative_effects(), case)
            self.assertEqual(brs2.get_negative_effects(), case)

    def test_berserk_pos_effects(self):
        cases = [['Berserk'], ['Berserk', 'Berserk']]
        for case in cases:
            with self.subTest(x=case):
                if case == cases[0]:
                    self.assertEqual(brs1.get_positive_effects(), case)
                elif case == cases[1]:
                    self.assertEqual(brs2.get_positive_effects(), case)

class TestCurse(unittest.TestCase):
    brs1 = Berserk(hero)
    brs2 = Berserk(brs1)
    cur1 = Curse(brs2)

    def test_curse_get_stats(self):
        cases = [
                {'HP': 228,
                'MP': 42, 'SP': 100, 'Strength': 27,
                'Perception': -4, 'Endurance': 20,
                'Charisma': -6, 'Intelligence': -5,
                'Agility': 20, 'Luck': 13}
                ]
        for case in cases:
            for k, v in case.items():
                with self.subTest(x=v):
                    self.assertEqual(cur1.get_stats()[k], v)

    def test_curse_neg_effects(self):
        case = ['Curse']
        with self.subTest(x=case):
            self.assertEqual(cur1.get_negative_effects(), case)

    def test_curse_pos_effects(self):
        case = ['Berserk', 'Berserk']
        with self.subTest(x=case):
            self.assertEqual(cur1.get_positive_effects(), case)

    def test_decrease_berserk_effect(self):
        cur1.base = brs1
        cases = [{'HP': 178,
                'MP': 42, 'SP': 100,
                'Strength': 20, 'Perception': -1,
                'Endurance': 13, 'Charisma': -3,
                'Intelligence': -2, 'Agility': 13,
                'Luck': 6},
                ['Berserk'],
                ['Curse']
                ]
        for case in cases:
            with self.subTest(x=case):
                if case == cases[0]:
                    for k, v in case.items():
                        self.assertEqual(cur1.get_stats()[k], v)
                elif case == cases[1]:
                    self.assertEqual(cur1.get_positive_effects(), case)
                elif case == cases[2]:
                    elf.assertEqual(cur1.get_negative_effects(), case)




unittest.main()

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

hero = Hero()
brs1 = Berserk(hero)
brs2 = Berserk(brs1)

class TestBerserk(unittest.TestCase):
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
                        self.assertEqual(brs1.get_stats()[k], v)
                    elif case == cases[1]:
                        self.assertEqual(brs2.get_stats()[k], v)

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

brs1 = Berserk(hero)
bless1 = Blessing(hero)
bless2 = Blessing(brs1)

class TestBlessing(unittest.TestCase):
    def test_bless_get_stats(self):
        cases = [{'HP': 128,
                'MP': 42, 'SP': 100, 'Strength': 17,
                'Perception': 6, 'Endurance': 10,
                'Charisma': 4, 'Intelligence': 5,
                'Agility': 10, 'Luck': 3},
                {'HP': 178,
                'MP': 42, 'SP': 100, 'Strength': 24,
                'Perception': 3, 'Endurance': 17,
                'Charisma': 1, 'Intelligence': 2,
                'Agility': 17, 'Luck': 10}
                ]
        for case in cases:
            for k, v in case.items():
                with self.subTest(x=v):
                    if case == cases[0]:
                        self.assertEqual(bless1.get_stats()[k], v)
                    elif case == cases[1]:
                        self.assertEqual(bless2.get_stats()[k], v)

    def test_bless_get_pos(self):
        case = ['Berserk', 'Blessing']
        with self.subTest(x=case):
            self.assertEqual(*bless1.get_positive_effects(), case[1])
            self.assertEqual(bless2.get_positive_effects(), case)

    def test_bless_neg_effects(self):
        case = []
        with self.subTest(x=case):
            self.assertEqual(bless1.get_negative_effects(), case)
            self.assertEqual(bless2.get_negative_effects(), case)


brscurse1 = Berserk(hero)
brscurse2 = Berserk(brscurse1)
cur1 = Curse(brscurse2)
cur2 = Curse(brscurse2)
cur2.base = brscurse1

class TestCurse(unittest.TestCase):
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
                        self.assertEqual(cur2.get_stats()[k], v)
                elif case == cases[1]:
                    self.assertEqual(cur2.get_positive_effects(), case)
                elif case == cases[2]:
                    self.assertEqual(cur2.get_negative_effects(), case)
#
#
weak1 = Weakness(hero)
brsweak1 = Berserk(hero)
curweak1 = Curse(brsweak1)
weak2 = Weakness(brsweak1)
weak3 = Weakness(curweak1)


class TestWeakness(unittest.TestCase):
    def test_weakness_get_stats(self):
        cases = [{'HP': 128,
                'MP': 42, 'SP': 100, 'Strength': 11,
                'Perception': 4, 'Endurance': 4,
                'Charisma': 2, 'Intelligence': 3,
                'Agility': 4, 'Luck': 1},
                {'HP': 178,
                'MP': 42, 'SP': 100, 'Strength': 18,
                'Perception': 1, 'Endurance': 11,
                'Charisma': -1, 'Intelligence': 0,
                'Agility': 11, 'Luck': 8}
                ]
        for case in cases:
            for k, v in case.items():
                with self.subTest(x=v):
                    if case == cases[0]:
                        self.assertEqual(weak1.get_stats()[k], v)
                    elif case == cases[1]:
                        self.assertEqual(weak2.get_stats()[k], v)

    def test_curse_neg_effects(self):
        case = ['Weakness', ['Curse', 'Weakness']]
        with self.subTest(x=case):
            self.assertEqual(*weak1.get_negative_effects(), case[0])
            self.assertEqual(*weak2.get_negative_effects(), case[0])
            self.assertEqual(weak3.get_negative_effects(), case[1])

    def test_curse_pos_effects(self):
        case = [[],['Berserk']]
        with self.subTest(x=case):
            self.assertEqual(weak1.get_positive_effects(), case[0])
            self.assertEqual(weak2.get_positive_effects(), case[1])


evil1 = EvilEye(hero)
curevil1 = Curse(evil1)


class TestEvilEye(unittest.TestCase):


    def test_evileye_get_stats(self):
        cases = [{'HP': 128,
                'MP': 42, 'SP': 100, 'Strength': 15,
                'Perception': 4, 'Endurance': 8,
                'Charisma': 2, 'Intelligence': 3,
                'Agility': 8, 'Luck': -9}
                ]
        for k, v in cases[0].items():
            with self.subTest(x=v):
                self.assertEqual(evil1.get_stats()[k], v)

    def test_evil_neg_effects(self):
        case = [['EvilEye'], ['EvilEye', 'Curse']]
        with self.subTest(x=case):
            self.assertEqual(evil1.get_negative_effects(), case[0])
            self.assertEqual(curevil1.get_negative_effects(), case[1])

unittest.main()

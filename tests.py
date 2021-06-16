import unittest

from dec_patt_solution import *

hero = Hero()

class TestHero(unittest.TestCase):
    def test_hero_get_stats(self):
        cases = [{'HP': 128, 'MP': 42, 'SP': 100, 'Strength': 15, 'Perception': 4, 'Endurance': 8, 'Charisma': 2, 'Intelligence': 3, 'Agility': 8, 'Luck': 1}]

        for case in cases:
            for k, v in case.items():
                with self.subTest(x=v):
                    self.assertEqual(hero.get_stats()[k], v)

    def test_hero_stats(self):
        cases = [{'HP': 128, 'MP': 42, 'SP': 100, 'Strength': 15, 'Perception': 4, 'Endurance': 8, 'Charisma': 2, 'Intelligence': 3, 'Agility': 8, 'Luck': 1}]

        for case in cases:
            for k, v in case.items():
                with self.subTest(x=v):
                    self.assertEqual(hero.stats[k], v)

    def test_hero_get_neg(self):
        case = []
        with self.subTest(x=case):
            self.assertEqual(hero.get_negative_effects(), case)

# class TestBerserk(unittest.TestCase):


unittest.main()

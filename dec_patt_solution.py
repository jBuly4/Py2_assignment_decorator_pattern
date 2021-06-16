from abc import ABC, abstractmethod

# class Hero:
#     def __init__(self):
#         self.positive_effects = []
#         self.negative_effects = []
#         self.stats = {
#             "HP": 128,  # health points
#             "MP": 42,  # magic points,
#             "SP": 100,  # skill points
#             "Strength": 15,  # сила
#             "Perception": 4,  # восприятие
#             "Endurance": 8,  # выносливость
#             "Charisma": 2,  # харизма
#             "Intelligence": 3,  # интеллект
#             "Agility": 8,  # ловкость
#             "Luck": 1  # удача
#         }
#
#     def get_positive_effects(self):
#         return self.positive_effects.copy()
#
#     def get_negative_effects(self):
#         return self.negative_effects.copy()
#
#     def get_stats(self):
#         return self.stats.copy()


class AbstractEffect(ABC, Hero):
    @abstractmethod
    def get_stats(self):
        pass


class AbstractPositive(AbstractEffect):
    def __init__(self, base):
        self.base = base

    @abstractmethod
    def get_positive_effects(self):
        pass

    def get_negative_effects(self):
        return self.base.get_negative_effects().copy()


class AbstractNegative(AbstractEffect):
    def __init__(self, base):
        self.base = base

    @abstractmethod
    def get_negative_effects(self):
        pass

    def get_positive_effects(self):
        return self.base.get_positive_effects().copy()


class Berserk(AbstractPositive):
    def get_positive_effects(self):
        effects = self.base.get_positive_effects()
        effects.append("Berserk")
        return effects.copy()

    def get_stats(self):
        effect = {"HP": 50,
                "Strength": 7,
                "Endurance": 7,
                "Agility": 7,
                "Luck": 7,
                "Perception": -3,
                "Charisma": -3,
                "Intelligence": -3}
        new_stats = self.base.get_stats()
        for key in effect:
            new_stats[key] += effect[key]
        return new_stats.copy()

class Blessing(AbstractPositive):
    def get_positive_effects(self):
        effects = self.base.get_positive_effects()
        effects.append("Blessing")
        return effects.copy()

    def get_stats(self):
        effect = {"Strength": 2,  # сила
        "Perception": 2,  # восприятие
        "Endurance": 2,  # выносливость
        "Charisma": 2,  # харизма
        "Intelligence": 2,  # интеллект
        "Agility": 2,  # ловкость
        "Luck": 2}
        new_stats = self.base.get_stats()
        for key in effect:
            new_stats[key] += effect[key]
        return new_stats.copy()


class Weakness(AbstractNegative):
    def get_negative_effects(self):
        effects = self.base.get_negative_effects()
        effects.append("Weakness")
        return effects.copy()

    def get_stats(self):
        effect = {"Strength": -4,  # сила
                  "Endurance": -4,  # выносливость
                  "Agility": -4 # ловкость
                  }
        new_stats = self.base.get_stats()
        for key in effect:
            new_stats[key] += effect[key]
        return new_stats.copy()


class EvilEye(AbstractNegative):
    def get_negative_effects(self):
        effects = self.base.get_negative_effects()
        effects.append("EvilEye")
        return effects.copy()

    def get_stats(self):
        effect = {"Luck": -10}
        new_stats = self.base.get_stats()
        for key in effect:
            new_stats[key] += effect[key]
        return new_stats.copy()


class Curse(AbstractNegative):
    def get_negative_effects(self):
        effects = self.base.get_negative_effects()
        effects.append("Curse")
        return effects.copy()

    def get_stats(self):
        effect = {"Strength": 2,  # сила
        "Perception": 2,  # восприятие
        "Endurance": 2,  # выносливость
        "Charisma": 2,  # харизма
        "Intelligence": 2,  # интеллект
        "Agility": 2,  # ловкость
        "Luck": 2}
        new_stats = self.base.get_stats()
        for key in effect:
            new_stats[key] -= effect[key]
        return new_stats.copy()

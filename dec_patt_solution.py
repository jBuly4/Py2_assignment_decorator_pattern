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


''' solution

# Объявим абстрактный декоратор
class AbstractEffect(Hero, ABC):

    def __init__(self, base):
        self.base = base

    @abstractmethod
    def get_positive_effects(self):
        return self.positive_effects

    @abstractmethod
    def get_negative_effects(self):
        return self.negative_effects

    @abstractmethod
    def get_stats(self):
        pass


# В AbstractPositive будем возвращать список наложенных отрицательных эффектов без изменений, чтобы не определять данный метод во всех положительных эффектах
class AbstractPositive(AbstractEffect):

    def get_negative_effects(self):
        return self.base.get_negative_effects()


# Объявим несколько положительных эффектов
class Berserk(AbstractPositive):

    def get_stats(self):
        # Получим характеристики базового объекта, модифицируем их и вернем
        stats = self.base.get_stats()
        stats["HP"] += 50
        stats["Strength"] += 7
        stats["Endurance"] += 7
        stats["Agility"] += 7
        stats["Luck"] += 7
        stats["Perception"] -= 3
        stats["Charisma"] -= 3
        stats["Intelligence"] -= 3
        return stats

    def get_positive_effects(self):
        # Модифицируем список эффектов, добавив в него новый эффект
        return self.base.get_positive_effects() + ["Berserk"]


class Blessing(AbstractPositive):

    def get_stats(self):
        stats = self.base.get_stats()
        stats["Strength"] += 2
        stats["Endurance"] += 2
        stats["Agility"] += 2
        stats["Luck"] += 2
        stats["Perception"] += 2
        stats["Charisma"] += 2
        stats["Intelligence"] += 2
        return stats

    def get_positive_effects(self):
        return self.base.get_positive_effects() + ["Blessing"]


# Для отрицательных эффектов неизменным останется список положительных эффектов
class AbstractNegative(AbstractEffect):

    def get_positive_effects(self):
        return self.base.get_positive_effects()


# Аналогично положительным эффектам, объявим отрицательные
class Weakness(AbstractNegative):

    def get_stats(self):
        stats = self.base.get_stats()
        stats["Strength"] -= 4
        stats["Endurance"] -= 4
        stats["Agility"] -= 4
        return stats

    def get_negative_effects(self):
        return self.base.get_negative_effects() + ["Weakness"]


class Curse(AbstractNegative):

    def get_stats(self):
        stats = self.base.get_stats()
        stats["Strength"] -= 2
        stats["Endurance"] -= 2
        stats["Agility"] -= 2
        stats["Luck"] -= 2
        stats["Perception"] -= 2
        stats["Charisma"] -= 2
        stats["Intelligence"] -= 2
        return stats

    def get_negative_effects(self):
        return self.base.get_negative_effects() + ["Curse"]


class EvilEye(AbstractNegative):

    def get_stats(self):
        stats = self.base.get_stats()
        stats["Luck"] -= 10
        return stats

    def get_negative_effects(self):
        return self.base.get_negative_effects() + ["EvilEye"]


'''

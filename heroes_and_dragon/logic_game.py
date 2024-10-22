import io
from random import choice
import sys

class Randomizer:
    @staticmethod
    def get_var():
        return choice([False, True])


class Attribute:
    def __init__(self, name, damage, hp):
        self.name = name
        self.damage = damage
        self.hp = hp

    def get_info(self):
        return f'Status:{self.name}|{self.hp}HP'

    def crit_attac(self):
        return int(self.damage * 1.3)

    def just_attac(self):
        return self.damage

    @staticmethod
    def value_block():
        return Randomizer.get_var()

    def initialized_fighter(self, target):
        buffer = io.StringIO()
        original_stdout = sys.stdout
        try:
            sys.stdout = buffer
            if Randomizer.get_var():
                target.hp -= self.crit_attac()
                print(f'{self.name} is attack {target.name}')
                print('Critical attack@!')
                print(f'{self.name} take {self.crit_attac()} damage to {target.name}')
                print(f'{target.get_info()}')
            else:
                if self.value_block():
                    print(f'{self.name} is attack {target.name}')
                    print('block attack')
                    print(f'{target.get_info()}')
                else:
                    target.hp -= self.just_attac()
                    print(f'{self.name} is attack {target.name}')
                    print(f'{self.name} take {self.just_attac()} damage to {target.name}')
                    print(f'{target.get_info()}')
        finally:
            sys.stdout = original_stdout
            return buffer.getvalue()
    def is_alive(self):
        return self.hp > 0

class Hero(Attribute):
    def __init__(self, name, damage, hp, lvl=1, max_hp=100):
        super().__init__(name, damage, hp, )
        self.lvl = lvl
        self.max_hp = max_hp

    def change_lvl(self, val=1):
        self.lvl += val
        self.hp = self.max_hp + 5
        self.max_hp = self.hp


class Monster(Attribute):
    def __init__(self, name, damage, hp):
        super().__init__(name, damage, hp)


tuple_monsters = (('monster_1', 10, 60),
                  ('monster_2', 15, 70),
                  ('monster_3', 17, 100))






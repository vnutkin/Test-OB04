from abc import ABC, abstractmethod
class Weapon(ABC):
    def __init__(self, weapon_typ):
        self.weapon_typ = weapon_typ
    @abstractmethod
    def attac(self,enemy):
        pass
class Monster():
    def __init__(self, name):
        self.name = name
        self.status = 'alive'
        print(f'Монстр {self.name} к бою готов')
    def killed(self):
        self.status = 'dead'
        print(f'Монстр {self.name} побежден!')
class Fighter():
    def __init__(self, name, weapon:Weapon):
        self.name = name
        self.status = 'alive'
        self.weapon = weapon
        print(f'Боец {self.name} c {self.weapon.weapon_typ} к бою готов')
    def change_weapon(self, weapon:Weapon):
        print(f'Боец {self.name} меняет {self.weapon.weapon_typ} на {weapon.weapon_typ}')
        self.weapon = weapon

    def killed(self):
        self.status = 'dead'
        print(f'Боец {self.name} побежден!')
    def attac(self, enemy):
        print(f'Боец {self.name} атакует {enemy.name}')
        self.weapon.attac(enemy)

class Sword(Weapon):
    def __init__(self,weapon_typ):
        super().__init__(weapon_typ)
    def attac(self, enemy):
        print(f'Атака мечом {self.weapon_typ} врага {enemy.name}')
        enemy.killed()
class Bow(Weapon):
    def __init__(self,weapon_typ):
        super().__init__(weapon_typ)
    def attac(self, enemy):
        print(f'Выстрел из лука {self.weapon_typ} во врага {enemy.name}')
        enemy.killed()
monster = Monster
m1 = monster('Кощей')
m2 = monster('Змей Горыныч')
m3 = monster('Упырь')
sword = Sword
s1 = sword('Кладенец')
s2 = sword('Палаш')
bow = Bow
b1 = bow('дубовый')
fighter = Fighter
f1 = fighter('Илья Муромец',s1)
f1.attac(m1)
f1.change_weapon(s2)
f1.attac(m2)
f1.change_weapon(b1)
f1.attac(m3)
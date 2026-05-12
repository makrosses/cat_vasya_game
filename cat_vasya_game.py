from abc import ABC, abstractmethod
import math

class Unit(ABC):
    '''Абстрактный класс Unit'''
    
    def __init__(
            self, strength: int, dexterity:int, constitution:int, 
            wisdom:int, intelligence:int, charisma:int):
        self.strength: int = strength
        self.dexterity: int = dexterity
        self.constitution: int = constitution
        self.wisdom: int = wisdom
        self.intelligence: int = intelligence
        self.charisma: int = charisma

    @abstractmethod
    def calculate_max_health(self):
        '''Метод подсчета максимального здоровья'''
        pass

    @abstractmethod
    def calculate_damage(self):
        '''Метод подсчета урона'''
        pass

    @abstractmethod
    def calculate_defense(self):
        '''Метод подсчета защиты'''
        pass


class Character(Unit):
    '''Класс всех персонажей'''

    def __init__(
            self, strength: int, dexterity:int, constitution:int, 
            wisdom:int, intelligence:int, charisma:int):
        self.strength: int = strength
        self.dexterity: int = dexterity
        self.constitution: int = constitution
        self.wisdom: int = wisdom
        self.intelligence: int = intelligence
        self.charisma: int = charisma

    def calculate_max_health(self) -> int:
        '''Метод подсчета максимального здоровья'''
        return math.floor(self.constitution * 10 + self.strength / 2)

    def calculate_damage(self) -> int:
        '''Метод подсчета урона'''
        return math.floor(self.strength * 1.5 + self.dexterity / 4)
    
    def calculate_defense(self) -> int:
        '''Метод подсчета защиты'''
        return math.floor(self.constitution * 1.5 + self.dexterity / 3)
    

class Monster(Unit):
    '''Класс всех монстров'''

    def __init__(
            self, strength: int, dexterity: int, constitution: int, 
            wisdom: int, intelligence: int, charisma: int):
        self.strength: int = strength
        self.dexterity: int  = dexterity
        self.constitution: int = constitution
        self.wisdom: int = wisdom
        self.intelligence: int = intelligence
        self.charisma: int = charisma

    def calculate_max_health(self) -> int:
        '''Метод подсчета максимального здоровья'''
        return math.floor(self.constitution * 8 + self.strength / 3) 

    def calculate_damage(self) -> int:
        '''Метод подсчета урона'''
        return math.floor(self.strength * 2 + self.constitution / 5)
    
    def calculate_defense(self) -> int:
        '''Метод подсчета защиты'''
        return math.floor(self.constitution * 1.2 + self.strength / 5)
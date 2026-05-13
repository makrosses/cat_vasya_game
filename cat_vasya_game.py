'''
Полностью переработана архитектура. Абстрактный класс Unit остался, 
но теперь от него наследуется только Character. В конструктор Character 
добавляется параметр character_class (строка) и сохраняется
как атрибут. Также в конструкторе сразу рассчитывается максимальное здоровье,
урон и защита и сохраняются в соответствующие поля.
'''

from abc import ABC, abstractmethod
import math

class Unit(ABC):
    '''
    Абстрактный класс Unit
    '''
    
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
        '''
        Метод подсчета максимального здоровья
        '''
        pass

    @abstractmethod
    def calculate_damage(self):
        '''
        Метод подсчета урона
        '''
        pass

    @abstractmethod
    def calculate_defense(self):
        '''
        Метод подсчета защиты
        '''
        pass


class Character(Unit):
    '''
    Класс всех персонажей
    '''
    # Множество возможных классов (character_class) у Character
    valid_classes = {"warrior", "mage", "hunter"}

    def __init__(
            self, strength: int, dexterity:int, constitution:int, 
            wisdom:int, intelligence:int, charisma:int, character_class:str):
        '''
        Конструктор: инициализация атрибутов обьекта
        '''
        character_class = character_class.lower() #Приводим к нижнему регистру
        if character_class not in self.valid_classes: #Проверка на правильный класс
            raise ValueError("Недопустимый класс!")
        self.strength: int = strength
        self.dexterity: int = dexterity
        self.constitution: int = constitution
        self.wisdom: int = wisdom
        self.intelligence: int = intelligence
        self.charisma: int = charisma
        self.character_class: str = character_class
        self.max_health: int = self.calculate_max_health()
        self.damage: int = self.calculate_damage()
        self.defense: int = self.calculate_defense()

    def calculate_max_health(self):
        '''
        Метод подсчета максимального здоровья
        '''
        return math.floor(self.strength / 2 + self.constitution * 10)

    def calculate_damage(self):
        '''
        Метод подсчета урона
        '''
        if self.character_class == "warrior":
            return math.floor(self.strength * 2.2 + self.constitution / 3)                  
        elif self.character_class == "mage":
            return math.floor(self.intelligence * 2.5 + self.wisdom / 2)
        elif self.character_class == "hunter":
            return math.floor(self.dexterity * 1.9 + self.strength / 3)

    def calculate_defense(self):
        '''
        Метод подсчета защиты
        '''
        if self.character_class == "warrior":
            return math.floor(self.constitution * 1.8 + self.strength / 4)
        elif self.character_class == "mage":
            return math.floor(self.wisdom * 1.3 + self.intelligence / 6)
        elif self.character_class == "hunter":
            return math.floor(self.dexterity * 1.6 + self.constitution / 5)
            

rumka = Character(2, 2, 3, 4, 5, 6, "jfjf")

print(rumka.max_health)
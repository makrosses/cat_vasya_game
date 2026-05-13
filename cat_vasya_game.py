'''
Что получилось?
-Абстрактный класс Unit с шестью характеристиками и абстрактными методами расчёта здоровья, 
урона, защиты, а теперь ещё и список заклинаний (spells) и ману (mana).
-Класс Character, наследующий от Unit и реализующий calculate_max_health, 
calculate_damage и calculate_defense с помощью проверки атрибута 
character_class (значения 'warrior', 'mage', 'hunter').
-Метод calculate_max_mana в Character, который также опирается на character_class 
для выбора формулы.
-Абстрактный класс Spell с названием, уроном и стоимостью маны, 
и хотя бы три конкретных заклинания (Fireball, IceLance, LightningBolt), 
реализующих метод cast().
-Методы в Unit для управления заклинаниями: add_spell(spell) и cast_spell(index),
 с проверкой маны и вычетом стоимости.
При создании персонажа его текущая мана автоматически устанавливается равной
 максимальной (вызов calculate_max_mana в конструкторе).
-Невозможность создать экземпляры абстрактных классов Unit и 
Spell — только конкретные наследники или класс Character.
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
        self.spells: list = []
        self.mana: int = 0

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

    def add_spell(self, spell):
        '''
        Добавляет заклинание в список доступных заклинаний
        '''
        self.spells.append(spell)

    def cast_spell(self, index: int):
        '''
        Применяет заклинание по индексу
        Проверяет наличие достаточного количества маны
        '''
        if index < 0 or index >= len(self.spells):
            raise IndexError("Заклинание не найдено")
        
        spell = self.spells[index]
        
        if self.mana < spell.mana_cost:
            raise ValueError(
                f"Недостаточно маны! Требуется: {spell.mana_cost}, "
                f"доступно: {self.mana}"
            )
        
        self.mana -= spell.mana_cost
        return spell.cast()
    

class Spell(ABC):
    '''
    Абстрактный класс Spell
    '''   
    def __init__(self, name, damage, mana_cost):
        self.name = name
        self.damage = damage
        self.mana_cost = mana_cost

    @abstractmethod
    def cast(self):
        '''
        Абстрактный метод cast
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
        self.max_mana: int = self.calculate_max_mana()
        self.spells: list = []
        self.mana: int = self.max_mana

    def calculate_max_health(self) -> int:
        '''
        Метод подсчета максимального здоровья
        '''
        return math.floor(self.strength / 2 + self.constitution * 10)

    def calculate_damage(self) -> int:
        '''
        Метод подсчета урона
        '''
        if self.character_class == "warrior":
            return math.floor(self.strength * 2.2 + self.constitution / 3)                  
        elif self.character_class == "mage":
            return math.floor(self.intelligence * 2.5 + self.wisdom / 2)
        elif self.character_class == "hunter":
            return math.floor(self.dexterity * 1.9 + self.strength / 3)

    def calculate_defense(self) -> int:
        '''
        Метод подсчета защиты
        '''
        if self.character_class == "warrior":
            return math.floor(self.constitution * 1.8 + self.strength / 4)
        elif self.character_class == "mage":
            return math.floor(self.wisdom * 1.3 + self.intelligence / 6)
        elif self.character_class == "hunter":
            return math.floor(self.dexterity * 1.6 + self.constitution / 5)

    def calculate_max_mana(self) -> int:
        '''
        Метод подсчета максимальной маны в зависимости от класса персонажа
        '''
        if self.character_class == "warrior":
            return math.floor(self.intelligence + self.strength // 2)
        elif self.character_class == "mage":        
            return math.floor(self.intelligence * 3 + self.wisdom)
        elif self.character_class == "hunter":
            return math.floor(self.dexterity * 1.5 + self.wisdom // 2)


class Fireball(Spell):
    '''
    Заклинание огненного шара
    '''
    def __init__(self):
        super().__init__(name="LightningBolt", damage=40, mana_cost=20)

    def cast(self):
        return self.damage


class IceLance(Spell):
    '''
    Заклинание ледяного копья
    '''
    def __init__(self):
        super().__init__(name="LightningBolt", damage=40, mana_cost=20)

    def cast(self):
        return self.damage


class LightningBolt(Spell):
    '''
    Заклинание молнии
    '''
    def __init__(self):
        super().__init__(name="LightningBolt", damage=40, mana_cost=20)

    def cast(self):
        return self.damage

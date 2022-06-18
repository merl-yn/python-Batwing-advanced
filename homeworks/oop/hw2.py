import random
from abc import ABC, abstractmethod

# 1


class Animals:
    def __init__(self, hp, endurance):
        self.hp = hp
        self.endurance = endurance

    @property
    def eat(self):
        self.hp += 10

    @property
    def sleep(self):
        self.endurance += 5


class Dogs(Animals):
    def __init__(self, hp, endurance):
        super().__init__(hp, endurance)

    def do_bark(self):
        self.endurance -= 3

    def do_attack(self):
        self.hp -= 7


class Cats(Animals):
    def __init__(self, hp, endurance):
        super().__init__(hp, endurance)

    def do_maw(self):
        self.endurance -= 3

    def do_defend(self):
        self.hp -= 7


class Cows(Animals):
    def __init__(self, hp, endurance):
        super().__init__(hp, endurance)

    def get_milk(self):
        self.endurance -= 2


class Pigs(Animals):
    def __init__(self, hp, endurance):
        super().__init__(hp, endurance)

    def do_bath_swamp(self):
        self.endurance -= 4


class Horses(Animals):
    def __init__(self, hp, endurance):
        super().__init__(hp, endurance)

    def run(self):
        self.endurance -= 4

# 1a


class Human(Animals):
    def __init__(self, hp, endurance, marks, money):
        super().__init__(hp, endurance)
        self.marks = marks
        self.money = money

    def study(self):
        self.marks = [random.randint(1, 5), random.randint(1, 5), random.randint(1, 5)]

    def work(self):
        self.money += random.randint(10, 50)


class Centaur(Human, Animals):
    def __init__(self, hp, endurance, marks, money):
        super().__init__(hp, endurance, marks, money)

    def get_archery(self):
        self.endurance -= 3


# 2
# a composition

class Person:
    def __init__(self):
        arm1 = Arm("5 fingers")
        arm2 = Arm("4 fingers")
        self.arms = [arm1.fingers, arm2.fingers]


class Arm:
    def __init__(self, fingers):
        self.fingers = fingers


# b aggregation


class CellPhone:
    def __init__(self, screen):
        self.screen = screen


class Screen:
    def __init__(self, screen_type):
        self.screen_type = screen_type


screen = Screen('OLED')
cell_phone = CellPhone(screen)

# 3


class Profile:
    def __init__(self, name, last_name, phone_number, address, email, birthday, age, sex=['male', 'female']):
        self.name = str(name)
        self.last_name = str(last_name)
        self.phone_number = str(phone_number)
        self.address = str(address)
        self.email = str(email)
        self.birthday = str(birthday)
        self.age = int(age)
        self.sex = random.choice(sex)

    def __str__(self):
        return f'{self.name}, {self.last_name},' \
               f' {self.phone_number}, {self.address},' \
               f' {self.email}, {self.birthday}, {self.age}' \
               f' {self.sex}'


# 4

class Laptop(ABC):

    @abstractmethod
    def get_screen(self):
        raise NotImplementedError('This method was not implemented')

    @abstractmethod
    def get_keyboard(self):
        raise NotImplementedError('This method was not implemented')

    @abstractmethod
    def get_touchpad(self):
        raise NotImplementedError('This method was not implemented')

    @abstractmethod
    def get_webcam(self):
        raise NotImplementedError('This method was not implemented')

    @abstractmethod
    def get_ports(self):
        raise NotImplementedError('This method was not implemented')

    @abstractmethod
    def get_dynamics(self):
        raise NotImplementedError('This method was not implemented')


class HPLaptop(Laptop):
    def __init__(self, screen, keyboard, touchpad, webcam, ports, dynamics):
        self.screen = screen
        self.keyboard = keyboard
        self.touchpad = touchpad
        self.webcam = webcam
        self.ports = ports
        self.dynamics = dynamics

    def get_screen(self):
        return f'Laptop has {self.screen} screen.'

    def get_keyboard(self):
        return f'Laptop has {self.keyboard} screen.'

    def get_touchpad(self):
        return f'Laptop has {self.touchpad} screen.'

    def get_webcam(self):
        return f'Laptop has {self.webcam} screen.'

    def get_ports(self):
        return f'Laptop has {self.ports} screen.'

    def get_dynamics(self):
        return f'Laptop has {self.dynamics} screen.'


if __name__ == '__main__':
    centaur1 = Centaur(10, 34, None, 25)
    centaur1.eat
    centaur1.sleep
    centaur1.work
    centaur1.get_archery
    print(centaur1.hp, centaur1.endurance, centaur1.money)
import random

AREA = {
    'small': 40,
    'middle': 60,
    'big': 80,
    'very big': 100
}

COST = {
    AREA['small']: 500,
    AREA['middle']: 1000,
    AREA['big']: 1500,
    AREA['very big']: 3000
}


class Person:

    def __init__(self, name, age, availability_of_money, make_home=["make own home", "without own home"]):
        self.name = name
        self.age = int(age)
        self.availability_of_money = int(availability_of_money)
        self.make_home = random.choice(make_home)


class Human(Person):

    def __init__(self, name, age, availability_of_money, make_home=["make own home", "without own home"]):
        super().__init__(name, age, availability_of_money, make_home)
        self.need_discount = None
        self.house = None
        self.option = None

    def get_info(self):
        return f'My name is {self.name}. I`m {self.age}. I have {self.availability_of_money}$ and I {self.make_home}.'

    def make_money(self):
        self.availability_of_money += random.randint(10, 50)
        return f'You have {self.availability_of_money}$'

    @property
    def buy_house(self):
        self.house = Home()

        if self.make_home == "without own home":

            # 0-499
            if self.availability_of_money in range(0, 500):
                return "Not enough money"

            # 500-999
            elif self.availability_of_money in range(500, 1000):
                i = input('Do you want to buy a house? Choose y/n: ')

                if i == 'y':
                    self.make_home = "make own home"
                    self.need_discount = input("Do you have a discount? Choose y/n: ")

                    if self.need_discount == 'y':
                        self.house.area = list(AREA.values())[0]
                        self.house.cost = list(COST.values())[0]
                        self.availability_of_money -= self.house.apply_discount()
                        return f'You bought {list(AREA.keys())[0]} home with area {list(AREA.values())[0]}m2.' \
                               f' Home cost {int(self.house.apply_discount())}'

                    else:
                        self.availability_of_money -= 500
                        return f'You bought {list(AREA.keys())[0]} home with area {list(AREA.values())[0]}m2. ' \
                               f'Home cost {list(COST.values())[0]}$'

                else:
                    return "You didn't want to buy a house"

            # 1000-1499
            elif self.availability_of_money in range(1000, 1500):
                i = input('Do you want to buy a house? Choose y/n: ')

                if i == 'y':

                    self.option = input("You can buy small or middle house. Choose one of: ")

                    # 500-1000
                    if self.option == 'small':

                        self.make_home = "make own home"
                        self.need_discount = input("Do you have a discount? Choose y/n: ")

                        if self.need_discount == 'y':
                            self.house.area = list(AREA.values())[0]
                            self.house.cost = list(COST.values())[0]
                            self.availability_of_money -= self.house.apply_discount()
                            return f'You bought {list(AREA.keys())[0]} home with area {list(AREA.values())[0]}m2.' \
                                   f' Home cost {int(self.house.apply_discount())}'
                        else:
                            self.availability_of_money -= 500
                            return f'You bought {list(AREA.keys())[0]} home with area {list(AREA.values())[0]}m2. ' \
                                   f'Home cost {list(COST.values())[0]}$'

                    # 1000-1499
                    elif self.option == 'middle':

                        self.make_home = "make own home"
                        self.need_discount = input("Do you have a discount? Choose y/n: ")

                        if self.need_discount == 'y':
                            self.house.area = list(AREA.values())[1]
                            self.house.cost = list(COST.values())[1]
                            self.availability_of_money -= self.house.apply_discount()
                            return f'You bought {list(AREA.keys())[1]} home with area {list(AREA.values())[1]}m2.' \
                                   f' Home cost {int(self.house.apply_discount())}'

                        else:
                            self.availability_of_money -= 1000
                            return f'You bought {list(AREA.keys())[1]} home with area {list(AREA.values())[1]}m2. ' \
                                   f'Home cost {list(COST.values())[1]}$'

                    # incorrect
                    else:
                        print('Choose SMALL or MIDDLE!!!')
                        return self.get_info()

                else:
                    return "You didn't want to buy a house"

            # 1500-2999
            elif self.availability_of_money in range(1500, 3000):
                i = input('Do you want to buy a house? Choose y/n: ')

                if i == 'y':

                    self.option = input("You can buy small, middle or big house. Choose one of: ")

                    # 500-1000
                    if self.option == 'small':

                        self.make_home = "make own home"
                        self.need_discount = input("Do you have a discount? Choose y/n: ")

                        if self.need_discount == 'y':
                            self.house.area = list(AREA.values())[0]
                            self.house.cost = list(COST.values())[0]
                            self.availability_of_money -= self.house.apply_discount()
                            return f'You bought {list(AREA.keys())[0]} home with area {list(AREA.values())[0]}m2.' \
                                   f' Home cost {int(self.house.apply_discount())}'

                        else:
                            self.availability_of_money -= 500
                            return f'You bought {list(AREA.keys())[0]} home with area {list(AREA.values())[0]}m2. ' \
                                   f'Home cost {list(COST.values())[0]}$'

                    # 1000-1499
                    elif self.option == 'middle':

                        self.make_home = "make own home"
                        self.need_discount = input("Do you have a discount? Choose y/n: ")

                        if self.need_discount == 'y':
                            self.house.area = list(AREA.values())[1]
                            self.house.cost = list(COST.values())[1]
                            self.availability_of_money -= self.house.apply_discount()
                            return f'You bought {list(AREA.keys())[1]} home with area {list(AREA.values())[1]}m2.' \
                                   f' Home cost {int(self.house.apply_discount())}'
                        else:
                            self.availability_of_money -= 1000
                            return f'You bought {list(AREA.keys())[1]} home with area {list(AREA.values())[1]}m2. ' \
                                   f'Home cost {list(COST.values())[1]}$'

                    # 1500-2999
                    elif self.option == 'big':

                        self.make_home = "make own home"
                        self.need_discount = input("Do you have a discount? Choose y/n: ")

                        if self.need_discount == 'y':
                            self.house.area = list(AREA.values())[2]
                            self.house.cost = list(COST.values())[2]
                            self.availability_of_money -= self.house.apply_discount()
                            return f'You bought {list(AREA.keys())[2]} home with area {list(AREA.values())[2]}m2.' \
                                   f' Home cost {int(self.house.apply_discount())}'
                        else:
                            self.availability_of_money -= 1500
                            return f'You bought {list(AREA.keys())[2]} home with area {list(AREA.values())[2]}m2. ' \
                                   f'Home cost {list(COST.values())[2]}$'

                    # incorrect
                    else:
                        print('Choose SMALL, MIDDLE, BIG!!!')
                        return self.get_info()

                else:
                    return "You didn't want to buy a house"

            # 3000+
            elif self.availability_of_money >= 3000:
                i = input('Do you want to buy a house? Choose y/n: ')

                if i == 'y':
                    self.option = input("You can buy small, middle, big or very big house. Choose one of: ")

                    # 500-1000
                    if self.option == 'small':

                        self.make_home = "make own home"
                        self.need_discount = input("Do you have a discount? Choose y/n: ")

                        if self.need_discount == 'y':
                            self.house.area = list(AREA.values())[0]
                            self.house.cost = list(COST.values())[0]
                            self.availability_of_money -= self.house.apply_discount()
                            return f'You bought {list(AREA.keys())[0]} home with area {list(AREA.values())[0]}m2.' \
                                   f' Home cost {int(self.house.apply_discount())}'

                        else:
                            self.availability_of_money -= 500
                            return f'You bought {list(AREA.keys())[0]} home with area {list(AREA.values())[0]}m2. ' \
                                   f'Home cost {list(COST.values())[0]}$'

                    # 1000-1499
                    elif self.option == 'middle':

                        self.make_home = "make own home"
                        self.need_discount = input("Do you have a discount? Choose y/n: ")

                        if self.need_discount == 'y':
                            self.house.area = list(AREA.values())[1]
                            self.house.cost = list(COST.values())[1]
                            self.availability_of_money -= self.house.apply_discount()
                            return f'You bought {list(AREA.keys())[1]} home with area {list(AREA.values())[1]}m2.' \
                                   f' Home cost {int(self.house.apply_discount())}'
                        else:
                            self.availability_of_money -= 1000
                            return f'You bought {list(AREA.keys())[1]} home with area {list(AREA.values())[1]}m2. ' \
                                   f'Home cost {list(COST.values())[1]}$'

                    # 1500-2999
                    elif self.option == 'big':

                        self.make_home = "make own home"
                        self.need_discount = input("Do you have a discount? Choose y/n: ")

                        if self.need_discount == 'y':
                            self.house.area = list(AREA.values())[2]
                            self.house.cost = list(COST.values())[2]
                            self.availability_of_money -= self.house.apply_discount()
                            return f'You bought {list(AREA.keys())[2]} home with area {list(AREA.values())[2]}m2.' \
                                   f' Home cost {int(self.house.apply_discount())}'
                        else:
                            self.availability_of_money -= 1500
                            return f'You bought {list(AREA.keys())[2]} home with area {list(AREA.values())[2]}m2. ' \
                                   f'Home cost {list(COST.values())[2]}$'

                    # 3000+
                    elif self.option == 'very big':

                        self.make_home = "make own home"
                        self.need_discount = input("Do you have a discount? Choose y/n: ")

                        if self.need_discount == 'y':
                            self.house.area = list(AREA.values())[3]
                            self.house.cost = list(COST.values())[3]
                            self.availability_of_money -= self.house.apply_discount()
                            return f'You bought {list(AREA.keys())[3]} home with area {list(AREA.values())[3]}m2.' \
                                   f' Home cost {int(self.house.apply_discount())}'
                        else:
                            self.availability_of_money -= 3000
                            return f'You bought {list(AREA.keys())[3]} home with area {list(AREA.values())[3]}m2. ' \
                                   f'Home cost {list(COST.values())[3]}$'

                    # incorrect
                    else:
                        print('Choose SMALL, MIDDLE, BIG or VERY BIG!!!')
                        return self.get_info()

                else:
                    return "You didn't want to buy a house"

        else:
            return "You already have a house!"


class House:

    def __init__(self):
        self.area = random.choice(list(AREA.values()))
        self.cost = COST[self.area]


class Home(House):

    def apply_discount(self):
        if self.area == 40:
            return self.cost / 100 * 94
        elif self.area == 60:
            return self.cost / 100 * 92
        elif self.area == 80:
            return self.cost / 100 * 90
        elif self.area == 100:
            return self.cost / 100 * 88
        else:
            print("Such a house does not exist!")


if __name__ == '__main__':
    petya = Human('Petya', 18, 3000)
    print(petya.get_info())
    print(petya.make_money())
    print(petya.buy_house)
    print(petya.make_money())
    print(petya.buy_house)

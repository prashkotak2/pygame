class Hero():
    def __init__(self):
        raise NotImplementedError("Do not create raw Hero objects")

    def __str__(self):
        return self.name, self.identity, self.power, self.hp

    def is_alive(self):
        return self.hp > 0


class WonderWoman(Hero):
    """Wonder Woman's name, idenity and characteristics"""
    def __init__(self):
        self.name = "Wonder Woman"
        self.identity = "Diana Prince"
        self.power = "super strength"
        self.hp = 200


class Batman(Hero):
    """Batman's name, idenity and characteristics"""
    def __init__(self):
        self.name = "Batman"
        self.identity = "Bruce Wayne"
        self.power = "martial arts"
        self.hp = 150


class Flash(Hero):
    """The Flash's name, idenity and characteristics"""
    def __init__(self):
        self.name = "The Flash"
        self.identity = "Barry Allen"
        self.power = "super speed"
        self.hp = 90


WonderWoman = WonderWoman()
Batman = Batman()
Flash = Flash()
heroes = [WonderWoman.name, Batman.name, Flash.name]


def hero_check(hero):
    """Checks which hero was chosen and prints out the characteristics"""
    if hero == "Wonder Woman":
        hero_characteristics(WonderWoman)
    elif hero == "The Flash":
        hero_characteristics(Flash)
    else:
        hero_characteristics(Batman)


def hero_characteristics(hero):
    """Prints out the hero's characteristics"""
    print(f"{hero.name}'s true identy is {hero.identity}")
    print(f"{hero.name}'s super power is {hero.power}")
    print(f"{hero.name} has {hero.hp} health points")

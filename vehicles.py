# dictionary of DC heroes and their vehicles. Nested set for Batman
# to account for multiple vehicles
vehicles = {"Wonder Woman": "Invisible Plane",
            "The Flash": None,
            # Batman has a nested set of vehicles
            "Batman": {"Tumbler", "Batmobile", "The Bat", "Batpod"}
            }


class Vehicle():
    def __init__(self, name, hero, protection, attack):
        self.name = name
        self.hero = hero
        self.protection = protection
        self.attack = attack

    def __str__(self):
        return self.name

    def description(self):
        print(f"{self.name} can only be used by {self.hero}.")
        print(f"{self.name} has a protection value of {self.protection}.")
        print(f"{self.name} has an attack value of {self.attack}")


class InvisiblePlane(Vehicle):
    def __init__(self, name, hero, protection, attack):
        self.name = "Invisible Plane"
        self.hero = "Wonder Woman"
        self.protection = 100
        self.attack = 20


class Tumbler(Vehicle):
    def __init__(self, name, hero, protection, attack):
        self.name = "Tumble"
        self.hero = "Batman"
        self.protection = 100
        self.attack = 50

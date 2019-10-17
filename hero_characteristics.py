# game characters
heroes = {
         "Batman": {"identity": "Bruce Wayne", "power": "martial arts",
                    "health points": 150},
         "Wonder Woman": {"identity": "Diana Prince", "power": "super strength",
                          "health points": 200},
         "The Flash": {"identity": "Barry Allen", "power": "super speed",
                       "health points": 90}
         }
# game locations
locations = {"Central City": "home of The Flash",
             "Hall of Justice": "headquarters for the Justice League",
             "Bat Cave": "subterranean headquarters of Batman",
             "Gotham City": "home of Batman",
             "Metropolis": "home of Superman",
             "Themyscira": "birth place of Wonder Woman"
             }
# inventory paired with characters
inventory = {"Wonder Woman": {"Lasso of Truth":
                              {"description": "extracts truth from people",
                               "damage": 0, "protection": 5},
                              "Bracelets of Submission":
                              {"description": "bulletproof bracelets",
                               "damage": 100, "protection": 50},
                              "Sword of Athena":
                              {"description":
                               "magically-empowered sword wielded",
                               "damage": 500, "protection": 0}},
            "Batman": {"Batarang":
                       {"description": "boomerang shaped like a bat",
                        "damage": 10, "protection": 0},
                       "Grapple hook":
                       {"description": "pear-shooting spring-based device",
                        "damage": 5, "protection": 0},
                       "Sonic Bat Device":
                       {"description":
                        "high frequency emitter allowing the control of bats",
                        "damage": 15, "protection": 100}},
             "The Flash": {"Red suit":
                           {"description":
                            "protection when travelling at super speed",
                            "damage": 0, "protection": 100}}
             }
# print out the characters with their characteristics
for hero in heroes:
    i = heroes[hero]["identity"]
    p = heroes[hero]["power"]
    hp = heroes[hero]["health points"]
    print(f"{hero}'s secret identity is {i}")
    print(f"{hero}'s super power is {p}")
    print(f"{hero} has {hp} health points")
    print("\n")
# print out the locations and their descriptions
for place in locations:
    description = locations[place]
    print(f"{place} is the {description}.")
# print out the invetory for each character, along with the characteristics
# of each item
for hero in inventory:
    print(f"{hero}'s Inventory:")
    for item in inventory[hero]:
        print(f"* {item}")
        for characteristics in inventory[hero][item]:
            detail = inventory[hero][item][characteristics]
            print(f"   {characteristics}: {detail}")

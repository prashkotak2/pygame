# game characters
heroes = {
         "Batman": {"identity": "Bruce Wayne", "power": "martial arts",
                    "health points": 150},
         "Wonder Woman": {"identity": "Diana Prince",
                          "power": "super strength",
                          "health points": 200},
         "The Flash": {"identity": "Barry Allen", "power": "super speed",
                       "health points": 90}
         }
# game cities
cities = {"Central City": "home of The Flash",
          "Hall of Justice": "headquarters for the Justice League",
          "Bat Cave": "subterranean headquarters of Batman",
          "Gotham City": "home of Batman",
          "Metropolis": "home of Superman",
          "Themyscira": "birth place of Wonder Woman"
          }
# map tile types
map_tiles = {"Enemy Tile": {"description": "location of an enemy",
                            "abbreviation": "ET",
                            "action": "must defeat the enemy to continue"},
             "Boss Tile": {"description": "location of a Big Boss enemy",
                           "abbreviation": "BT",
                           "action":
                           "may run away or fight the boss to continue"},
             "Weapons Tile": {"description": "location of a weapon",
                              "abbreviation": "WT",
                              "action":
                              "may pick up items or move to another location"},
             "Supply Tile": {"description":
                             "location of protection and healing items",
                             "abbreviation": "ST",
                             "action": "must pick up the weapon to continue"},
             "Blank Tile": {"description":
                            "location with no items",
                            "abbreviation": "BT",
                            "action": "may rest or move to another location"}
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
# dictionary of DC heroes and their vehicles. Nested set for Batman
# to account for multiple vehicles
vehicles = {"Wonder Woman": "Invisible Plane",
            "The Flash": None,
            # Batman has a nested set of vehicles
            "Batman": {"Tumbler", "Batmobile", "The Bat", "Batpod"}
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
# print out the cities and their descriptions
for place in cities:
    description = cities[place]
    print(f"{place} is the {description}.")
print("\n")
# print out the types of locations within the cities
for tiles in map_tiles:
    d = map_tiles[tiles]["description"]
    ab = map_tiles[tiles]["abbreviation"]
    act = map_tiles[tiles]["action"]
    print(f"You are on a {tiles} ({ab})tile. This is a {d}. You {act}.")
print("\n")
# print out the invetory for each character, along with the characteristics
# of each item
for hero in inventory:
    print(f"{hero}'s Inventory:")
    for item in inventory[hero]:
        print(f"* {item}")
        for characteristics in inventory[hero][item]:
            detail = inventory[hero][item][characteristics]
            print(f"   {characteristics}: {detail}")
print("\n")
# print a list of the hero's vehicles
for heroes in vehicles:
    vehicle = vehicles[heroes]
    # we need a nested loop for Batman because he has multiple vehicles
    if heroes == "Batman":
        batvehicles = vehicles["Batman"]
        print(f"{heroes}'s vehicles:")
        for results in batvehicles:
            print(f"* {results}")
    else:
        print(f"{heroes}'s vehicles:")
        print(f"* {vehicle}")
    print("\n")

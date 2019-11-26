import random
from tabulate import tabulate


# map tile types
map_tiles = {"Enemy": {"description": "location of an enemy",
                       "abbreviation": "ET",
                       "action": "must defeat the enemy to continue"},
             "Big Boss": {"description":
                          "Big Boss enemy location and the exit for the city",
                          "abbreviation": "BT",
                          "action":
                          "may run away or fight the boss to continue"},
             "Weapons": {"description": "location of a weapon",
                         "abbreviation": "WT",
                         "action":
                         "may pick up items or move to another location"},
             "Supplies": {"description":
                          "location of protection and healing items",
                          "abbreviation": "ST",
                          "action": "must pick up the weapon to continue"},
             " ": {"description":
                   "location with no items",
                   "abbreviation": "BT",
                   "action": "may rest or move to another location"},
             "Start": {"description": "entrance to the city",
                       "abbreviation": "S",
                       "action": "may rest or move to another location"}
             }


class MapTile():
    """ Map with x and y coordinates"""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return self.description, self.action, self.name

    def intro_text(self):
        raise NotImplementedError("Create a subclass instead!")

    def modify_player(self, player):
        """Added modify_player to every tile"""
        pass


class StartTile(MapTile):
    """Player starting position"""

    def intro_text(self):
        """Descriptive text for the Start Tile"""
        return """

        """


class BoringTile(MapTile):
    """Position with no materials"""
    def intro_text(self):
        return """
        There are no supplies or enemies here.
        """


class ViewMapTile(MapTile):
    """Position that prints a map"""
    def intro_text(self):
        """Descriptive text for the Viewable Map Tile"""
        return """
        You see a map on the wall.
        """

    def print_map(self):
        """Print a map of the ship with directions"""
        return """

        """


class SuppliesTile(MapTile):
    """Position that contains survival supplies"""
    def __init__(self, x, y):
        """Initial supplies at the tile"""
        # index for switching descriptive messagages
        self.i = 0
        self.name = "Supplies"
        # self.inventory = [items.Blaster(), items.OxygenTank(),
        #                   items.SpaceSuit(), items.FirstAid(),
        #                   items.CrustyBread(), items.Water(), items.Shelter()]

        super().__init__(x, y)

    def intro_text(self):
        """Descriptive texts for the Start Tile"""
        # initial description
        self.start_supplies = """

        """
        # description after supplies are added
        self.no_supplies = "No supplies left at this location"
        # define the descriptive text for the supply text
        supply_text = [self.start_supplies, self.no_supplies]
        # switch messages after the supplies are added
        if self.i == 0:
            self.i += 1
            return supply_text[0]
        else:
            return supply_text[1]

    def suppy(self):
        """Message for what items were added"""
        for i, item in enumerate(self.inventory, 1):
            print("You added the following items to your inventory!")
            print("{}. {}.".format(i, item.name))
        self.add_inventory()

    def add_inventory(self, current_inventory):
        """Add items from the supply tile to the player's inventory"""
        for item in self.inventory:
            current_inventory.append(item)
        # remove supplies from the tile
        self.inventory = []


class BigBoss(MapTile):
    """Position that contains the main villin of the level"""
    def modify_player(self, player):
        """Player wins the level if they beat the big boss"""
        player.victory = True
        sys.exit()

    def intro_text(self):
        return """

        """

class EnemyTile(MapTile):


def append_list(dictionary, list):
    """Create a list from elements of a dictionary"""
    for x in dictionary:
        list.append(x)


def replace_tile(list, tile1, tile2):
    """Make sure that replaced tiles do not overwrite each other"""
    while random_tile(list, tile1) == random_tile(list, tile2):
            random_tile(list, tile1)
            random_tile(list, tile2)


def random_tile(list, tile):
    """Choose a random tile to replace and return the indices"""
    x = random.choice(list)
    y = random.choice(x)
    n = list.index(x)
    m = x.index(y)
    list[n][m] = tile
    return (n, m)


def generate_map(list):
    """randomly generate a 5x5 city map from tile types"""
    map = [[random.choice(list) for i in range(5)] for j in range(5)]
    # add boss and start tiles
    replace_tile(map, "Big Boss", "Start")
    return map


def print_map(dictionary):
    """print out each city map generated"""
    for key in dictionary:
        map = dictionary[key]
        print(f"{key}")
        # format the maps in rows and columns
        print(tabulate(map, tablefmt="plain"))
        print("\n")


def tile_at(x, y):
    """Locates the tile at a coordinate"""
    if x < 0 or y < 0:
        return None
    try:
        return map[y][x]
    except IndexError:
        return None


# game cities
cities = {"Central City": "home of The Flash",
          "Hall Of Justice": "headquarters for the Justice League",
          "Gotham City": "home of Batman",
          "Metropolis": "home of Superman",
          "Themyscira": "birth place of Wonder Woman"
          }


# generate a list of cities
city_level = []
append_list(cities, city_level)
# generate a list of tile types removing the start and boss tiles
tile_types = []
append_list(map_tiles, tile_types)
tile_types.remove("Big Boss")
tile_types.remove("Start")

# organize each city level and its map in a dictionary
main_map = {}
for city in city_level:
    city_map = generate_map(tile_types)
    main_map[city] = city_map

# print_map(main_map)

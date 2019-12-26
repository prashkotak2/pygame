import random
from tabulate import tabulate
#

# class Invent():
#     def
ef msg(room):
    if room['msg'] == '' :
        return "You have entered the " + room['name'] + '.'
    else:
        return room['msg']

def get_choice(room,dir):
    if dir=='N':
        choice = 1
    elif dir=='E':
        choice = 5
    elif dir=='S':
        choice = 2
    elif dir=='W':
        choice = 3
    else:
        return -1

    if room['directions'][choice] == 0:
        return 4
    else:
        return choice


# defining the function to start game
def mapcode():
    final = []  # making a list
    game = []  # making a list
    game1 = []  # list for game1
    finalgame = []  # making list for final one whch will be main list
    f1 = []
    i = 6  # index is set equal to 6
    # list for locations
    list = ['Enterence ', ['livingroom', 'bathroom', 'kitchen', 'bedroom', "hall"]]
    # using loop for printing
    for j in range(1):
        final.append(list[0])  # adding a value in a list
        for i in range(20):
            final.append(random.choice(list[len(list) - 1]))  # adding it to list
            # adding  it into final list
        game.append(final)
        final = []
    for k in game[0]:
        if k not in game1:
            game1.append(k)
    finalgame.append(game1)  # adding it to the main list

    a = finalgame[0][:3]  # it will divide the output into to 2 rows
    b = finalgame[0][3:]  # it will divide the output into to 2 rows

    # print()
    # print(a)
    # print(b)
    c = []
    c.append(a)
    c.append(b)
    print(c)
    print(tabulate(c, tablefmt="fancy_grid"))  # printing it in a table
    print(game1)


def startgame():
    game1 = [[ 'Diningroom ', 'Livingroom','Park '],['Kitchen','Entrance Way','Family Room'],['garrage','HallWay','backyard'] ]

    print(tabulate(game1, tablefmt="fancy_grid"))
    dirs = (0,0,0,0)


    entrance = {'name': 'Entrance Way ', 'direction': dirs, 'msg': ''}
    livingroom = {'name': 'Livingroom', 'directions': dirs, 'msg': ''}
    hallway = {'name': 'HallWay ', 'direction': dirs, 'msg': ''}
    kitchen = {'name': 'Kitchen', 'direction': dirs, 'msg': ''}
    diningroom = {'name': 'Diningroom', 'direction': dirs, 'msg': ''}
    family_room = {'name': 'Family Room', 'direction': dirs, 'msg': ''}

    entrance['directions'] = (livingroom, hallway , 0, 0)
    livingroom['directions'] = (diningroom, 0, 0, entrance)
    hallway['directions'] = (0, kitchen, 0, family_room)
    kitchen['directions'] = (0, diningroom, entrance, hallway)
    diningroom['directions'] = (0, 0, livingroom, kitchen)
    family_room['directions'] = (0, hallway, 0, 0)

    rooms = [livingroom, hallway, kitchen, diningroom, family_room]
    room_with_eggs = random.choice(rooms)
    eggs_delivered = False
    room = entrance
    print('WELCOME,to game ')

    while True:
        if eggs_delivered and room['name'] == game1[0]:
            print('You have deliverd the eggs and camo to the entrance ')
            break;
        elif not eggs_delivered and room['name'] ==  room_with_eggs['name']:
        # elif not eggs_delivered and room['name'] ==  room_with_enemy['name']:
            eggs_deliverd = True
            print(msg(room) + ' There the basket an he is sleeping ' +
                  'right next to it! You have delivere the egs. '+
                  'Now get out quick ')
            room['msg'] = ('you are back in the ' + room['name'] +
                            '! YOU HAVE BEEN THERE.')
        else:
            print(msg(room))
            room['msg'] = 'You are back in' + room['name']

        stuck = True
        while stuck:
            dir =input("Whick direction do you want to go: N,E,S,W?")
            choice = get_choice(room,dir)
            if choice == -1:
                dir = print("Please enter N,E,W,S?")
            elif choice == 4:
                dir = print("You cannot go that direction")
            else:
                room = room['directions'][choice]
                stuck = False

startgame()






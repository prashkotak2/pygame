import random


def msg(room):
    if room['msg'] == '' :
        return "You have entered the " + room['name'] + '.'
    else:
        return room['msg']

def get_choice(room,dir):
    if dir=='N':
        choice = 0
    elif dir=='E':
        choice = 1
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


def main():
    dirs = (0,0,0,0)

    entrance = {'name':'Entrance Way ','direction':dirs,'msg':''}
    livingroom = {'name':'Livingroom', 'directions' :dirs,'msg': ''}
    hallway = {'name':'HallWay ','direction':dirs,'msg':''}
    kitchen = {'name':'Kitchen','direction':dirs,'msg':''}
    diningroom = {'name':'Diningroom','direction':dirs,'msg':''}
    family_room = {'name':'Family Room','direction':dirs,'msg':''}


    entrance['directions'] = (kitchen,livingroom,0,0)
    livingroom['directions'] = (diningroom,0,0,entrance)
    hallway['directions'] = (0,kitchen,0,family_room)
    kitchen['directions'] = (0,diningroom,entrance,hallway)
    diningroom['directions'] = (0,0,livingroom,kitchen)
    family_room['directions'] = (0,hallway,0,0)


    rooms = [livingroom,hallway,kitchen,diningroom,family_room]
    room_with_eggs = random.choice(rooms)
    eggs_delivered = False
    room = entrance
    print('WELCOME,Bunny! Can u find basket?')

    while True:
        if eggs_delivered and room['name'] == 'Entrance Way':
            print('You have deliverd the eggs and camo to the entrance ')
            break;

        elif not eggs_delivered and room['name'] ==  room_with_eggs['name']:
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

main ()
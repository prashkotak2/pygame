# RPG based on the comic book series published by DC Comics
# 12 issue run: April 1985 - March 1986
import sys


def play():
    """Print an action menu and allow for continous game play"""
    print("Justice League: Crisis on Infinite Earths")
    print("Valid actions for current location")
    # valid directions and actions for the characters
    valid_actions = {"directions": ["north", "south", "east", "west"],
                     "actions": ["explore", "attack", "defend", "heal",
                                 "quit"]}
    # print a list a valid actions before user input. Organized according to
    # possible direction and actions
    for user_action in valid_actions:
        if user_action == "directions":
            print(f"Go in one of the following {user_action}:")
            possible_directions = valid_actions["directions"]
            for direction in possible_directions:
                print(f"* {direction}")
        else:
            print(f"Complete one of the following {user_action}:")
            possible_actions = valid_actions["actions"]
            for action in possible_actions:
                print(f"* {action}")
    while True:
        # after user input, print out the action choosen by the user
        action_input = get_player_command()
        direction = valid_actions["directions"]
        action = valid_actions["actions"]
        if action_input in direction:
            print(f"Go {action_input}!")
        elif action_input in action:
            print(f"{action_input}!")
            if action_input == "quit":
                sys.exit()
        else:
            print("Invalid action!")


def get_player_command():
    """Get user input and convert the string to lowercase"""
    action_input = input("Action: ")
    return action_input.lower()


play()

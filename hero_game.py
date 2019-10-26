# RPG based on the comic book series published by DC Comics
# 12 issue run: April 1985 - March 1986
print("Justice League: Crisis on Infinite Earths")
print("Valid actions for current location")
# valid directions and actions for the characters
valid_actions = {"directions": ["north", "south", "east", "west"],
                 "actions": ["explore", "attack", "defend", "heal"]}
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
# after user input, print out the action choosen by the user
action_input = input("Action: ")
direction = valid_actions["directions"]
action = valid_actions["actions"]
if action_input.lower() in direction:
    print(f"Go {action_input}!")
elif action_input.lower() in action:
    print(f"{action_input}!")

else:
    print("Invalid action!")

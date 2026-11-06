from game import new_game, available_actions, apply_action, is_win

player = new_game()


print("MYSTERY ISLAND")
print("WELCOME TO THE GAME, HOPE YOU ARE PREPARED")

name = input("What is your name player: ")
print(f"Welcome to Mystery Island, {name}!")



print(f"{name}, your inventory is empty.")
print(player["inventory"])

print(f"Your energy is: {player['energy']}")
print(f"Your current location is: {player['current_location']}")




playing = True

while playing:


    print("====== MYSTERY ISLAND ADVENTURE======")

    choices = available_actions()

    for number, action in enumerate(choices, start=1):
        print(f"{number}. {action}")

    choice = input("Choose your Location: ")

    action = choices[int(choice) - 1]

    if action == "Explore Beach":
        answer = input("Do you want to collect the Rope? ")
        answer = answer.lower()

    elif action == "Explore Jungle":
        print("You discovered a LAntern")
        answer = input("Do you want to collect the Lantern? ")
        answer = answer.lower()

    elif action == "Visit Cave":
        answer = input("do you want to go back and get lantern: ")
        answer = answer.lower()

    elif action == "Old Brigde":
        answer = input("do you want to go back and get rope: ")
        answer = answer.lower()


    else:
        answer = None
    
    apply_action(player, action, answer)


    print(f"You selected: {action}")






from game import new_game, available_actions, apply_action

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

    else:
        answer = None
    
    apply_action(player, action, answer)






    print(f"You selected: {action}")

'''
    if choice == "1":
        print("Enjoy the sunshine")
        print("There's a Rope here")
        if "Rope" in player["inventory"]:
            print("Already have rope in inventory")
        elif "Rope" not in player["inventory"]:
            invent = input("Do you want to collect the rope: ")
            invent = invent.lower()
            if invent == "yes":
                player["inventory"].append("Rope")
                print(player["inventory"])
                player["energy"] += 2
                print(f"You collected a rope and energy has increased to: {player['energy']}")
        
            else:
                print("Rope not collected")


    elif choice == "2":
        print("Beware of lurking Beast")

        if player["current_location"] == "Jungle":
            print("You are already in the Jungle!")

        else:
            if "Jungle" in player["visited_locations"]:
                required_energy = 2
                print("You have visited the Jungle before.")
            else:
                required_energy = 1
                print("This is a new location.")

            if player["energy"] >= required_energy:
                player["energy"] -= required_energy
                player["current_location"] = "Jungle"

                if "Jungle" not in player["visited_locations"]:
                    player["visited_locations"].append("Jungle")

                print(f"Current location: {player['current_location']}")
                print(f"Remaining energy: {player['energy']}")

            else:
                print("You don't have enough energy!")
                print("GAME OVER!")
                playing = False
        print("You discovered a Latern!")
        if "Lantern" in player["inventory"]:
            print("Already have Lantern in inventory")
        elif "Lantern" not in player["inventory"]:
            answer = input("Do you want to add Lantern in your inventory: ")
            answer = answer.lower()
            if answer == "yes":
                player["inventory"].append("Lantern")
                print(player["inventory"])
                player["energy"] += 2
                print(f"You collected a Lantern and energy has increased to: {player['energy']}")
        
        else:
            print("Lantern not collected")

            
    elif choice == "3":
        print("Make sure you have a Lantern")
        if "Lantern" in player["inventory"]:
            print("You are eligible to explore")
        else:
            print("You will loss energy")
            goback = input("do you want to go back and get lantern: ")
            goback = goback.lower()
            if goback == "yes":
                print("Go back to Jungle and collect the lantern")
            else:
                player["energy"] -= 2
                print(f"Your energy has decreased to: {player['energy']}")
    elif choice == "4":
        print("Using Rope will be crucial")
    elif choice == "5":
        print("Successfully Arrived")
    elif choice == "6":
        print("Inventory")
    elif choice == "7":
        print("Goodbye")
        playing = False
    else:
        print("Invalid Location")
'''




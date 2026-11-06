def new_game():
    player = {
    "inventory": [],
    "energy": 5,
    "visited_locations": ["Beach"],
    "current_location": "Beach",
    "bridge_crossed": False
    "game_over": False
    "won": False
}
    return player
    

def available_actions():
    actions = [
        "Explore Beach",
        "Explore Jungle",
        "Explore Cave",
        "Visit Old Bridge",
        "Visit Lighthouse",
        "Check Inventory",
        "Quit Game"
    ]

    return actions


def apply_action(player, action, answer):

    if action == "Explore Beach":
        print("Enjoy the sunshine")
        print("There's a Rope here")
        if "Rope" in player["inventory"]:
            print("Already have rope in inventory")
        else:
            print("You don't have a Rope yet")
            if answer == "yes":
                player["inventory"].append("Rope")
                player["energy"] += 2
                print(player["inventory"])
                print(f"You've collected Rope and your energy has increased to: {player['energy']}")
            else:
                print("Rope not collected")


    elif action == "Explore Jungle":
        print("Beware of lurking Beast")
        if player["current_location"] == "Jungle":
            print("You are already in the Jungle!")

        else:
            if "Jungle" in player["visited_locations"]:
                print("You have visited the Jungle before, going back requires energy")

                required_energy = 2
                

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
                

        print("You discovered a Lantern!")
        if "Lantern" in player["inventory"]:
            print("Already have Lantern in inventory")
        else:
            
            if answer == "yes":
                player["inventory"].append("Lantern")
                print(player["inventory"])
                player["energy"] += 2
                print(f"You collected a Lantern and energy has increased to: {player['energy']}")
        
            else:
                print("Lantern not collected")

    elif action == "Explore Cave":
        print("Make sure you have a Lantern")
        if "Lantern" in player["inventory"]:
            print("You are eligible to explore")
        else:
            print("You will loss energy")
            
            if answer == "yes":
                print("Go back to Jungle and collect the lantern")
            else:
                player["energy"] -= 2
                print(f"Your energy has decreased to: {player['energy']}")
    elif action == "Visit Old Bridge":
        print("Using Rope will be crucial")
        print("Make sure you have a rope you will loss energy if don't have a rope5")
        if "Rope" in player["inventory"]:
            print("You are eligible to explore")
        else:
            print("You will loss energy")
            
            if answer == "yes":
                print("Go back to Beach and collect the rope")
            else:
                player["energy"] -= 2
                print(f"Your energy has decreased to: {player['energy']}")
        player["bridge_crossed"] == True

    elif action == "Visit Lighthouse":
        player["won"] = True
        player["game_over" = True]
        print("Successfully Arrived and restore the lighthouse beacon")
    elif action == "Check Inventory":
        print("Inventory")
    elif action == "Quit Game":
        print("Goodbye!")
        playing = False
    else:
        print("Invalid Location")



def is_win(player):
    if ("Rope" in player["inventory"] 
        and "Lantern" in player["inventory"]
        and player["energy"] >= 1
        and "Beach" in player["visited_locations"] 
        and "Jungle" in player["visited_locations"]
        and "Cave" in player["visited_locations"] 
        and "Old Bridge" in player["visited_locations"]
        and "Lighthouse" in player["visited_locations"]
        and player["current_location"] == "Lighthouse"
        and player["bridge_crossed"]

    ):
        return True
    else:
        return False

   
    



    
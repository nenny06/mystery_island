def new_game():
    player = {
    "inventory": [],
    "energy": 5,
    "visited_locations": ["Beach"],
    "current_location": "Beach",
    "bridge_crossed": False
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

    # "Beach" in player["visited_locations"] and "Jungle" in player["visited_locations"]
        #and "Cave" in player["visited_locations"] and "Old Bridge" in player["visited_locations"]
        #and "Lighthouse" in player["visited_locations"]:


    



    
print("MYSTERY ISLAND")
print("WELCOME TO THE GAME, HOPE YOU ARE PREPARED")

name = input("What is your name player: ")
print(f"Welcome to Mystery Island, {name}!")


inventory = []
print(f"{name} your inventory is empty")
#inventory.append("Rope")
#inventory.append("Lantern")
print(inventory)

energy = 5
#inventory = ["Rope", "Lantern"]
#if "Rope" in inventory:
    #print("You can cross the bridge!")
#else:
    #energy -= 1
    #print(energy)
    #print("You need a rope to cross!")

#current_location = "Beach"
#print(f"Your current location is: {current_location}")
#current_location = "Jungle"
#print(f"Your current location is: {current_location}")
#current_location = "Cave"
#print(f"Your current location is: {current_location}")

visited_locations = ["Beach"]
current_location = "Beach"


playing = True

while playing:

    print("====== MYSTERY ISLAND ADVENTURE======")


    print("1. Explore Beach")
    print("2. Explore Jungle")
    print("3. Explore Cave")
    print("4. Visit Old Bridge")
    print("5. Visit Lighthouse")
    print("6. Check Inventory")
    print("7. Quit Game")

    choice = input("Choose your Location: ")

    if choice == "1":
        print("Enjoy the sunshine")
        print("There's a Rope here")
        if "Rope" in inventory:
            print("Already have rope in inventory")
        elif "Rope" not in inventory:
            invent = input("Do you want to collect the rope: ")
            invent = invent.lower()
            if invent == "yes":
                inventory.append("Rope")
                print(inventory)
                energy += 2
                print(f"You collected a rope and energy has increased to: {energy}")
        
            else:
                print("Rope not collected")
    elif choice == "2":
        print("Beware of lurking Beast")
        if "Jungle" not in visited_locations:
            visited_locations.append("Jungle")
            current_location = "Jungle"
            energy -= 1
            print(f"You changed to a new location  and remaining energy is: {energy}")
            print(current_location)
        else:
            current_location = "Jungle"
            energy -= 2
            print(f"You want back to a previous location  and remaining energy is: {energy}")
            print(current_location)
            
    elif choice == "3":
        print("Make sure you have a Lantern")
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

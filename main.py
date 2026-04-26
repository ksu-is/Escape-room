# Escape the dorm

# Starting values
current_location = "Dorm Room"
inventory = []
time_left = 5

def start_game():
    print("Welcome to Escape the Dorm!")
    print("Find your keys, backpack, and shoes before time runs out.\n")

def show_location():
    print(f"You are currently in the {current_location}.")

def move():
    global current_location
    print("\nWhere do you want to go?")
    print("1. Hallway")
    print("2. Outside")
    print("3. Dorm Room")
    choice = input("> ")

    if choice == "1":
        current_location = "Hallway"
    elif choice == "2":
        current_location = "Outside"
    elif choice == "3":
        current_location = "Dorm Room"
    else:
        print("Invalid choice.")

def search_room():
    global inventory
    if current_location == "Dorm Room":
        if "keys" not in inventory:
            print("You found your keys!")
            inventory.append("keys")
        else:
            print("Nothing else here.")
    elif current_location == "Hallway":
        if "backpack" not in inventory:
            print("You found your backpack!")
            inventory.append("backpack")
        else:
            print("Nothing else here.")
    elif current_location == "Outside":
        if "shoes" not in inventory:
            print("You found your shoes!")
            inventory.append("shoes")
        else:
            print("Nothing else here.")
    else:
        print("Nothing to find here.")

def countdown():
    global time_left
    time_left -= 1
    print(f"Time left: {time_left}")

    if time_left <= 0:
        print("You ran out of time! Game over.")
        exit()

def game_loop():
    start_game()

    while True:
        show_location()
        print("\nWhat do you want to do?")
        print("1. Move")
        print("2. Search")
        print("3. Check inventory")
        choice = input("> ")

        if choice == "1":
            move()
        elif choice == "2":
            search_room()
        elif choice == "3":
            print("Inventory:", inventory)
        else:
            print("Invalid choice.")

        countdown()

        # Win condition
        if "keys" in inventory and "backpack" in inventory and "shoes" in inventory:
            print("\nYou found everything! You escaped the dorm on time!")
            break

game_loop()


rooms = {
    "lobby": {
        "description": "a dark room. You can see a dim light in from of you about 10 yards. It's a big room, but rather dark for your liking.",
    },
    "bedroom": {
        "description": "it's dingy and messy. You don't want to be in this room...",
    },
    "kitchen": {
        "description": "and directly in front of you is a door to the backyard. Make sure you have your keys though.",
    },
    "backyard": {
        "description": "and you've been locked out. Great job."
    }
}

room_map = {
    "lobby": {"forward": "kitchen", "right": "bedroom"},
    "bedroom": {"back": "lobby"},
    "kitchen": {"back": "lobby", "forward": "backyard"},
    "backyard": {}
}

def show_room(current_room, rooms):
    room_data = rooms[current_room]
    if current_room == "backyard":
        print("You've been locked out! You lose!")
        return False
        
    print(f"You're in the {current_room},", room_data["description"])

    print("Doors:")
    for direction in room_map[current_room]:
        print("-", direction)

def handle_choice(choice, current_room):
    if choice == "exit":
        print("Goodbye!")
    if choice in room_map[current_room]:
        current_room = room_map[current_room][choice]
        return current_room
    else:
        print("[ERROR] Invalid direction!")
        return current_room
    

def inventory():
    print("[ERROR] Inventory not yet implemented")


playing = True
inventory = {}
current_room = "lobby"

while playing:
    result = show_room(current_room, rooms)
    
    if result is False:
        playing = False
        continue

    choice = input("Which direction do you want to go? ").lower()
    if choice == "inventory":
        if inventory:
            print("You have # items in your inventory")
        else:
            print("Your inventory is empty!")
        continue
    current_room = handle_choice(choice, current_room)


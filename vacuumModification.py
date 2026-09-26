room_A = input("Enter status of Room A (Clean/Dirty): ").capitalize()
room_B = input("Enter status of Room B (Clean/Dirty): ").capitalize()
current_room = input("Enter starting room (A/B): ").upper()

rooms = {
    "A": room_A,
    "B": room_B
}

battery = 100

print("\n--- Vacuum Cleaner Agent ---")

while True:

    print("\nCurrent Room:", current_room)
    print("Room A:", rooms["A"])
    print("Room B:", rooms["B"])
    print("Battery:", battery, "%")

    if battery <= 20:
        print("Battery is low!")
        print("Vacuum cleaner stopped.")
        break

    if rooms[current_room] == "Dirty":
        print("Room is dirty.")
        print("Vacuum cleaner is cleaning...")

        rooms[current_room] = "Clean"

        battery -= 20

        print("Room cleaned successfully!")
        print("Battery remaining:", battery, "%")

    else:
        print("Room is already clean.")

    if rooms["A"] == "Clean" and rooms["B"] == "Clean":
        print("\nBoth rooms are clean!")
        print("Vacuum cleaner stopped.")
        break

    if current_room == "A":
        current_room = "B"
    else:
        current_room = "A"

    battery -= 10

    print("Moving to Room", current_room)
    print("Battery remaining:", battery, "%")

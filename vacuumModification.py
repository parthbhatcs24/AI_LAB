import random

room_A = input("Enter status of Room A (Clean/Dirty): ").capitalize()
room_B = input("Enter status of Room B (Clean/Dirty): ").capitalize()
current_room = input("Enter starting room (A/B): ").upper()

rooms = {
    "A": room_A,
    "B": room_B
}

battery = 100
scratched = False

print("\n--- Vacuum Cleaner Agent ---")

while True:

    print("\nCurrent Room:", current_room)
    print("Room A:", rooms["A"])
    print("Room B:", rooms["B"])
    print("Battery:", battery, "%")

    # Simulate wall detection
    wall_detected = random.choice([True, False])

    if wall_detected:
        print(" Wall detected!")

        # Simulate possibility of getting scratched
        scratched = random.choice([True, False])

        if scratched:
            print(" Vacuum hit the wall and got scratched!")
            print(" Vacuum cleaner stopped for safety.")
            break
        else:
            print("Vacuum avoided the wall safely.")

    # Clean the current room
    if rooms[current_room] == "Dirty":
        print("Room is dirty.")
        print("Vacuum cleaner is cleaning...")

        rooms[current_room] = "Clean"
        battery -= 20

        print("Room cleaned successfully!")

    else:
        print("Room is already clean.")

    # Check battery
    if battery <= 20:
        print("Battery is low!")
        print(" Vacuum cleaner stopped.")
        break

    # Check whether both rooms are clean
    if rooms["A"] == "Clean" and rooms["B"] == "Clean":
        print("\n Both rooms are clean!")
        print("Vacuum cleaner stopped.")
        break

    # Move to other room
    if current_room == "A":
        current_room = "B"
    else:
        current_room = "A"

    print("Moving to Room", current_room)

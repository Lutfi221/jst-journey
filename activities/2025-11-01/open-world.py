
player_hand = ""
player_location = "backpack"

while True:
    if player_location == "backpack":
        print("You're at your backpack")
        ans = input("Do you want to pick up a lockpick (y/n)")

    if player_location == "shack":
        print("You're at a shack")

    if player_location == "cave":
        print("You're at a cave")

    print("Where do you want to go?")
    print("1. backpack, 2. shack, 3. cave")

    location_input = input(" > ")

    if int(location_input) == 1:
        player_location = "backpack"

    if int(location_input) == 2:
        if player_hand == "lockpick":
            player_location = "shack"
        else:
            print("You need a lockpick to enter the shack")

    if int(location_input) == 3:
        player_location = "cave"

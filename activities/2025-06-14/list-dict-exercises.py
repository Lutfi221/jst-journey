
divider = "\n" + "-" * 12

weapon_names = ["Spear", "Mjolnir", "Sword"]
weapon_strengths = [4, 10, 7]
weapon_durabilities = [20, 50, 25]

n_weapon_names = len(weapon_names)

print("# Iterating over weapon names, durabilities, and strengths using `for ... in range(...)")
for i in range(n_weapon_names):
    no = i + 1
    weapon_strength = weapon_strengths[i]
    weapon_name = weapon_names[i]
    weapon_durability = weapon_durabilities[i]
    print(str(no) + ". " + weapon_name + " (durability: " + str(weapon_durability) + ", strength: " + str(weapon_strength) + ")")

weapons = []

spear = {
    "name": "Spear",
    "durability": 20,
    "strength": 4,
}

weapons.append(spear)

mjolnir = {
    "name": "Mjolnir",
    "durability": 50,
    "strength": 25,
}

weapons.append(mjolnir)

sword = {
    "name": "Sword",
    "durability": 25,
    "strength": 7,
}

weapons.append(sword)

print(divider)

print("# Combining the power of lists and dictionaries:")

print(weapons)

print(divider)

print("# Iterating over weapons using `for ... in weapons` loop:")

for weapon in weapons:
    weapon_name = weapon["name"]
    weapon_durability = weapon["durability"]
    weapon_strength = weapon["strength"]
    print("name: " + weapon_name)
    print("durability: " + str(weapon_durability))
    print("strength: " + str(weapon_strength))
    print()

print(divider)

n_weapons = len(weapons)

print("# Iterating over weapons using `for ... in range(...)` loop:")

for i in range(n_weapons):
    no = i + 1
    weapon = weapons[i]
    weapon_name = weapon["name"]
    weapon_durability = weapon["durability"]
    weapon_strength = weapon["strength"]
    print(str(no) + ". " + weapon_name + " (durability: " + str(weapon_durability) + ", strength: " + str(weapon_strength) + ")")

print(divider)

print("# Defining a function to show all our weapons")

def print_weapons(weapons):
    n_weapons = len(weapons)
    for i in range(n_weapons):
        no = i + 1
        weapon = weapons[i]
        weapon_name = weapon["name"]
        weapon_durability = weapon["durability"]
        weapon_strength = weapon["strength"]
        print(str(no) + ". " + weapon_name + " (durability: " + str(weapon_durability) + ", strength: " + str(weapon_strength) + ")")

print_weapons(weapons)

print(divider)

print("# Making all the weapons ten times stronger using `for ... in weapons`")

for weapon in weapons:
    weapon["strength"] = weapon["strength"] * 10

print_weapons(weapons)

print(divider)

print("# Making all our weapons twice as durable using `for ... in range(...)`")

n_weapons = len(weapons)

for i in range(n_weapons):
    weapon = weapons[i]
    weapon["durability"] = weapon["durability"] * 2

print_weapons(weapons)

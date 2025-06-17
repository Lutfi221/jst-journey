
divider = "\n" + "-" * 12

weapon_names = ["Spear", "Mjolnir", "Sword"]
weapon_strengths = [4, 10, 7]

n_weapons = len(weapon_names)
print("number of weapons: " + str(n_weapons))

print("weapon names: " + str(weapon_names))

print("weapon strengths: " + str(weapon_strengths))

first_weapon_name = weapon_names[0]
second_weapon_name = weapon_names[1]

print(divider)
print("first weapon name: " + first_weapon_name)
print("second weapon name: " + second_weapon_name)

first_weapon_strength = weapon_strengths[0]
second_weapon_strength = weapon_strengths[1]

print("first weapon strength: " + str(first_weapon_strength))
print("second weapon strength: " + str(second_weapon_strength))

print(divider)

print("# Iterating over weapon names using `for ... in weapon_names` loop:")

for weapon_name in weapon_names:
    print(weapon_name)

print(divider)

print("# Iterating over weapon names using `for ... in range(...)` loop:")

n_weapon_names = len(weapon_names)

for i in range(n_weapon_names):
    no = i + 1
    weapon_name = weapon_names[i]
    print(str(no) + ". " + weapon_name)

print(divider)

print("# Iterating over weapon strengths using `for ... in weapon_strengths` loop:")

for weapon_strength in weapon_strengths:
    print(weapon_strength)

print(divider)

print("# Iterating over weapon strengths using `for ... in range(...)` loop:")

n_weapon_strengths = len(weapon_strengths)

for i in range(n_weapon_strengths):
    no = i + 1
    weapon_strength = weapon_strengths[i]
    print(str(no) + ". " + str(weapon_strength))

print(divider)

print("# Iterating over both weapon names and strengths using `for ... in range(...)` loop:")

n_weapons = len(weapon_names)

for i in range(n_weapons):
    no = i + 1
    weapon_name = weapon_names[i]
    weapon_strength = weapon_strengths[i]
    print(str(no) + ". " + weapon_name + " (" + str(weapon_strength) + ")")

print(divider)

weapon_durabilities = [20, 50, 25]

print("weapon durabilities: " + str(weapon_durabilities))

print(divider)

print("# Iterating over weapon durabilities using `for ... in weapon_durabilities` loop:")

for weapon_durability in weapon_durabilities:
    print(weapon_durability)

print(divider)

print("# Iterating over weapon durabilities using `for ... in range(...)` loop:")

n_weapon_durabilities = len(weapon_durabilities)

for i in range(n_weapon_durabilities):
    no = i + 1
    weapon_durability = weapon_durabilities[i]
    print(str(no) + ". " + str(weapon_durability))

print(divider)

print("# Iterating over weapon names, durabilities, and strengths using `for ... in range(...)")
for i in range(n_weapon_durabilities):
    no = i + 1
    weapon_strength = weapon_strengths[i]
    weapon_name = weapon_names[i]
    weapon_durability = weapon_durabilities[i]
    print(str(no) + ". " + weapon_name + " (durability: " + str(weapon_durability) + ", strength: " + str(weapon_strength) + ")")

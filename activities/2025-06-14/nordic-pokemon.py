import random


is_hero_automated = True
is_villain_automated = True

print("Welcome to Nordic Pokemon!")

hero_automation_choice = input("Do you want the hero be played by computer? (y/n) ")
villain_automation_choice = input(
    "Do you want the villain be played by computer? (y/n) "
)

if hero_automation_choice == "y":
    is_hero_automated = True
else:
    is_hero_automated = False

# Alternative way to do the same thing
is_villain_automated = villain_automation_choice == "y"

hero = {
    "name": "Thor",
    "health": 90,
    "weapon": "Fists",
    "weapon_strength": 2,
}

print(
    """Hero weapons:

1. Spear (4)
2. Mjolnir (10)
3. Sword (7)

Choose 1-3:"""
)

hero_weapon_choice = int(input(" > "))

if hero_weapon_choice == 1:
    hero["weapon"] = "Spear"
    hero["weapon_strength"] = 4
elif hero_weapon_choice == 2:
    hero["weapon"] = "Mjolnir"
    hero["weapon_strength"] = 10
elif hero_weapon_choice == 3:
    hero["weapon"] = "Sword"
    hero["weapon_strength"] = 7

villain = {
    "name": "Loki",
    "health": 80,
    "weapon": "Fists",
    "weapon_strength": 1,
}

print(
    """Villain weapons:

1. Halbur (10)
2. Scepter (8)
3. Axe (6)

Choose 1-3:"""
)

villain_weapon_choice = int(input(" > "))

if villain_weapon_choice == 1:
    villain["weapon"] = "Halbur"
    villain["weapon_strength"] = 10
elif villain_weapon_choice == 2:
    villain["weapon"] = "Scepter"
    villain["weapon_strength"] = 8
elif villain_weapon_choice == 3:
    villain["weapon"] = "Axe"
    villain["weapon_strength"] = 6

print("The battle begins!")


def calculate_attack_multiplier(attack_style):
    if attack_style == 1:
        return random.randint(3, 6)
    else:
        return random.randint(1, 3)


def print_health_bars(hero_health, villain_health):
    hero_bar = "#" * hero_health
    villain_bar = "#" * villain_health
    print("HERO    : " + hero_bar)
    print("VILLAIN : " + villain_bar)


while True:
    if is_hero_automated:
        hero_attack_style = random.randint(1, 3)
    else:
        print("Hero attack styles:")
        print("1. Heavy")
        print("2. Light")
        hero_attack_style = int(input("Choose hero attack style (1-2): "))

    hero_attack_multiplier = calculate_attack_multiplier(hero_attack_style)

    print(
        f"Hero {hero['name']} deals {hero['weapon_strength'] * hero_attack_multiplier} damage"
    )

    villain["health"] = (
        villain["health"] - hero_attack_multiplier * hero["weapon_strength"]
    )

    if is_villain_automated:
        villain_attack_style = random.randint(1, 3)
    else:
        print("Villain attack styles:")
        print("1. Heavy")
        print("2. Light")
        villain_attack_style = int(input("Choose villain attack style (1-2): "))

    villain_attack_multiplier = calculate_attack_multiplier(villain_attack_style)

    hero["health"] = (
        hero["health"] - villain_attack_multiplier * villain["weapon_strength"]
    )

    print(
        f"Villain {villain['name']} deals {villain['weapon_strength'] * villain_attack_multiplier} damage"
    )

    print_health_bars(hero["health"], villain["health"])

    if hero["health"] <= 0:
        print(f"Hero {hero['name']} is dead!")
        break
    if villain["health"] <= 0:
        print(f"Villain {villain['name']} is dead!")
        break

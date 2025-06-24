import time
import random

print("Welcome to Nordic Pokemon!")

hero_automation_choice = input("Do you want the hero be played by computer? (y/n) ")
villain_automation_choice = input(
    "Do you want the villain be played by computer? (y/n) "
)

if hero_automation_choice == "y":
    is_hero_automated = True
else:
    is_hero_automated = False
is_villain_automated = villain_automation_choice == "y"
hero = {
    "name": "Thor",
    "weapon": "",
    "weapon_strength": 0,
    "health": 80,
}
print(
    """Hero weapons:

1. Spear (4)
2. Mjolnir (10)
3. Sword (7)
etc. Barehanded"""
)
time.sleep(0.5)
hero_wc = int(input("Choose, 1, 2, 3, or etc: "))
if hero_wc == 1:
    hero["weapon"] = "Spear"
    hero["weapon_strength"] = 4
elif hero_wc == 2:
    hero["weapon"] = "Mjolnir"
    hero["weapon_strength"] = 10
elif hero_wc == 3:
    hero["weapon"] = "Sword"
    hero["weapon_strength"] = 7
else:
    hero["weapon"] = "Mr & mrs knuckles"
    hero["weapon_strength"] = 0
time.sleep(1)
print(hero)
time.sleep(2)

villain = {
    "name": "Loki",
    "weapon": "",
    "weapon_strength": 0,
    "health": 70,
}
print(
    """villain weapons:

1. Halberd (10)
2. Scepter (8)
3. Axe (6)
etc. Barehanded"""
)
time.sleep(0.5)
villain_wc = int(input("Choose, 1, 2, 3, or etc: "))
if villain_wc == 1:
    villain["weapon"] = "Halberd"
    villain["weapon_strength"] = 4
elif villain_wc == 2:
    villain["weapon"] = "Scepter"
    villain["weapon_strength"] = 8
elif villain_wc == 3:
    villain["weapon"] = "Axe"
    villain["weapon_strength"] = 6
else:
    villain["weapon"] = "Presditigitation"
    villain["weapon_strength"] = 0
time.sleep(1)
print(villain)
time.sleep(2)


def calculate_attack_multiplier(attack_style):
    if attack_style == 1:
        return random.randint(3, 6)
    else:
        return random.randint(1, 3)


print("Commencing battle...")
time.sleep(5)
while True:
    if is_hero_automated:
        hero_attack_style = random.randint(1, 3)
    else:
        print("Hero attack styles:")
        print("1. Heavy")
        print("2. Light")
        hero_attack_style = int(input("Choose hero attack style (1-2): "))

    hero_attack_multiplier = calculate_attack_multiplier(hero_attack_style)

    print("Thor attacks Loki with " + hero["weapon"] + ".")
    time.sleep(2)
    villain["health"] = villain["health"] - hero["weapon_strength"]
    print("Loki takes damage from Thor.")
    time.sleep(2)
    if is_villain_automated:
        villain_attack_style = random.randint(1, 3)
    else:
        print("Villain attack styles:")
        print("1. Heavy")
        print("2. Light")
        villain_attack_style = int(input("Choose villain attack style (1-2): "))

    villain_attack_multiplier = calculate_attack_multiplier(villain_attack_style)
    print("Loki attacks Thor with " + villain["weapon"] + ".")
    time.sleep(2)
    hero["health"] = hero["health"] - villain["weapon_strength"]
    print("Thor takes damage from Loki.")

    # <<<<

    # if hero["health"] > villain["health"]:
    #     print('Thor says: I have the high ground, Loki.')
    #     time.sleep(2)
    #     if hero["health"] == 0:
    #         print('Thor says: You either live long enough to see yourself become the villain, or die a hero.')
    #         time.sleep(2)
    #     elif hero["health"] < 0:
    #         print('Thor Dies.')
    #         time.sleep(2)
    #         break
    # elif villain["health"] < hero["health"]:
    #     print('Loki says: I have the high ground, Thor')
    #     time.sleep(1)
    #     if villain["health"] == 0:
    #         print('Loki says: See you in Hel, Thor')
    #         time.sleep(1)
    #     elif villain["health"] < 0:
    #         print('Loki Dies.')
    #         time.sleep(1)
    #         break

    # ====

    hero_has_high_ground = hero["health"] > villain["health"]

    if hero_has_high_ground:
        print(f"Thor says: I have the high ground, Loki.")
    else:
        print(f"Loki says: I have the high ground, Thor.")

    if hero["health"] <= 0:
        print("Loki says: See you in Hel, Thor")
        time.sleep(1)
        print("Thor dies!")
        break
    if villain["health"] <= 0:
        print("Thor says: You either live long enough to see yourself become the villain, or die a hero.")
        time.sleep(1)
        print("Loki dies!")
        break

    # >>>>>

    print("Current health of Loki: " + "#" * villain["health"])
    time.sleep(1)
    print("Current health of Thor: " + "#" * hero["health"])
    time.sleep(1)

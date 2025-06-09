from time import sleep


def introduce_character(character):
    print("Meet " + character["name"] + ".")
    sleep(1)
    print("He carries a " + character["weapon"] + ".")
    sleep(1)
    print("It has a strength of " + str(character["weapon_strength"]) + ".")
    sleep(1)
    print("He has " + str(character["health"]) + " health.")
    sleep(1)
    print()
    
def show_health(character):
    print(character["name"] + ": " + "#" * character["health"])

question_prefix = "What is the main character's"

hero = {}

hero["name"] = input(question_prefix + " name? ")
hero["weapon"] = input(question_prefix + " weapon? ")
hero["weapon_strength"] = int(input(question_prefix + " weapon strength? "))
hero["health"] = int(input(question_prefix + " health? (0-100) "))

question_prefix = "What is the villain's"

villain = {}

villain["name"] = input(question_prefix + " name? ")
villain["weapon"] = input(question_prefix + " weapon? ")
villain["weapon_strength"] = int(input(question_prefix + " weapon strength? "))
villain["health"] = int(input(question_prefix + " health? (0-100) "))

introduce_character(hero)
introduce_character(villain)

print("The battle begins!")

while True:
    # Hero attacks villain
    villain["health"] = villain["health"] - hero["weapon_strength"]
    print(hero["name"] + " attacks " + villain["name"] + "!")
    show_health(villain)
    sleep(1)
    
    if villain["health"] <= 0:
        print(villain["name"] + " is dead!")
        break
    
    # Villain attacks hero
    hero["health"] = hero["health"] - villain["weapon_strength"]
    print(villain["name"] + " attacks " + hero["name"] + "!")
    show_health(hero)
    sleep(1)
    
    if hero["health"] <= 0:
        print(hero["name"] + " is dead!")
        break

print("The battle is over!")

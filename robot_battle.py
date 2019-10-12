
ovitality = 100
evitality = 0
enemydmg = 0
name_enemy = "Nobody"

chosen_enemy = input("Against who do you want to fight? (Roger / Ernesto / Luca): ").upper()

if chosen_enemy == "ROGER":
    name_enemy = "Roger"
    evitality = 90
    enemydmg = 8

elif chosen_enemy == "ERNESTO":
    name_enemy = "Ernesto"
    evitality = 75
    enemydmg = 5

elif chosen_enemy == "LUCA":
    name_enemy = "Luca"
    evitality = 80
    enemydmg = 10

while ovitality > 0 and evitality > 0:

    attack = input("Which attack do you want to use? (Use Hammer / Use Saw): ").upper()

    if attack == "USE HAMMER":
        evitality -= 10
        print("You deal 10 points of damage to {}, his current vitality is: {}".format(name_enemy, evitality))

    elif attack == "USE SAW":
        evitality -= 15
        print("You deal 15 points of damage to {}, his current vitality is: {}".format(name_enemy, evitality))

    elif attack != "USE HAMMER" and "USE SAW":
        print("Your robot doest understand you, so he does nothing")
    ovitality -= enemydmg
    print("{} deal to you {} points of damage, your current vitality is: {}".format(name_enemy, enemydmg, ovitality))

if ovitality > 0 and evitality <= 0:
    print("You win")

elif ovitality <= 0 and evitality > 0:
    print("You lose")
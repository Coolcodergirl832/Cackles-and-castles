import random

while True:
    player_name = input("What is your name, traveler? ")
    player_health = 100
    
    def monster_dice_roll():
        monster_dice = random.randint(1, 6)
        if monster_dice == 1:
            monster_type = "witch"
            monster_health = 30
            attack_dice = random.randint(1,2)
            if attack_dice == 1:
                monster_attack = "potion"
                monster_attack_dmg = 15
            elif attack_dice == 2:
                monster_attack = "heal" 
                monster_attack_dmg = 0
        elif monster_dice == 2:
            monster_type = "gobilin"
            monster_health = 20
            attack_dice = random.randint(1,2)
            if attack_dice == 1:
                monster_attack = "kick"
                monster_attack_dmg = 5
            elif attack_dice == 2:
                monster_attack = "stab" 
                monster_attack_dmg = 10
        elif monster_dice == 3:
            monster_type = "midusa"
            monster_health = 80
            attack_dice = random.randint(1,2)
            if attack_dice == 1:
                monster_attack = "bite"
                monster_attack_dmg = 5
            elif attack_dice == 2:
                monster_attack = "parilize" 
                monster_attack_dmg = 10
        elif monster_dice == 4:
            monster_type = "minitar"
            monster_health = 30
            attack_dice = random.randint(1,2)
            if attack_dice == 1:
                monster_attack = "horse kick"
                monster_attack_dmg = 5
            elif attack_dice == 2:
                monster_attack = "charge" 
                monster_attack_dmg = 10
        elif monster_dice == 5:
            monster_type = "cyeribis"
            monster_health = 40
            attack_dice = random.randint(1,2)
            if attack_dice == 1:
                monster_attack = "triple bite"
                monster_attack_dmg = random.randint(1,15)
            elif attack_dice == 2:
                monster_attack = "bite" 
                monster_attack_dmg = 10
        elif monster_dice == 6:
            monster_type = "zombie"
            monster_health = 10
            attack_dice = random.randint(1,2)
            if attack_dice == 1:
                monster_attack = "bite"
                monster_attack_dmg = 5
            elif attack_dice == 2:
                monster_attack = "hit" 
                monster_attack_dmg = 10
        
        return (monster_type,monster_health,monster_attack,monster_attack_dmg)
    
    def Chosse_spices():
        player_spices = input("What is your species type? (a) troll, (b) org, (c) vampire, (d) human: ")
        if player_spices.lower() == 'a':
            print("You have chosen to be a troll, you are strong but slow.")
            attacks = ["club smash", "ground pound", "troll roar"]
            dmg1, dmg2, dmg3 = 10, 15, 5
            spices = "troll"
        elif player_spices.lower() == 'b':
            print("You have chosen to be an org, you are fierce and powerful but not very smart.")
            attacks = ["smash", "roar", "charge"]
            dmg1, dmg2, dmg3 = 5, 10, 15
            spices = "org"
        elif player_spices.lower() == 'c':
            print("You have chosen to be a vampire, you are fast and durable but are hackable.")
            attacks = ["shriek", "bite", "cyber attack"]
            dmg1, dmg2, dmg3 = 15, 5, 10
            spices = "vampire"
        elif player_spices.lower() == 'd':
            print("You have chosen to be a human, you are balanced and versatile but not durable.")
            attacks = ["slash", "stab", "punch"]
            dmg1, dmg2, dmg3 = 10, 15, 5
            spices = "human"
        else:
            print("Invalid choice! spices has been set to human by default.")
            attacks = ["slash", "stab", "punch"]
            dmg1, dmg2, dmg3 = 10, 15, 5
            spices = "human"
        
        # Return all 5 values as a tuple
        return (spices, attacks, dmg1, dmg2, dmg3)

    choice = input(f"Welcome {player_name}, you have been chosen to be the hero of this world. Do you accept? (y/n) ")
    
    if choice.lower() == 'y':
        # FIX: We must "unpack" the 5 things the function returns into 5 variables
        player_spices, current_attacks, attack1_dmg, attack2_dmg, attack3_dmg = Chosse_spices()

        print(f"Great! {player_name} the {player_spices}, your adventure begins now.")
        
        input("""How this game will work: when you defeat a monster you gain skill points...
              (Press Enter to continue)""")
        
        choice = input("Are you ready to start your adventure? (y/n) ")
        if choice.lower() == 'y':
            print("Let's begin!")
            
            # Start the game loop here
            while True:
                player_spices

    elif choice.lower() == 'n':
        print("Perhaps another time.")
        break
    else:
        print("Please enter 'y' or 'n'.")

import random
def the_second_game():
    def Choose_species():
        player_health = 100
        player_species = input("What is your species type? (a) troll, (b) orc, (c) vampire, (d) human: ")
        if player_species.lower() == 'a':
            print("You have chosen to be a troll, you are strong but slow.")
            attacks = ["club smash", "ground pound", "troll roar"]
            dmg1, dmg2, dmg3 = 10, 15, 5
            species = "troll"
        elif player_species.lower() == 'b':
            print("You have chosen to be an orc, you are fierce and powerful but not very smart.")
            attacks = ["smash", "roar", "charge"]
            dmg1, dmg2, dmg3 = 5, 10, 15
            species = "orc"
        elif player_species.lower() == 'c':
            print("You have chosen to be a vampire, you are fast and durable but are vulnerable to sunlight.")
            attacks = ["shriek", "bite", "blood drain"]
            dmg1, dmg2, dmg3 = 15, 5, 10
            species = "vampire"
        elif player_species.lower() == 'd':
            print("You have chosen to be a human, you are balanced and versatile but not durable.")
            attacks = ["slash", "stab", "punch"]
            dmg1, dmg2, dmg3 = 10, 15, 5
            species = "human"
        else:
            print("Invalid choice! species has been set to human by default.")
            attacks = ["slash", "stab", "punch"]
            dmg1, dmg2, dmg3 = 10, 15, 5
            species = "human"
        
        # Return all 5 values as a tuple
        return (species, attacks, dmg1, dmg2, dmg3)
    def new_monster_generator():
        dice = random.randint(1,12)
        if dice == 1:
            monster = "skellaten"
            attck_dice = random.randint(1,2)
            if attck_dice == 1:
                monster_attack = "arrow_shot"
                monster_attack_dmg = 5
            elif attck_dice == 2:
                monster_attack = "call for backup" 
                monster_attack_dmg = 0

        if dice == 2:
            monster = "mummy"
            attck_dice = random.randint(1,2)
            if attck_dice == 1:
                monster_attack = "bite"
                monster_attack_dmg = 5
            elif attck_dice == 2:
                monster_attack = "drain life" 
                monster_attack_dmg = 10

        if dice == 3:
            monster = "werewolf"
            attck_dice = random.randint(1,2)
            if attck_dice == 1:
                monster_attack = "claw swipe"
                monster_attack_dmg = 5
            elif attck_dice == 2:
                monster_attack = "howl" 
                monster_attack_dmg = 0
        if dice == 4:
            monster = "gargoyal"
            attck_dice = random.randint(1,2)
            if attck_dice == 1:
                monster_attack = "stone throw"
                monster_attack_dmg = 5
            elif attck_dice == 2:
                monster_attack = "petrify" 
                monster_attack_dmg = 10

        if dice == 5:
            monster = "Huldra"
            attck_dice = random.randint(1,2)
            if attck_dice == 1:
                monster_attack = "charm"
                monster_attack_dmg = 0
            elif attck_dice == 2:
                monster_attack = "claw swipe" 
                monster_attack_dmg = 5
        if dice == 6:
            monster = "Liche"
            attck_dice = random.randint(1,2)
            if attck_dice == 1:
                monster_attack = "dark magic"
                monster_attack_dmg = 10
            elif attck_dice == 2:
                monster_attack = "drain life" 
                monster_attack_dmg = 5
        if dice == 7:
            monster = "Gremlins"
            attck_dice = random.randint(1,2)
            if attck_dice == 1:
                monster_attack = "sabotage"
                monster_attack_dmg = 0
            elif attck_dice == 2:
                monster_attack = "bite" 
                monster_attack_dmg = 5
        if dice == 8:
            monster = "Wraiths"
            attck_dice = random.randint(1,2)
            if attck_dice == 1:
                monster_attack = "drain life"
                monster_attack_dmg = 10
            elif attck_dice == 2:
                monster_attack = "hit" 
                monster_attack_dmg = 5
        if dice == 9:
            monster = "Ghoul"
            attck_dice = random.randint(1,2)
            if attck_dice == 1:
                monster_attack = "bite"
                monster_attack_dmg = 5
            elif attck_dice == 2:
                monster_attack = "hit" 
                monster_attack_dmg = 10
        if dice == 10:
            monster = "Revenants"
            attck_dice = random.randint(1,2)
            if attck_dice == 1:
                monster_attack = "bite"
                monster_attack_dmg = 5
            elif attck_dice == 2:
                monster_attack = "hit" 
                monster_attack_dmg = 10
        if dice == 11:
            monster = "Cyclops"
            attck_dice = random.randint(1,2)
            if attck_dice == 1:
                monster_attack = "bite"
                monster_attack_dmg = 5
            elif attck_dice == 2:
                monster_attack = "hit" 
                monster_attack_dmg = 10
        if dice == 12:
            monster = "Yeti"
            attck_dice = random.randint(1,2)
            if attck_dice == 1:
                monster_attack = "bite"
                monster_attack_dmg = 5
            monster_dice = random.randint(1, 6)
            if monster_dice == 13:
                monster_type = "witch"
                monster_health = random.randint(10,50)
                attack_dice = random.randint(1,2)
                if attack_dice == 1:
                    monster_attack = "potion"
                    monster_attack_dmg = 15
                elif attack_dice == 2:
                    monster_attack = "heal" 
                    monster_attack_dmg = 0
            elif monster_dice == 14:
                monster_type = "goblin"
                monster_health = random.randint(10,50)
                attack_dice = random.randint(1,2)
                if attack_dice == 1:
                    monster_attack = "kick"
                    monster_attack_dmg = 5
                elif attack_dice == 2:
                    monster_attack = "stab" 
                    monster_attack_dmg = 10
            elif monster_dice == 15:
                monster_type = "medusa"
                monster_health = random.randint(10,50)
                attack_dice = random.randint(1,2)
                if attack_dice == 1:
                    monster_attack = "bite"
                    monster_attack_dmg = 5
                elif attack_dice == 2:
                    monster_attack = "paralyze" 
                    monster_attack_dmg = 10
            elif monster_dice == 16:
                monster_type = "minotaur"
                monster_health = random.randint(10,50)
                attack_dice = random.randint(1,2)
                if attack_dice == 1:
                    monster_attack = "horse kick"
                    monster_attack_dmg = 5
                elif attack_dice == 2:
                    monster_attack = "charge" 
                    monster_attack_dmg = 10
            elif monster_dice == 17:
                monster_type = "cerberus"
                monster_health = random.randint(10,50)
                attack_dice = random.randint(1,2)
                if attack_dice == 1:
                    monster_attack = "triple bite"
                    monster_attack_dmg = random.randint(1,15)
                elif attack_dice == 2:
                    monster_attack = "bite" 
                    monster_attack_dmg = 10
            elif monster_dice == 18:
                monster_type = "zombie"
                monster_health = random.randint(10,50)
                attack_dice = random.randint(1,2)
                if attack_dice == 1:
                    monster_attack = "bite"
                    monster_attack_dmg = 5
                elif attack_dice == 2:
                    monster_attack = "hit" 
                    monster_attack_dmg = 10
            
            return (monster_type,monster_health,monster_attack,monster_attack_dmg)
            
    choice = input("welcom back travler our world is in distress agein and you will be the one to save it do you accept this quest (y/n)")
    if choice.lower() == "y":
        print("you are a brave hero saving us again")


    elif choice.lower() == "n":
        print("you are a coward!")

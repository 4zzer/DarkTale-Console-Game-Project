import os
import time
import getpass
import random
import keyboard

# Clear terminal
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear') # To avoid error in windows and linux. 'cls' for windows and 'clear' for linux. if os.name is nt(windoww) then cls, else clear

#Title using ASCII art
def show_title():
    title = """
      ██████╗   █████╗ ██████╗  ██╗  ██╗ ████████╗ █████╗ ██╗     ███████╗
      ██╔══██╗ ██╔══██╗██╔══██╗ ██║ ██╔╝ ╚══██╔══╝██╔══██╗██║     ██╔════╝
      ██║  ██║ ███████║██████╔╝ █████╔╝     ██║   ███████║██║     █████╗  
      ██║  ██║ ██╔══██║██╔══██╗ ██╔═██╗     ██║   ██╔══██║██║     ██╔══╝  
      ██████╔╝ ██║  ██║██║  ██║ ██║  ██╗    ██║   ██║  ██║███████╗███████╗
      ╚═════╝  ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═╝  ╚═╝    ╚═╝   ╚═╝  ╚═╝╚══════╝╚══════╝
    """
    print(title)

# Main menu function
def main_menu():
    while True:
        clear_terminal()
        show_title()
        print("="*79)
        print(" ")
        print("                              1. New Game")
        print("                              2. How to Play")
        print("                              3. Exit")
        print("\n" + "="*79)
        choice = input("> ")

        if choice == "1":
            break
        elif choice == "2":
            clear_terminal()
            guide()
        elif choice == "3":
            clear_terminal()
            print("Exiting program...")
            exit()
        else:
            clear_terminal()
            main_menu()

# Guide function
def guide():
    show_title()
    print("="*79)
    print("\nHow to Play:")
    print("Press W, A, S, D to move.\n")
    print("On the map:")
    print("  P - Player")
    print("  I - Item")
    print("  0 - Wall")
    print("  E - Enemy")
    print("  B - Boss")
    print(" ")
    getpass.getpass("Press any key to return...") # getpass.getpass() is used to pause the program until the user presses the Enter key.
    print("\n" + "="*79)

# Note function
def note():
    clear_terminal()
    print("Note:")
    print("="*79)
    print("You can move using W, A, S, D keys without pressing enter.")
    print("This is a turn-based game. You can only move once per turn.")
    print("You cant spam to attack, otherwise you will die quickly.")
    print("You have to think carefully on your choices to survive")
    print("Good luck!")
    getpass.getpass("Press enter to start...")

# Prologue function
def slow_print(text, delay=0.04, end_char=""): # delay is the speed of the text
    for char in text: # loop through each character in the text
        print(char, end="", flush=True) # print the character without waiting for a newline
        time.sleep(delay) # wait for the delay
    print(end=end_char, flush=True) 

def prolouge():
    global player_name # Make player_name a global variable so it can be accessed outside the function
    clear_terminal()
    print("Prologue: The Cursed Forest")  
    print("="*79)

    # First part
    time.sleep(0.5) # delay for ("number") seconds
    slow_print("In a world where despair and darkness cloud your every thought, ")
    time.sleep(0.7)
    slow_print('you find yourself at a breaking point.\n') # \n for new line because slow_print doesn't automatically add a new line
    time.sleep(1)
    slow_print("You hear whispers of a cursed forest, ")
    time.sleep(0.7)
    slow_print('a place where no one who enters ever returns.\n')
    time.sleep(1)
    slow_print("Seeking an escape from the pain, ")
    time.sleep(0.7)
    slow_print('you decide to venture into this forbidden forest')
    time.sleep(0.7)
    slow_print('.')
    time.sleep(0.7) 
    slow_print('.')
    time.sleep(0.7)
    slow_print('.')
    
    time.sleep(2)

    slow_print("\n\nYou walk through the forest, the sun setting behind you.\n")
    time.sleep(1)
    slow_print("The air grows colder, and the trees seem to close in as night falls.\n")
    time.sleep(1)
    slow_print("You push forward, determined to let nature decide your fate.\n")
    time.sleep(1)
    slow_print("Suddenly, the ground gives way beneath your feet!\n")
    time.sleep(1)
    slow_print("You fall endlessly into the darkness, screaming")
    time.sleep(0.7)
    slow_print('.')
    time.sleep(0.7)
    slow_print('.')
    time.sleep(0.7)
    slow_print('.')
    slow_print(" the fear overwhelming you.\n")
    time.sleep(1)
    slow_print("As you fall, your senses blur, and a memory begins to form")
    time.sleep(0.7)
    slow_print('.')
    time.sleep(0.7)
    slow_print('.')
    time.sleep(0.7)
    slow_print('.\n')
    time.sleep(1)

    # Get player name using loop to ensure the name is not empty or just spaces
    while True:
        player_name = input("\nBefore everything fades, what is your name? > ")

        if player_name.strip(): # Check if the name is not empty or just spaces
            break
        else:
            clear_terminal()
            print("Error: Invalid name.")
            print("="*79)
            print("Please enter a valid name (cannot be empty or just spaces).")
        
    # Second part
    clear_terminal()
    print("Prologue: The Past")
    print("="*79)

    time.sleep(0.5)
    slow_print("You were a child once, lost and frightened in a forest.\n")
    time.sleep(1)
    slow_print("Sitting beneath a tree, tears streaming down your face.\n")
    time.sleep(1)
    slow_print("Out of nowhere,")
    time.sleep(0.7)
    slow_print(" a girl about your age approached.\n")
    time.sleep(1)
    slow_print("She looked at you kindly and said, ")
    time.sleep(0.5)
    slow_print("\"Hey, are you okay?\"\n")
    time.sleep(1)
    slow_print("You couldn’t respond, frozen in fear.\n")
    time.sleep(1)
    slow_print("She smiled and asked again, ")
    time.sleep(0.5)
    slow_print("\"What’s your name?\"\n")
    time.sleep(1)
    slow_print("Still unable to speak, you shook your head, clutching your shirt.\n")
    time.sleep(1)
    slow_print(f"\"Alright, I’ll call you '\'{player_name}\'' for now.\"")
    time.sleep(0.5)
    slow_print(" while smiling.\n\n")

    time.sleep(2)

    slow_print("She stayed with you, calming you down.\n")
    time.sleep(1)
    slow_print("With her help, you stood and followed her through the forest.\n")
    time.sleep(1)
    slow_print("She spoke of hope and strength, of a world beyond the trees.\n")
    time.sleep(1)
    slow_print("As you neared the edge of the forest, she stopped.\n")
    time.sleep(1)
    slow_print("\"You’ll be okay from here,\" she said,")
    time.sleep(0.5)
    slow_print(" pointing down the path.\n")
    time.sleep(1)
    slow_print("\"Aren’t you coming with me?\" you asked.\n")
    time.sleep(1)
    slow_print("She shook her head, her smile turning bittersweet.\n")
    time.sleep(1)
    slow_print("\"I can't. There’s something I still have to do.\"\n")
    time.sleep(1)
    slow_print("You hesitated, and walked towards the exit.\n")
    time.sleep(1)
    slow_print("Before you left, you asked her name.\n")
    time.sleep(1)
    slow_print("Her lips moved, but no sound came out.\n")
    time.sleep(1)
    slow_print("The memory began to fade, and you fell once more")
    time.sleep(0.7)
    slow_print('.')
    time.sleep(0.7)
    slow_print('.')
    time.sleep(0.7)
    slow_print('.\n\n')

    getpass.getpass("Press enter to continue...")

    # Third part
    clear_terminal()
    print("Prologue: The Awakening")
    print("="*79)

    time.sleep(0.5)
    slow_print("You jolt awake, gasping for air. Pain radiates through your body.\n")
    time.sleep(1)
    slow_print("You’re lying on cold, damp stone")
    time.sleep(0.7)
    slow_print(", the faint sound of dripping water breaking the silence.\n")
    time.sleep(1)
    slow_print("It’s a dark, foreboding cave.\n")
    time.sleep(1)
    slow_print("A faint light filters through a hole far above, marking where you fell.\n")
    time.sleep(1)
    slow_print("The climb back is impossible.\n\n")

    time.sleep(2)

    slow_print("That memory-the girl, her voice, the nickname-lingers at the edge of your thoughts.\n")
    time.sleep(1)
    slow_print("You stand up and look around.\n")
    time.sleep(1)
    slow_print("The forest, once meant to end your life, now offers a chance at a new beginning.\n")
    time.sleep(1)
    slow_print("What is this place? A second chance? or punishment for your choices?\n")
    time.sleep(1)
    slow_print("You take a deep breath and prepare yourself for the journey ahead.\n\n")
    time.sleep(1)
    getpass.getpass("Press enter to continue...")

# Player stats
player = { # Dictionary for easy access to player/enemy stats
    "hp": 10,
    "max_hp": 10,
    "damage": 0,
    "potion": 0,
    "stamina": 4,
    'max_stamina': 4
}

# Enemy stats
enemy1 = {
    "hp": 10,
    "attack": 3,
    'stamina': 4,
    'max_stamina': 4
}

enemy2 = {
    "hp": 15,
    "attack": 3,
    'stamina': 4,
    'max_stamina': 4
}

boss = { 
    "hp": 20,
    "attack": 5,
    'stamina': 4,
    'max_stamina': 4
}

# Combat function
def combat(enemy):
    turn = "player" if random.randint(0, 1) == 0 else "enemy" # Randomly choose who goes first, well its not always the player who goes first. Sometimes I got brutally killed by the dogs or rats on Darksouls/Elden ring without having a chance to attack.
    player_defense_mode = False # Defense mode is False at the start of combat
    enemy_defense_mode = False
    
    while player['hp'] > 0 and enemy['hp'] > 0: 
        clear_terminal()
        print("      Combat!")
        print('-'*18)
        print(f"Player HP: {player['hp']} / {player['max_hp']} | Stamina: {player['stamina']} / {player['max_stamina']} | Potion: {player['potion']}")
        print("\nEnemy HP:", enemy['hp'])
        print('-'*18)

        # Player's turn
        if turn == "player":
            print("Player's turn!")
            print("1. Attack")
            print("2. Defend")
            print("3. Use potion")
            print("4. Run")
            print('-'*18)
            choice = input("Enter your choice: ")

            if choice == "1":
                print("\nYou choose to attack the enemy!")

                crit_chance = random.random() # Random chance for critical hit
                if crit_chance < 0.1:
                    player_crit_dmg = player["damage"] + (player["damage"]//2) # Critical hit deals 1.5x damage
                    print("Critical hit!")

                    if enemy_defense_mode:
                        enemy['hp'] -= max(0, player_crit_dmg - 2) # If in defense mode, reduce damage by 2
                        print("The enemy successfully defended your attack!")
                        print("You deal", max(0, player_crit_dmg - 2), "damage to the enemy!")
                    else:
                        print("You deal", (player_crit_dmg), "damage to the enemy!")  
                        enemy['hp'] -= player_crit_dmg

                elif enemy_defense_mode:
                    enemy['hp'] -= max(0, player['damage'] - 2)  
                    print("The enemy successfully defended your attack!")
                    print("You deal", max(0, player['damage'] - 2), "damage to the enemy!")
                else:
                    print("You deal", player['damage'], "damage to the enemy!")  
                    enemy['hp'] -= player['damage']
                input("Press Enter to continue...")
                enemy_defense_mode = False # Reset defense mode for enemy after player's turn
                turn = "enemy" # Switch turn to enemy

            elif choice == "2":
                if player['stamina'] >= 2:
                    print("\nYou choose to defend! Incoming damage will be reduced.")
                    player['stamina'] -= 3 # Reduce stamina by 3 for defense to avoid spamming defense
                    player_defense_mode = True # Set defense mode to True
                else:
                    print("You are too tired to defend the incoming attack.")
                    player_defense_mode = False  # Reset defense mode if stamina is not enough
                input("Press Enter to continue...")
                enemy_defense_mode = False # Reset defense mode for enemy after player's turn
                turn = "enemy" # Switch turn to enemy

            elif choice == "3":
                print("\nYou use a potion!")
                if player['potion'] > 0:
                    player['hp'] = min(player['hp'] + 10, player['max_hp']) # Heal 10 HP, but not more than max HP
                    player['potion'] -= 1 # Reduce potion count by 1
                    print(f"You healed 10 HP!")
                else:
                    print("You don't have any potions left.")
                input("Press Enter to continue...")
                enemy_defense_mode = False # Reset defense mode for enemy after player's turn
                turn = "enemy" # Switch turn to enemy

            elif choice == "4":
                print("\nYou runs away!")
                run_chance = random.random() # Random chance to run away. Sometimes you need to take a risk to run away if you're in a tight spot.
                if run_chance < 0.3:
                    print("You successfully ran away!")
                    break
                else:
                    print("You failed to run away! The enemy catch up to you!")
                    turn = "enemy" # If failed to run away, switch turn to enemy
                input("Press Enter to continue...")
                enemy_defense_mode = False # Reset defense mode for enemy after player's turn
                turn = "enemy" # Switch turn to enemy

            else:
                print('') # Print empty line if invalid choice then continue the loop

            if player["max_stamina"] < 4: # Increase stamina by 1 if max stamina is less than 5
                player["stamina"] += 1 # Increase stamina by 1 each turn
            
        # Enemy's turn
        elif turn == "enemy":
            print("Enemy's turn!")
            enemy_choice = random.randint(1, 3) # Random choice for enemy's action

            if enemy_choice == 1 or enemy_choice == 2: # Enemy attacks or defends. I made the choices here are 1 and 2, because the enemy spamming defense is annoying even though its random.
                print("\nEnemy attacks you!") # The attack is similar to the player's attack

                crit_chance = random.random() # Random chance for critical hit. It would be unfair if the enemy cant do critical hit.
                if crit_chance < 0.1:
                    enemy_crit_dmg = enemy['attack'] + (enemy["attack"]//2) 
                    print("Critical hit!")

                    if player_defense_mode:
                        player['hp'] -= max(0, enemy_crit_dmg - 2)
                        print("You successfully defended the enemy's attack!")
                        print("Enemy deals", max(0, enemy_crit_dmg - 2), "damage to you!")
                    else:
                        player['hp'] -= enemy_crit_dmg
                        print("Enemy deals", (enemy_crit_dmg), "damage to you!")

                elif player_defense_mode:
                    player['hp'] -= max(0, enemy['attack'] - 2)
                    print("You successfully defended the enemy's attack!")
                    print("Enemy deals", max(0, enemy['attack'] - 2), "damage to you!")
                else:
                    player['hp'] -= enemy['attack']
                    print("Enemy deals", enemy['attack'], "damage to you!")
            
            elif enemy_choice == 3: # Same as player's defense
                if enemy["stamina"] >=2:
                    print("Enemy choose to defend! Incoming damage will be reduced.")
                    enemy["stamina"] -= 3
                    enemy_defense_mode = True
                else:
                    print('The enemy is too tired to defend!')
                    enemy_defense_mode = False
            
            turn = "player" # Switch turn to player
            player_defense_mode = False # Reset defense mode for player after enemy's turn
        
            input("Press Enter to continue...")

            if enemy["max_stamina"] < 4: # Same as player's stamina
                enemy["stamina"] += 1
    
    if player['hp'] <= 0: # If player's HP is 0, player dies
        print("You died...")
        getpass.getpass("Press enter to continue...")

        if player['hp'] <= 0 and enemy1['hp'] <= 0 and enemy2['hp'] <= 0:
            boss['hp'] = 20
            boss['stamina'] = 4
            explore3()
        elif player['hp'] <= 0:
            map2[5][8] = 'E'
            enemy_respawn()
            explore2()

    elif enemy1['hp'] <= 0: # If enemy's HP is 0 or less, enemy dies
        print("You defeated the enemy!")
        getpass.getpass("Press enter to continue...")
        respawn() # It will reset the player's HP, potion, and stamina. Youll just respawn in the same map.
    
    elif enemy2['hp'] <= 0:
        print("You defeated the enemy!")
        getpass.getpass("Press enter to continue...")
        respawn()
    
    elif boss['hp'] <= 0:
        print("You defeated the orc!")
        getpass.getpass("Press enter to continue...")
        respawn()



def respawn():
    player['hp'] = 10  # Restore full health
    player['potion'] = 2  # Reset potions
    player['stamina'] = 4  # Reset stamina
 
def enemy_respawn(): # Reset enemy's HP
    enemy1['hp'] = 10
    enemy1['stamina'] = 4
    enemy2['hp'] = 15
    enemy2['stamina'] = 4
    boss['hp'] = 20
    boss['stamina'] = 4

# Map
map1 = [
    list('╔═══════════════════════════════════════════╗'), # 0
    list('║0000000000000000000000000000000000000000000║'), # 1
    list('║00000000           000000000000000000000000║'), # 2
    list('║000                     0000000000000000000║'), # 3
    list('║0                   I                     |║'), # 4
    list('║000                     0000000000000000000║'), # 5 
    list('║00000000           000000000000000000000000║'), # 6
    list('║0000000000000000000000000000000000000000000║'), # 7
    list('╚═══════════════════════════════════════════╝'), # 8
]

map2 = [
    list('╔═══════════════════════════════════════════╗'), # 0
    list('║0000000000000000000000000000000000000000000║'), # 1
    list('║        00000000000000000   E    0000000000║'), # 2
    list('║0000       000000000000    0000    00000000║'), # 3
    list('║00      00000000000       000000         00║'), # 4
    list('║0000   E                00000000000000    |║'), # 5 
    list('║00000000            00000000000000000000000║'), # 6
    list('║0000000000000000000000000000000000000000000║'), # 7
    list('╚═══════════════════════════════════════════╝'), # 8
]

map3 = [
    list('╔═══════════════════════════════════════════╗'), # 0
    list('║0000000000000000000000000000000000000000000║'), # 1
    list('║0000000000           0000000000000000000000║'), # 2
    list('║0000                       0000000000000000║'), # 3
    list('║                 B                        |║'), # 4
    list('║00000                               0000000║'), # 5 
    list('║000000000                       00000000000║'), # 6
    list('║0000000000000000000000000000000000000000000║'), # 7
    list('╚═══════════════════════════════════════════╝'), # 8
]

# Print map
def print_map(map1): 
    print('Location: Deepnest')
    print("="*79)
    print('A dark, oppressive cave filled with silent echoes and hidden dangers.')

    print("-"*79)
    print(f"Name: {player['hp']}/{player['max_hp']}  |  Damage: {player['damage']}  |  Potion: {player['potion']}") # Print player's stats
    print("="*79)

    for row in map1: # Loop through each row in the map
        print(''.join(row)) # Join each character in the row and print it instead of printing each character separately
    print("="*79)


# Dialogue. I made the dialogue as a function so it can be called later.
def dialogue1():
    slow_print('You saw a worn backpack lies on the ground.\n')
    getpass.getpass('Press enter to continue...')

def dialogue2(): 
    player['damage'] += 2 
    player['potion'] += 2
    slow_print("You picked up the backpack.")
    time.sleep(0.5)
    slow_print(" Inside, you found a rusty sword and 2 flask.\n")
    time.sleep(0.5)
    slow_print('"How long has this been here...')
    time.sleep(0.5)
    slow_print(' and why does it feel like its meant for me?"\n')
    getpass.getpass('Press enter to continue...')

def dialogue3_alternate():
    slow_print("Maybe I should pick up the backpack first...\n")
    time.sleep(0.5)
    slow_print("It feels like something I might need later.\n")
    getpass.getpass('Press enter to continue...')

# Explore function for each map
def explore1():
    print_map(map1) # Print the map
    player_x = 7 # Set player's starting position
    player_y = 4 # Set player's starting position
    message_shown = False # Set message_shown to False so the message is only shown once
    bag_pick = False # Set bag_pick to False so the player can't go to the next map without picking up the bag

    while True:
        clear_terminal()
        new_x, new_y = player_x, player_y # Set new_x and new_y to player's current position.

        map1[player_y][player_x] = 'P' # Set player's position on the map to 'P'
        print_map(map1) # Print the map with the player's position
        map1[player_y][player_x] = ' ' # Reset player's position to empty space

        print('Use W/A/S/D to move, Q to quit.') 
        key = keyboard.read_event (suppress=True) # Read keyboard input without displaying it on the screen
        if key.event_type == 'down': # Check if the key is pressed down. This is to prevent the player from moving twice in one turn.
            if key.name == 'w':
                player_y -= 1
                time.sleep(0.1)
            elif key.name == 's':
                player_y += 1
                time.sleep(0.1)
            elif key.name == 'a':
                player_x -= 1
                time.sleep(0.1)
            elif key.name == 'd':
                player_x += 1
                time.sleep(0.1)
            elif key.name == 'q':
                print('Exiting game...')
                exit()

        if map1[player_y][player_x] == '║' or map1[player_y][player_x] == '═' or map1[player_y][player_x] == '0': # Check if the player hits a wall or tree
            player_x, player_y = new_x, new_y  # If the player hits a wall or tree, reset the player's position to the previous position

        if player_x == 16 and not message_shown: # Check if the player is at the location of the message and the message is not shown
            dialogue1()
            message_shown = True
        
        if map1[player_y][player_x] == 'I': # Check if the player picks up the bag
            dialogue2()
            bag_pick = True
        
        if map1[player_y][player_x] == '|': # Check if the player reaches the door. If the player picks up the bag, the player can go to the next map. If not, show an alternate message.
            if not bag_pick:
                dialogue3_alternate()
                player_x, player_y = new_x, new_y
            else:
                break

# Same as explore1() but with different map and enemies
def explore2():
    print_map(map2)
    player_x = 2
    player_y = 2
    
    if player['hp'] <= 0:
        respawn()

        while True:
            clear_terminal()
            new_x, new_y = player_x, player_y

            map2[player_y][player_x] = 'P'
            print_map(map2)
            map2[player_y][player_x] = ' '

            print('Use W/A/S/D to move, Q to quit.')
            key = keyboard.read_event (suppress=True)
            if key.event_type == 'down':
                if key.name == 'w':
                    player_y -= 1
                    time.sleep(0.1)
                elif key.name == 's':
                    player_y += 1
                    time.sleep(0.1)
                elif key.name == 'a':
                    player_x -= 1
                    time.sleep(0.1)
                elif key.name == 'd':
                    player_x += 1
                    time.sleep(0.1)
                elif key.name == 'q':
                    print('Exiting game...')
                    exit()

            if map2[player_y][player_x] == '║' or map2[player_y][player_x] == '═' or map2[player_y][player_x] == '0':
                player_x, player_y = new_x, new_y 
            
            if map2[player_y][player_x] == 'E':
                print("An enemy blocks your path!")
                getpass.getpass("Press enter to continue...")
                
                if enemy1['hp'] > 0: # To check which enemy will the player encounter
                    player_x, player_y = new_x, new_y
                    combat(enemy1)

                    if enemy1['hp'] <= 0:  # Remove enemy1 from the map after death
                        map2[5][8] = ' '

                elif enemy2['hp'] > 0:
                    player_x, player_y = new_x, new_y
                    combat(enemy2)

                    if enemy2['hp'] <= 0:
                        map2[2][29] = ' '
            
            if map2[player_y][player_x] == '|': 
                print("Beyond this door leads to the orc's lair.")
                getpass.getpass("Press enter to continue...")
                break

    else: 
        while True:
            clear_terminal()
            new_x, new_y = player_x, player_y

            map2[player_y][player_x] = 'P'
            print_map(map2)
            map2[player_y][player_x] = ' '

            print('Use W/A/S/D to move, Q to quit.')
            key = keyboard.read_event (suppress=True)
            if key.event_type == 'down':
                if key.name == 'w':
                    player_y -= 1
                    time.sleep(0.1)
                elif key.name == 's':
                    player_y += 1
                    time.sleep(0.1)
                elif key.name == 'a':
                    player_x -= 1
                    time.sleep(0.1)
                elif key.name == 'd':
                    player_x += 1
                    time.sleep(0.1)
                elif key.name == 'q':
                    print('Exiting game...')
                    exit()

            if map2[player_y][player_x] == '║' or map2[player_y][player_x] == '═' or map2[player_y][player_x] == '0':
                player_x, player_y = new_x, new_y 
            
            if map2[player_y][player_x] == 'E': # Check if the player encounters an enemy
                print("An enemy blocks your path!")
                getpass.getpass("Press enter to continue...")
                
                if enemy1['hp'] > 0: # To check which enemy will the player encounter
                    player_x, player_y = new_x, new_y
                    combat(enemy1)

                    if enemy1['hp'] <= 0:  # Remove enemy1 from the map after death
                        map2[5][8] = ' '

                elif enemy2['hp'] > 0:
                    player_x, player_y = new_x, new_y
                    combat(enemy2)

                    if enemy2['hp'] <= 0:
                        map2[2][29] = ' '

            if map2[player_y][player_x] == '|': 
                print("Beyond this door leads to the orc's lair.")
                getpass.getpass("Press enter to continue...")
                break

# Same as explore1() but with different map and boss enemy
def explore3():
    print_map(map3)
    player_x = 1
    player_y = 4

    if player['hp'] <= 0:
        respawn()

        while True:
            clear_terminal()
            new_x, new_y = player_x, player_y

            map3[player_y][player_x] = 'P'
            print_map(map3)
            map3[player_y][player_x] = ' '

            print('Use W/A/S/D to move, Q to quit.')
            key = keyboard.read_event (suppress=True)
            if key.event_type == 'down':
                if key.name == 'w':
                    player_y -= 1
                    time.sleep(0.1)
                elif key.name == 's':
                    player_y += 1
                    time.sleep(0.1)
                elif key.name == 'a':
                    player_x -= 1
                    time.sleep(0.1)
                elif key.name == 'd':
                    player_x += 1
                    time.sleep(0.1)
                elif key.name == 'q':
                    print('Exiting game...')
                    exit()

            if map3[player_y][player_x] == '║' or map3[player_y][player_x] == '═' or map3[player_y][player_x] == '0':
                player_x, player_y = new_x, new_y 
            
            if map3[player_y][player_x] == 'B': # Check if the player encounters the boss
                print("An orc blocking your exit!")
                getpass.getpass("Press enter to continue...")
                player_x, player_y = new_x, new_y
                combat(boss) # Combat with the boss

                if boss['hp'] <= 0:
                    map3[4][18] = ' '

            if map3[player_y][player_x] == '|':
                if boss['hp'] > 0: # If the boss is still alive, the player can't leave
                    print("The orc doesn't let you leave!")
                    player_x, player_y = new_x, new_y
                    getpass.getpass("Press enter to continue...")
                    combat(boss)
                else:
                    print("You escaped the cave!") # If the boss is defeated, the player can leave the cave
                    getpass.getpass("Press enter to continue...")
                    break
    else:
        while True:
            clear_terminal()
            new_x, new_y = player_x, player_y

            map3[player_y][player_x] = 'P'
            print_map(map3)
            map3[player_y][player_x] = ' '

            print('Use W/A/S/D to move, Q to quit.')
            key = keyboard.read_event (suppress=True)
            if key.event_type == 'down':
                if key.name == 'w':
                    player_y -= 1
                    time.sleep(0.1)
                elif key.name == 's':
                    player_y += 1
                    time.sleep(0.1)
                elif key.name == 'a':
                    player_x -= 1
                    time.sleep(0.1)
                elif key.name == 'd':
                    player_x += 1
                    time.sleep(0.1)
                elif key.name == 'q':
                    print('Exiting game...')
                    exit()

            if map3[player_y][player_x] == '║' or map3[player_y][player_x] == '═' or map3[player_y][player_x] == '0':
                player_x, player_y = new_x, new_y 
            
            if map3[player_y][player_x] == 'B': # Check if the player encounters the boss
                print("An orc blocking your exit!")
                getpass.getpass("Press enter to continue...")
                player_x, player_y = new_x, new_y
                combat(boss) # Combat with the boss

                if boss['hp'] <= 0:
                    map3[4][18] = ' '

            if map3[player_y][player_x] == '|':
                if boss['hp'] > 0: # If the boss is still alive, the player can't leave
                    print("The orc doesn't let you leave!")
                    player_x, player_y = new_x, new_y
                    getpass.getpass("Press enter to continue...")
                    combat(boss)
                else:
                    print("You escaped the cave!") # If the boss is defeated, the player can leave the cave
                    getpass.getpass("Press enter to continue...")
                    break

main_menu()
note()
prolouge()
explore1()
explore2()
explore3()

clear_terminal()
print("This game is incomplete!")
print("It has also a bug, maybe a lot. I just havent found them yet")
print("I only have a limited time to make this because of the other projects on other subjects")
print("I'll update this game if I have enough time and complete the storyline.\n")

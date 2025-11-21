import random
basic_health=100
# strategy_chosen=input("What is your choice? ") #Use it directly
pokemon_health=100
enemy_health=100
enemy_attack=20
# -------------- Function #1 ----------------
def choose_pokemon():
    pokemon_chosen = int(input("Enter your Pokemon's name(Charmander(1), Bulbasaur(2), Pikachu(3)):"))
    if pokemon_chosen == 1:
        print("You have chosen the pokemon Charmander!")
        pokemon_chosen = "Charmander"
    elif pokemon_chosen == 2:
        print("You have chosen the pokemon Bulbasaur!")
        pokemon_chosen = "Bulbasaur"
    elif pokemon_chosen == 3:
        print("You have chosen the pokemon Pikachu!")
        pokemon_chosen = "Pikachu"
    else:
        print("Sorry, that was not valid. Your pokemon's name is now Pikachu!")
        pokemon_chosen = "Pikachu"
        
   
    # Asking user to enter number of specific Pokemon.
 
 
# -------------Function #2-----------------
def game_intro():
    if choose_pokemon() == "pikachu":
        print("The forest around me crackles with energy as I step onto the grassy clearing—this is where wild Pokémon often appear. Suddenly, a flash of yellow darts out from behind a tree, cheeks sparking with tiny sparks of electricity. Pikachu tilts its head, lets out a curious “Pika?”, and I slowly reach for a Poké Ball… unsure if it wants to battle, befriend, or just play.")
    elif choose_pokemon() == "bulbasaur":
        print("Sunlight filters through the tall trees as I wander deeper into the quiet forest, the air warm and earthy. A rustling sound catches my attention, and a small green Pokémon steps into view—Bulbasaur, its plant bulb gently glowing with stored energy. It gives a calm “Bulba… saur!”, watching me closely as I decide whether to battle it, approach it, or earn its trust.")
    elif choose_pokemon() == "charmander":
        print("Heat shimmers in the rocky clearing as I make my way up the trail, the air growing warmer with every step. Suddenly, a small orange Pokémon appears atop a boulder—Charmander, its tail flame flickering brightly as it studies me with bright, determined eyes. It lets out a confident “Char!”, and I pause, wondering whether this fiery partner wants a friendly greeting or an exciting battle.")
   
    print("This is Ash Ketchum, a Pokémon Trainer from Pallet Town who began his journey at age ten with his partner Pikachu. Throughout his travels across many regions, he’s formed deep bonds with his Pokémon, challenged countless Gym Leaders, and competed in major leagues and tournaments. After years of adventure, Ash eventually became a World Champion, proving his growth from an eager beginner to one of the strongest trainers in the Pokémon world.")
 
# This code introduces the user to the pokemon that they chose. 

# -------------Function #3-----------------
def make_decision():
    pk_pick = input("You have encountered a wild pokemon: Do you want to battle it or catch it?")
    return pk_pick
 
 # In this function, the user is choosing whether to battle or catch it. 
 
# -------------Function #4-----------------
def pokemon_battle():
        print ("Having a battle against the Pokemon")
        print("Your health is: ") #Using health function
        print("Do you want to:")
        print(f"{"Attack":<10}{"Defend":<10}{"Skill":<10}{"Escape":>10}")
 

 
def choice(): #Also using health function
    if strategy_chosen=="attack" or "Attack":
        print("Your pokemon attack! It dealt 10 damage!")
        enemy_health-10
    elif strategy_chosen=="defend" or "Defend":
        print("Your pokemon defend! The enemy's next attack will deal half damage!")
        pokemon_health-(enemy_attack//2)
    elif strategy_chosen=="skill" or "Skill":
        print("Your pokemon use the skill! It dealt 30 damage!")
        print("(This skill can be used again in 1 turn)")
        enemy_health-30
    elif strategy_chosen=="escape" or "Escape":
        print("Your pokemon escapes!")

    
 
# -------------Function #4-----------------
 
def catch_and_battle():
    if make_decision() == "catch" or "Catch" or "catch it" or "Catch it":
        catch_random = random.random()
        if catch_random<=0.1:
            print("You caught the pokemon!")
        elif catch_random>0.1:
            print("You lost the pokemon")
        print("You have decided to catch the pokemon. You spot a wild Pokémon rustling in the grass ahead, its eyes locking onto yours with curiosity and challenge. Heart pounding, you ready your Poké Ball and take aim, hoping this throw will make the catch. The Poké Ball strikes the Pokémon, bursts open, and pulls it inside in a flash of light. After three tense shakes… {}")
    elif make_decision() == "battle" or "battle it" or "Battle" or "Battle it":
        pokemon_battle()
        choice()

# -------------Function #5-----------------
def manage_health(current_health,damage_taken):
    current_health = pokemon_health
    if current_health <= 0:
        print("Your health has gone to 0")
        end_game()
    elif current_health >= 1:
        print(f"Your pokemon's health is equal to {current_health}! You are still alive.")
        print(f"Your health: {current_health}")

# ------------ Function: Ends Game --------
def end_game(): # Function ends the game. 
    print("Since your pokemon is dead, the game is over.")
    return 
    
# ------------ Function #6 ---------------


# Function Calling Orders

choose_pokemon()
game_intro()
make_decision()
pokemon_battle()
choice()
catch_and_battle()
manage_health()
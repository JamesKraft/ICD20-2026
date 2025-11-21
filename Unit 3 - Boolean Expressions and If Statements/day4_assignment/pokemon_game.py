import random
# -------------- Function #1 ----------------
def choose_pokemon():
    pokemon_chosen = input("Enter your Pokemon's name(Charmander, Bulbasaur, Pikachu):").lower()
    if pokemon_chosen != "charmander" or "bulbasaur" or "pikachu":
        print("Sorry, your pokemon was invalid. Your pokemon will now be Pikachu!")
        pokemon_chosen = "pikachu"
    
    # Asking user to enter number of specific Pokemon.

    num = input("Enter the number of your Pokemon")

# -------------Function #2-----------------
def game_intro(player_pokemon):
    if choose_pokemon() == "pikachu":
        print("The forest around me crackles with energy as I step onto the grassy clearing—this is where wild Pokémon often appear. Suddenly, a flash of yellow darts out from behind a tree, cheeks sparking with tiny sparks of electricity. Pikachu tilts its head, lets out a curious “Pika?”, and I slowly reach for a Poké Ball… unsure if it wants to battle, befriend, or just play.")
    elif choose_pokemon() == "bulbasaur":
        print("Sunlight filters through the tall trees as I wander deeper into the quiet forest, the air warm and earthy. A rustling sound catches my attention, and a small green Pokémon steps into view—Bulbasaur, its plant bulb gently glowing with stored energy. It gives a calm “Bulba… saur!”, watching me closely as I decide whether to battle it, approach it, or earn its trust.")
    elif choose_pokemon() == "charmander":
        print("Heat shimmers in the rocky clearing as I make my way up the trail, the air growing warmer with every step. Suddenly, a small orange Pokémon appears atop a boulder—Charmander, its tail flame flickering brightly as it studies me with bright, determined eyes. It lets out a confident “Char!”, and I pause, wondering whether this fiery partner wants a friendly greeting or an exciting battle.")
    
    print("This is Ash Ketchum, a Pokémon Trainer from Pallet Town who began his journey at age ten with his partner Pikachu. Throughout his travels across many regions, he’s formed deep bonds with his Pokémon, challenged countless Gym Leaders, and competed in major leagues and tournaments. After years of adventure, Ash eventually became a World Champion, proving his growth from an eager beginner to one of the strongest trainers in the Pokémon world.")

# -------------Function #3-----------------
def make_decision():
    pk_pick = input("You have encountered a wild pokemon: Do you want to battle it or catch it?")
    return pk_pick
    

# -------------Function #4-----------------
def pokemon_battle(action,player_pokemon):
    if make_decision() == "catch" or "Catch" or "catch it" or "Catch it":
        print("You have decided to catch the pokemon. You spot a wild Pokémon rustling in the grass ahead, its eyes locking onto yours with curiosity and challenge. Heart pounding, you ready your Poké Ball and take aim, hoping this throw will make the catch. The Poké Ball strikes the Pokémon, bursts open, and pulls it inside in a flash of light. After three tense shakes… {}")
        catch_random = random.random()
        if catch_random<=0.5:
            print("You caught the pokemon!")
        elif catch_random>0.5:
            print("You lost the pokemon")
    elif make_decision() == "battle" or "battle it" or "Battle" or "Battle it":
        print("You have decided to battle the pokemon.")
        catch_random = random.random()
        if catch_random<=0.5:
            print("You battled, and won!")
        elif catch_random>0.5:
            print("You battled and lost!")

#----------- Function 6 & 7----------------





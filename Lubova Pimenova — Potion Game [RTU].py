# Video demo: https://youtu.be/b7zV05azGNk

import time # delaying the message appearance to make it easier for the user to understand the text. 
import random

cheat_count = 0
loss_count = 0
win_count = 0

# ------- POTION ------- #
class Potion:
    def __init__(self, name, ingredients, cure_for):
        self.name = name  
        self.ingredients = ingredients  
        self.cure_for = cure_for  

    def __str__(self):
        return f"{self.name} (Cures: {', '.join(self.cure_for)})\nIngredients: {', '.join(self.ingredients)}"

# Potion List
potions = [
    Potion("\033[32mElixir of Mortal Bliss\033[0m", ["Mushrooms of Sorrow", "Cursed Swamp Water", "Ashes of Lost Hopes", "Leprechaun's Luck"], ["Karmic Allergy"]),
    Potion("\033[32mBreath of Wet Fire\033[0m", ["Mermaid Scales", "Stone Troll's Blood", "Giant's Nose Hair"], ["Flying Amanita Rash", "Stone Face"]),
    Potion("\033[32mSedative of Eternal Sleep\033[0m", ["Unicorn Hooves without Horseshoes", "Ashes of Lost Hopes", "Ogre's Saliva"], ["Cursed Headache"]),
    Potion("\033[32mLiquid Luck\033[0m", ["Leprechaun's Luck", "Ashes of Lost Hopes", "Ogre's Saliva", "Stone Troll's Blood", "Cursed Swamp Water"], ["Mystical Dysfunction", "Stone Face", "Poor Dragon Syndrome"]),
    Potion("\033[32mSerum of Eternal Night\033[0m", ["Mushrooms of Sorrow", "Mermaid Scales", "Ogre's Saliva", "Cursed Swamp Water", "Earwax"], ["Mirror Syndrome"]),
]

# ------- DISEASE ------- #
diseases = ["Cursed Headache", "Flying Amanita Rash", "Stone Face", "Karmic Allergy", "Mirror Syndrome", "Mystical Dysfunction", "Poor Dragon Syndrome"]

# ------- POTION SEARCH ------- #
def find_potion_for_disease(disease):
    for potion in potions:
        if disease in potion.cure_for:
            return potion
    return None

# ------- PATIENT DESCRIPTION ------- #
def describe_patient():
    races = ["Golem", "Elf", "Dwarf", "Orc", "Spirit", "Fairy", "Demon", "Zombie", "Skeleton"]
    characteristics = ["Stinky", "Mad", "Soulless", "One-eyed", "Winged", "Creepy", "Repulsive", "Hairy", "Ancient", "Cursed"]

    patient_race = random.choice(races)
    patient_characteristic = random.choice(characteristics)
    patient_disease = random.choice(diseases)

    patient_descriptions = [
        f"One evening, a \033[34m{patient_characteristic} {patient_race}\033[0m arrived at your doorstep. By his symptoms, it is evident that he has \033[31m{patient_disease}\033[0m.",
        f"You were visited by a \033[34m{patient_characteristic}\033[0m traveler of the \033[34m{patient_race}\033[0m race who appears to be suffering from \033[31m{patient_disease}\033[0m.",
        f"Upon your doorstep stood a \033[34m{patient_characteristic} {patient_race}\033[0m with clear signs of \033[31m{patient_disease}\033[0m."
    ]
    current_patient = random.choice(patient_descriptions)
    
    print() # New Line (Enter)
    print(current_patient)

    return patient_disease

# ------- MINIGAME ------- #
def guess_word_game(actual_word, hidden_word):
    global cheat_count
    global loss_count
    global win_count

    # Replacing letters with numbers (a-1, b-2 etc.)
    encrypted_word = ""
    for letter in  hidden_word:
        if letter.isalpha():
            letter_value = ord(letter.lower()) - ord('a') + 1
            if letter_value < 10:
                encrypted_word += f"0{letter_value} "  
            else:
                encrypted_word += f"{letter_value} "
        else:
            encrypted_word += letter
            
    time.sleep(3)  # Delay
    print(f"\n\033[34mAncient Grimoire\033[0m: Your great forefather hid the secrets of some potions, you need to solve the riddle. Can you guess it? You can ask me for\033[36m help\033[0m or use \033[36mcheat\033[0m, but everything has a price.")
    print(f"\033[34m\nAncient Grimoire\033[0m: {encrypted_word.strip()}\n")  

    attempts = 3
    help_requests = [
                "\033[34mAncient Grimoire\033[0m: Oh, of course, \033[35meach letter of the alphabet must have its own ordinal number\033[0m! Couldn't they just be letters and not complicate our lives with numbers? But of course, we're in a world of magic, why not give each letter its own unique personality and number, as if that's more important than spells and potions",
                "\033[34mAncient Grimoire\033[0m: No difficulty at all, of course, but please continue your introduction to letters. Maybe someday you will find out that they can even form words\n1-A :: 2-B :: 3-C :: 4-D :: 5-E :: 6-F :: 7-G :: 8-H :: 9-I :: 10-J :: 11-K :: 12-L :: 13-M :: 14-N :: 15-O :: 16-P :: 17-Q :: 18-R :: 19-S :: 20-T :: 21-U :: 22-V :: 23-W :: 24-X :: 25-Y :: 26-Z"
                ] 
    help_index = 0  

    while attempts > 0:
        guess = input("Your guess: ")

        if guess.lower() == actual_word.lower():
            win_message = [
                "\033[34m\nAncient Grimoire\033[0m: Congratulations!!! At least you didn't kill your patient.",
                "\033[34m\nAncient Grimoire\033[0m: Bravo! Your patient has survived yet another one of your treatment methods. Who would've thought, right?",
                "\033[34m\nAncient Grimoire\033[0m: Hooray! Your patient is still in one piece. You've certainly mastered the art of not making things worse."
                 ]
            current_win_message = random.choice(win_message)
            print(current_win_message)
            win_count += 1
            return True
        elif guess.lower() == "help":
            current_help_request = help_requests[help_index]
            print(current_help_request)
            help_index = (help_index + 1) % len(help_requests) 
            attempts -= 1 
        elif guess.lower() == "cheat":
            cheat_count += 1
            if cheat_count >= 2:
                print("\033[34mAncient Grimoire\033[0m: I've put up with your tricks for a long time. Your soul is going to the very heart of hell, where perhaps even the demons will be surprised by your tricks. The GAME IS OVER, but you can always try your chances in the next life..... if, of course, you have another soul.")
                exit()
            else:
                print(f"\033[34mAncient Grimoire\033[0m: Ah, great cheater, you truly deserve praise! Your skill at deception and cheating is worthy of respect... though perhaps even your own character in the game is ashamed of you! Fine, the word is {actual_word}.")
        else:
            mistake_message = [
                "\033[34mAncient Grimoire\033[0m: Look what an expert we have here! Just one wrong letter pressed, and voila, magic turns into... er, magiK? Try again",
                "\033[34mAncient Grimoire\033[0m: Quite the alchemist, aren't you? Let's see if you can brew up the correct spelling.",
                "\033[34mAncient Grimoire\033[0m: Oh, the precision! Keep your focus, and let's make the spellings match your magical talents."
                ]
            current_mistake_message = random.choice(mistake_message)
            print(current_mistake_message)
            attempts -= 1

    print(f"\033[34m\nAncient Grimoire\033[0m: You couldn't guess the word. The word was \033[32m{actual_word}\033[0m. Sometimes even healers have trouble figuring out what to mix with what!")

    # Loss Counter
    loss_count += 1
    if loss_count >= 2:
        print("\033[34m\nNarrator\033[0m: You have so skillfully failed too many times! Your patients have decided to go to another alchemist, and the shop stands with its windows boarded up. It looks like it's GAME OVER, and we don't even have enough time machine to go back and fix all your 'victories'.")
        exit()

    return False


# ------- THE GAME ------- #
def game():
    # ------- WELCOME SCREEN ------- #
    start_game = input("Start the game? (Yes/No): ")

    if start_game.lower() == "yes":
        user_name = input("\nChoose your name, alchemist: ").capitalize()

        welcome_text = f"\nWelcome, \033[34m{user_name}\033[0m the alchemist!\n"
        print(welcome_text)

        time.sleep(2) # Delay before the start of the game
        game_intro = f"\033[34mNarrator\033[0m: In the dense forest, in the depths of a mystical kingdom, there lives an alchemist named \033[34m{user_name}\033[0m, a worthy heir to a great ancestor. An\033[34m ancient grimoire\033[0m and a mysterious potion shop have been entrusted to his caring hands. Now, in front of the portal to his magically concealed shop, wanderers and travelers gather, thirsting for incredible elixirs and magical potions. \033[1mSome recipes have been lost to time\033[0m and remain hidden in secrecy, somewhere within this enchanted store. Is \033[34m{user_name}\033[0m ready to unveil their secrets and fill the world with magic and wonders? The journey begins.."
    
        print(game_intro)

        # ------- GAMEPLAY ------- #
        while True:
            patient_disease = describe_patient()  # Patient Generator
            found_potion = find_potion_for_disease(patient_disease)  
            
            
            print(f"\nYou consult your potion recipe book and find a potion that can cure \033[31m{patient_disease}\033[0m:")
            if found_potion:
                # Hiden ingredient
                hidden_ingredients = found_potion.ingredients.copy()
                hidden_ingredient_index = random.randint(0, len(hidden_ingredients) - 1)
                hidden_ingredients[hidden_ingredient_index] = "***************"
                hidden_word = ", ".join(hidden_ingredients)

                time.sleep(3)  # Delay
                print(f"Potion: {found_potion.name} \nIngredients: {hidden_word}")
            else:
                print("\nYou don't have a potion that can cure this disease.")            
            
            if guess_word_game(found_potion.ingredients[hidden_ingredient_index], found_potion.ingredients[hidden_ingredient_index]): # minigame
                if win_count == 3:
                    print("\n\033[34mNarrator\033[0m: You reveal all the secrets of potions with such ease that it already feels like magic! Well the celebrations can begin, as YOU'VE WON the game, and I'm off to find a more interesting audience.... perhaps without such an outstanding talent.")
                    exit()

            play_again = input("\nDo you want to serve another customer? (Yes/No): ")
            if play_again.lower() != "yes":
                break
            else:
                print("\n" + "-"*40)

# START
game()

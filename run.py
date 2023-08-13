import sys
import time
import random
from tqdm import tqdm


def slow_print(t, typing_speed=90):
    """
    This function simulates a human typing effect by introducing
    a random delay between printing each character.
    """
    for char in t:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(random.random() * 5.0 / typing_speed)
    print()


def create_song_lyrics(lyrics_template, words):
    """
    This function generates song lyrics by replacing placeholders
    in the given lyrics template with specific words.
    It uses the format() method of the string to replace the placeholders
    with the values from the words dictionary.
    """
    return lyrics_template.format(**words)


def get_valid_input(prompt):
    """
    This function gets valid text input from the user.
    It ensures that the input is not empty and not a number.
    """
    while True:
        user_input = input(prompt)
        if user_input.strip() and not user_input.isdigit():
            return user_input
        else:
            print("Invalid input. Please enter valid text.")


# Welcome message for the game
slow_print("Welcome to Liric!")
slow_print("A game that allows you to create your own Vacation Serenade.\n")


# Prompt to start game
slow_print("Ready to get started? Type in 'yes' to continue:")
startGame = input()


# Validate the user's input
if startGame.lower() == "yes":
    slow_print("Okay, let's go!\n")
    time.sleep(0.5)
else:
    slow_print("Invalid input. Please type 'yes' to start the game.\n")
    exit()


# Question intro text
slow_print(
    "I need some more info from you to generate your song lyrics.\n"
    "Please type in your answers...\n")


# Define keywords for user input questions
words = {
    "place1": get_valid_input("Your favourite place with a beach: "),
    "partner_name": get_valid_input("Your partner's (or crush’s) name: "),
    "pet_name": get_valid_input("Your pet’s name: "),
    "place2": get_valid_input("Your favourite place with a mountain view: "),
    "day_activity": get_valid_input("Your favourite daytime outdoor activity: "),
    "flying_animal": get_valid_input("Your favourite animal that can fly: "),
    "beautiful_place": get_valid_input("The most beautiful place you ever visited: "),
    "night_activity": get_valid_input("Your favourite nighttime outdoor activity: "),
    "swimming_animal": get_valid_input("Your favourite animal that can swim: "),
    "last_vacation_spot": get_valid_input("Your last vacation spot by the sea: "),
}


# Read lyrics template from file
with open("lyrics_template.txt", "r") as file:
    lyrics_template = file.read()


# Progess bar for lyric generation
pbar = tqdm (total=100, position=0, leave=False)
for i in range(10):
    time.sleep(0.3)
    pbar.set_description("Loading...".format(i))
    pbar.update(10)
pbar.close()


# Create and print song lyrics
song_lyrics = create_song_lyrics(lyrics_template, words)
slow_print("\nReady! Here are your song lyrics: \n")
slow_print(song_lyrics)

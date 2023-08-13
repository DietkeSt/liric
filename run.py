import sys
import time
import random


def slow_print(t, typing_speed=50):
    """
    This function simulates a human typing effect by introducing
    a random delay between printing each character.
    """
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random() * 10.0 / typing_speed)
    print()


def create_song_lyrics(lyrics_template, words):
    """
    This function generates song lyrics by replacing placeholders
    in the given lyrics template with specific words.
    It uses the format() method of the string to replace the placeholders
    with the values from the words dictionary.
    """
    return lyrics_template.format(**words)


print("Welcome to Liric!")
print("A game that allows you to create your own Vacation Serenade.\n")

while True:
    startGame = input("Ready to get started? Type in 'yes' to continue:\n")

    if startGame.lower() == "yes":
        print("Okay, let's go!\n")
        time.sleep(1)
        print("Please let me know the following:\n")
        break
    else:
        print("Invalid input. Please type 'yes' to start the game.\n")


# Define keywords for user input questions
words = {
    "place1": input("Your favourite place with a beach: "),
    "partner_name": input("Your partner's (or crush’s) name: "),
    "pet_name": input("Your pet’s name: "),
    "place2": input("Your favourite place with a mountain view: "),
    "day_activity": input("Your favourite daytime outdoor activity: "),
    "flying_animal": input("Your favourite animal that can fly: "),
    "beautiful_place": input("The most beautiful place you ever visited: "),
    "night_activity": input("Your favourite nighttime outdoor activity: "),
    "swimming_animal": input("Your favourite animal that can swim: "),
    "last_vacation_spot": input("Your last vacation spot by the sea: "),
}


# Read lyrics template from file
with open("lyrics_template.txt", "r") as file:
    lyrics_template = file.read()


# Create and print song lyrics
song_lyrics = create_song_lyrics(lyrics_template, words)
print(song_lyrics)

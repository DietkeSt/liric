from ast import FloorDiv
from random import randint
import copy

print("Welcome to Liric!")
print("A game that allows you to create your own Vacation Serenade.\n")

startGame = input("Ready to get started? Type in yes or no:\n")

if startGame.lower() != "yes":
    quit()

print("Okay, let's go!\n")

place1 = input("Name your favourite place with a beach: ")
name = input("What is your partner's (or crush’s) name? ")
animal1 = input("What is your pet’s name? ")
place2 = input("Name your favourite place with a mountain view: ")
activity1 = input("What is your favourite daytime outdoor activity? ")
animal2 = input("What is your favourite animal that can fly? ")
place3 = input("Name the most beautiful place you ever visited: ")
activity2 = input("What is your favourite nighttime outdoor activity? ")
animal3 = input("What is your favourite animal that can swim? ")
place4 = input("Name your last vacation spot by the sea: \n")
    
# print Song Lyrics

print(

    "(Verse 1)\n\n" 
    "I packed my bags, set off on a flight\n"
    "To a place where dreams take flight\n"
    "Golden beaches, the sun so bright\n"
    "In the land of " + place1 + " everything felt just right\n\n"
        
    "(Chorus)\n\n"
    + name + " by my side, we explored the shore\n"
    "Danced with the waves, feeling the pure\n"
    + animal1 + " playing in the sand\n"
    "Time slipping away like grains in my hand\n\n"
        
    "(Verse 2)\n\n"
    "Ventured through " + place2 + " a magical sight\n"
    "Mountains kissed the heavens, such a breathtaking height\n"
    + activity1 + " in the morning, under the clear blue sky\n"
    + name + " and I felt like we could fly\n\n"
        
    "(Chorus)\n\n"
    + name + " by my side, we climbed so high\n"
    "Lost in the moment, reaching for the sky\n"
    + animal2 + " cheering from the trees\n"
    "Nature's symphony, bringing us to our knees\n\n"
        
    "(Bridge)\n\n"
    "Every moment, every sight\n"
    + place3 + "'s beauty, pure delight\n"
    + activity2 + " under the stars\n"
    "Lost in time, no walls, no bars\n\n"
        
    "(Verse 3)\n\n"
    "From " + place1 + " to " + place2 + ", the adventure goes on\n"
    "Through " + activity1 + " and " + activity2 + ", we carry on\n"
    "Hand in hand with " + name + ", heart full of glee\n"
    "This vacation, a dream, a moment of glee\n\n"
        
    "(Chorus)\n\n"
    + name + " by my side, we sail the sea\n"
    "The horizon ahead, full of mystery\n"
    + animal3 + " guiding our way\n"
    "In this paradise, we're destined to stay\n\n"
        
    "(Outro)\n\n"
    "As the sun sets, painting the sky\n"
    + place4 + "'s memories, forever in my eye\n"
    "A vacation to treasure, a love so true\n"
    + name + " and I, under the starry blue\n"

    )
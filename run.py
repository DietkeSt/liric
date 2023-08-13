from ast import FloorDiv
from random import randint
import copy

print("Welcome to Liric!")
print("A game that allows you to create your own Vacation Serenade.\n")

startGame = input("Ready to get started?\n")

if startGame.lower() != "yes":
    quit()

    print("Okay, let's go!\n")

    place1 = input("Name your favourite place with a beach.")
    name = input("What is your partner's (or crush’s) name?")
    animal1 = input("What is your pet’s name?")
    place2 = input("Name your favourite place with a mountain view.")
    activity1 = input("What is your favourite daytime outdoor activity?")
    animal2 = input("What is your favourite animal that can fly?")
    place3 = input("Name the most beautiful place you ever visited.")
    activity2 = input("What is your favourite nighttime outdoor activity?")
    animal3 = input("What is your favourite animal that can swim?")
    place4 = input("Name your last vacation spot by the sea.")

    #print Song Lyrics

    lyrics = (

        "(Verse 1)\n" 
        "I packed my bags, set off on a flight"
        "To a place where dreams take flight"
        "Golden beaches, the sun so bright"
        "In the land of [Place1], everything felt just right\n"
        
        "(Chorus)\n"
        "[Name] by my side, we explored the shore"
        "Danced with the waves, feeling the pure"
        "[Animal1] playing in the sand"
        "Time slipping away like grains in my hand\n"
        
        "(Verse 2)\n"
        "Ventured through [Place2], a magical sight"
        "Mountains kissed the heavens, such a breathtaking height"
        "[Activity1] in the morning, under the clear blue sky"
        "[Name] and I felt like we could fly\n"
        
        "(Chorus)\n"
        "[Name] by my side, we climbed so high"
        "Lost in the moment, reaching for the sky"
        "[Animal2] cheering from the trees"
        "Nature's symphony, bringing us to our knees\n"
        
        "(Bridge)\n"
        "Every moment, every sight"
        "[Place3]'s beauty, pure delight"
        "[Activity2] under the stars"
        "Lost in time, no walls, no bars\n"
        
        "(Verse 3)\n"
        "From [Place1] to [Place2], the adventure goes on"
        "Through [Activity1] and [Activity2], we carry on"
        "Hand in hand with [Name], heart full of glee"
        "This vacation, a dream, a moment of glee\n"
        
        "(Chorus)\n"
        "[Name] by my side, we sail the sea"
        "The horizon ahead, full of mystery"
        "[Animal3] guiding our way"
        "In this paradise, we're destined to stay\n"
        
        "(Outro)\n"
        "As the sun sets, painting the sky"
        "[Place4]'s memories, forever in my eye"
        "A vacation to treasure, a love so true"
        "[Name] and I, under the starry blue"
        
    )
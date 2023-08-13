print("Welcome to Liric!")
print("A game that allows you to create your own Vacation Serenade.\n")

while True:
    startGame = input("Ready to get started? Type in 'yes' to continue:\n")

    if startGame.lower() == "yes":
        print("Okay, let's go!\n")
        break
    else:
        print("Invalid input. Please type 'yes' to start the game.\n")


place1 = input("Name your favourite place with a beach: ")
name = input("What is your partner's (or crush’s) name? ")
animal1 = input("What is your pet’s name? ")
place2 = input("Name your favourite place with a mountain view: ")
activity1 = input("What is your favourite daytime outdoor activity? ")
animal2 = input("What is your favourite animal that can fly? ")
place3 = input("Name the most beautiful place you ever visited: ")
activity2 = input("What is your favourite nighttime outdoor activity? ")
animal3 = input("What is your favourite animal that can swim? ")
place4 = input("Name your last vacation spot by the sea: ")
    
# print Song Lyrics

lyricsTemplate = (
    "\n"
    "(Verse 1)\n\n" 
    "I packed my bags, set off on a flight\n"
    "To a place where dreams take flight\n"
    "Golden beaches, the sun so bright\n"
    f"In the land of {place1} everything felt just right\n\n"
        
    "(Chorus)\n\n"
    f"{name} by my side, we explored the shore\n"
    "Danced with the waves, feeling the pure\n"
    f"{animal1} playing in the sand\n"
    "Time slipping away like grains in my hand\n\n"
        
    "(Verse 2)\n\n"
    f"Ventured through {place2}, a magical sight\n"
    "Mountains kissed the heavens, such a breathtaking height\n"
    f"{activity1} in the morning, under the clear blue sky\n"
    f"{name} and I felt like we could fly\n\n"
        
    "(Chorus)\n\n"
    f"{name} by my side, we climbed so high\n"
    "Lost in the moment, reaching for the sky\n"
    f"{animal2} cheering from the trees\n"
    "Nature's symphony, bringing us to our knees\n\n"
        
    "(Bridge)\n\n"
    "Every moment, every sight\n"
    f"{place3}'s beauty, pure delight\n"
    f"{activity2} under the stars\n"
    "Lost in time, no walls, no bars\n\n"
        
    "(Verse 3)\n\n"
    f"From {place1} to {place2}, the adventure goes on\n"
    f"Through {activity1} and {activity2}, we carry on\n"
    f"Hand in hand with {name}, heart full of glee\n"
    "This vacation, a dream, a moment of glee\n\n"
        
    "(Chorus)\n\n"
    f"{name} by my side, we sail the sea\n"
    "The horizon ahead, full of mystery\n"
    f"{animal3} guiding our way\n"
    "In this paradise, we're destined to stay\n\n"
        
    "(Outro)\n\n"
    "As the sun sets, painting the sky\n"
    f"{place4}'s memories, forever in my eye\n"
    "A vacation to treasure, a love so true\n"
    f"{name} and I, under the starry blue\n"
)

print(lyricsTemplate)
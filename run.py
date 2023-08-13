def read_user_input_questions(filename):
    """
    This function reads user input questions file.
    It reads each line and removes whitespace using strip(),
    then collects the lines into a list and returns it.
    """
    with open(filename, "r") as file:
        return [line.strip() for line in file.readlines()]


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
        break
    else:
        print("Invalid input. Please type 'yes' to start the game.\n")


# Read input questions from file
user_input_questions = read_user_input_questions("user_input_questions.txt")


# Ask the user for input
words = {}
for question in user_input_questions:
    words[question] = input(question)


# Read lyrics template from file
with open("lyrics_template.txt", "r") as file:
    lyrics_template = file.read()


# Create and print song lyrics
song_lyrics = create_song_lyrics(lyrics_template, words)
print(song_lyrics)

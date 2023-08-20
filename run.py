import sys
import time
import random
from tqdm import tqdm
from simple_term_menu import TerminalMenu


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


def slow_print_lyrics(t, typing_speed=180):
    """
    This function is used to display the lyric text faster
    by adjusting the typing_speed.
    """
    for char in t:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(random.random() * 5.0 / typing_speed)
    print()


def get_valid_input(prompt):
    """
    This function gets valid text input from the user.
    It ensures that the input is not empty and not a number.
    """
    while True:
        user_input = input(prompt).strip() 
        if user_input and not user_input.isdigit():
            return user_input
        else:
            slow_print("Invalid input. Please enter valid text.\n")


def choose_topic():
    """
    This function gives the user a topic chooser 
    option using a terminal menu.
    """
    topics = ["beach", "love", "nature"]
    terminal_menu = TerminalMenu(topics, title="Choose a topic for your song lyrics:")
    chosen_index = terminal_menu.show()

    chosen_topic = topics[chosen_index]
    slow_print(f"You've chosen the topic: {chosen_topic.capitalize()}.\n")
    return chosen_topic



def load_lyric_template(chosen_topic):
    """
    This function loads the song lyric template file
    for the chosen topic.
    """
    template_filename = f"{chosen_topic}_lyrics_template.txt"
    with open(template_filename, "r") as file:
        return file.read()
    

def create_song_lyrics(lyrics_template, words):
    """
    This function creates the lyrics from the chosen
    lyrics template.
    """
    return lyrics_template.format(**words)


def start_game():
    """
    This function starts the game using a terminal menu.
    """
    options = ["yes", "no"]
    terminal_menu = TerminalMenu(options, title="Ready to get started?")
    chosen_index = terminal_menu.show()

    if chosen_index == 0:
        slow_print("\nOkay, let's start the game!\n")
        time.sleep(0.5)
        return True
    else:
        slow_print("Exiting the game. Goodbye!\n")
        sys.exit()


def get_user_input():
    """
    Function to ask user for input. 
    Defining the keywords for the lyric placeholders.
    """
    slow_print(
        "I need some more info from you to generate your song lyrics.\n"
        "Please type in your answers...\n")
    time.sleep(0.5)

    words = {
        "place1": get_valid_input("Your favourite place with a beach: \n"),
        "partner_name": get_valid_input("Your partner's (or crush’s) name: \n"),
        "pet_name": get_valid_input("Your pet’s name: \n"),
        "place2": get_valid_input("Your favourite place with a mountain view: \n"),
        "day_activity": get_valid_input("Your favourite daytime outdoor activity: \n"),
        "flying_animal": get_valid_input("Your favourite animal that can fly: \n"),
        "beautiful_place": get_valid_input("The most beautiful place you ever visited: \n"),
        "night_activity": get_valid_input("Your favourite nighttime outdoor activity: \n"),
        "swimming_animal": get_valid_input("Your favourite animal that can swim: \n"),
        "last_vacation_spot": get_valid_input("Your last vacation spot by the sea: \n"),
    }
    return words


def generate_song(chosen_topic, words):
    """
    This function creates and prints the song lyrics.
    It also shows a progress bar to indicate the process
    of song lyric creation for the user.
    """
    lyrics_template = load_lyric_template(chosen_topic)

    # Progess bar for lyric generation
    pbar = tqdm (total=100, position=0, leave=False)
    for i in range(10):
        time.sleep(0.3)
        pbar.set_description("Generating lyrics...".format(i))
        pbar.update(10)
    pbar.close()

    # Create and print song lyrics
    song_lyrics = create_song_lyrics(lyrics_template, words)
    slow_print("\nReady! Here are your song lyrics: \n")
    slow_print_lyrics(song_lyrics)


def main():
    """
    This main function displays a welcome message,
    starts the topic chooser,
    starts the game,
    starts the questions for the keywords,
    and generates and prints the lyrics.
    """

    # Welcome message for the game
    slow_print("Welcome to Liric!")
    slow_print("A game that allows you to create your own song lyrics.\n")

    # Choose a topic
    chosen_topic = choose_topic()

    # Start the game
    start_game()

    # Get user input for lyrics
    words = get_user_input()

    # Generate and print lyrics
    generate_song(chosen_topic, words)

if __name__ == "__main__":
    main()
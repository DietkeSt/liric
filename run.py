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


def choose_typing_speed():
    """
    This function allows the user to choose 
    the typing speed with a terminal menu.
    """
    options = ["Slow", "Medium", "Fast"]
    terminal_menu = TerminalMenu(options, title="\nReady! Let me know how quickly I should print out the lyrics for you.\n")
    chosen_index = terminal_menu.show()

    typing_speeds = [90, 180, 270]  # Corresponding typing speeds for "Slow", "Medium", "Fast"
    chosen_typing_speed = typing_speeds[chosen_index]

    slow_print(f"\nYou've chosen typing speed: {options[chosen_index]}.\n")
    return chosen_typing_speed


def get_valid_input(prompt, max_length=55):
    """
    This function gets valid text input from the user.
    It ensures that the input meets specified criteria
    and provides custom error messages.
    """
    while True:
        user_input = input(prompt).strip()

        if not user_input:
            slow_print("You did not type anything, please enter your answer below\n")
        elif not any(char.isalpha() for char in user_input):
            slow_print("Please enter at least one letter in your answer\n")
        elif len(user_input) < 2:
            slow_print("Please enter a word with at least 2 characters\n")
        elif len(user_input) > max_length:
            slow_print(f"Please enter a shorter answer. The max length is {max_length} characters.\n")
        else:
            return user_input


def choose_topic():
    """
    This function gives the user a topic chooser 
    option using a terminal menu.
    """
    topics = ["Beach", "Love", "Nature"]
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
    options = ["Yes", "No"]
    terminal_menu = TerminalMenu(options, title="Ready to get started?")
    chosen_index = terminal_menu.show()

    if chosen_index == 0:
        slow_print("Okay, let's start the game!\n")
        time.sleep(0.5)
        return True
    else:
        exit_options = ["Yes, exit the game", "No, start the game"]
        exit_menu = TerminalMenu(exit_options, title="Are you sure you want to exit the game?")
        exit_choice_index = exit_menu.show()

        if exit_choice_index == 1:
            return start_game()
        else:
            slow_print("Okay, exiting the game. Goodbye!\n")
            slow_print("To restart the game hit the 'Run' option on top of the screen.\n")
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
    # Load the lyrics template
    lyrics_template = load_lyric_template(chosen_topic)

    # Progess bar for lyric generation
    pbar = tqdm (total=100, position=0, leave=False)
    for i in range(10):
        time.sleep(0.3)
        pbar.set_description("Generating lyrics...".format(i))
        pbar.update(10)
    pbar.close()

    # Choose typing speed with a menu
    typing_speed = choose_typing_speed()

    # Create and print song lyrics
    song_lyrics = create_song_lyrics(lyrics_template, words)
    slow_print("Here are your song lyrics: \n")
    slow_print(song_lyrics, typing_speed)


def main():
    """
    This main function displays a welcome message,
    starts the topic chooser,
    starts the game,
    starts the questions for the keywords,
    and generates and prints the lyrics.
    """

    # Welcome message for the game
    slow_print("\nWelcome to Liric!")
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
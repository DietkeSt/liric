import sys
import time
import random
import re
import os
from tqdm import tqdm
from simple_term_menu import TerminalMenu


def continue_cls():
    """
    This function is used to clear the screen
    of the console.
    """
    menu = TerminalMenu(["Yes", "No"], title="Ready to continue?\n")
    continue_choice = menu.show()
    if continue_choice == 0:
        cls()
    else:
        slow_print(
            """
            Exiting the game. Goodbye!\n
            To restart the game hit the 'Run' option on top of the screen.\n
            """
            )
        sys.exit()

def cls():
    """
    This function is used to clear the screen
    of the console.
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def slow_print(text, typing_speed=90):
    """
    This function simulates a human typing effect by introducing
    a random delay between printing each character.
    """
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(random.random() * 5.0 / typing_speed)
    print()


def choose_typing_speed():
    """
    This function allows the user to choose 
    the typing speed with a terminal menu.
    """
    options = [
        "Slow", "Medium", "Fast", "Lightning Speed"
        ]
    terminal_menu = TerminalMenu(
        options, 
        title="Ready! How quickly should I print out the lyrics for you.\n"
        )
    chosen_index = terminal_menu.show()

    typing_speeds = [90, 180, 270, 900]
    chosen_typing_speed = typing_speeds[chosen_index]

    slow_print(
        f"You've chosen typing speed: {options[chosen_index]}."
        )
    time.sleep(0.5)
    cls()
    return chosen_typing_speed


def get_valid_input(prompt, max_length=25):
    """
    This function gets valid text input from the user.
    It ensures that the input meets specified criteria
    and provides custom error messages.
    """
    while True:
        user_input = input(prompt).strip()

        if not user_input:
            slow_print(
                "You did not type anything, please enter your answer below.\n"
                )
        elif not any(char.isalpha() for char in user_input):
            slow_print(
                "Please enter at least one letter in your answer.\n"
                )
        elif len(user_input) < 2:
            slow_print(
                "Please enter a word with at least 2 characters.\n"
                )
        elif len(user_input) > max_length:
            slow_print(
                f"Please enter a shorter answer. The max length is {max_length} characters.\n"
                )
        elif not re.match(r'^[A-Za-zÀ-ÖØ-öø-ÿ\s\'-]+$', user_input):
            slow_print(
                "Please do not use standalone special characters. Special characters within words are allowed, e.g. ', -, ñ.\n"
                )
        else:
            return user_input
        

def welcome_message():
    slow_print(
        """
        Welcome to Liric!\n
        A game that allows you to create your own song lyrics.\n
        """
    )


def choose_topic():
    """
    This function gives the user a topic chooser 
    option using a terminal menu.
    """
    topics = [
        "beach", "love", "nature"
        ]
    capitalized_topics = [topic.capitalize() for topic in topics] 
    terminal_menu = TerminalMenu(
        capitalized_topics, title="Choose a topic for your song lyrics:\n"
        )
    chosen_index = terminal_menu.show()
    time.sleep(0.5)
    cls()
    time.sleep(0.5)

    chosen_topic = topics[chosen_index]
    slow_print(
        f"You've chosen the topic: {capitalized_topics[chosen_index]}.\n"
        )
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
    options = [
        "Yes", "No"
        ]
    terminal_menu = TerminalMenu(options, title="Ready to continue?\n")
    chosen_index = terminal_menu.show()
    time.sleep(0.5)
    cls()
    time.sleep(0.5)

    if chosen_index == 0:
        slow_print(
            "Okay, let's create some lyrics!\n"
            )
        time.sleep(0.5)
        slow_print(
            """
            I need more info from you to generate your song lyrics.\n
            "When entering your data, please keep the following in mind:\n
            """
        )
        time.sleep(0.5)
        slow_print(
            """
            1. You have to enter at least 1 letter.\n
            2. The word can contain between 2-25 characters.\n
            3. You are not allowed to enter nothing, or just a space.\n
            4. Special characters are only allowed, if they belong to the word.\n
            5. Words like 'C3PO' are allowed.\n
            """
        )
        time.sleep(0.5)
        continue_cls()
        return True
    else:
        exit_options = ["Yes, exit the game", "No, start the game"]
        exit_menu = TerminalMenu(
            exit_options, title="Are you sure you want to exit the game?"
            )
        exit_choice_index = exit_menu.show()

        if exit_choice_index == 1:
            return start_game()
        else:
            slow_print(
                """
                Okay, exiting the game. Goodbye!\n
                To restart the game hit the 'Run' option on top of the screen.\n
                """
            )
            sys.exit()


def get_user_input(chosen_topic):
    """
    Function to ask user for input. 
    Defining the keywords for the lyric placeholders.
    """
    slow_print(
        f"Please type in your answers for the {chosen_topic} topic below.\n"
        )
    time.sleep(0.5)

    words = {
        "place1": get_valid_input("Name a place with a beach: \n"),
        "partner_name": get_valid_input("Your partner's name: \n"),
        "pet_name": get_valid_input("Your pet's name: \n"),
        "place2": get_valid_input("Name a place with mountains: \n"),
        "day_activity": get_valid_input("Name a daytime activity: \n"),
        "flying_animal": get_valid_input("Name a flying animal: \n"),
        "beautiful_place": get_valid_input("Name a beautiful place: \n"),
        "night_activity": get_valid_input("Name a nighttime activity: \n"),
        "swimming_animal": get_valid_input("Name a swimming animal: \n"),
        "last_vacation_spot": get_valid_input("Name a place by the sea: \n"),
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
    time.sleep(0.5)
    cls()
    time.sleep(0.5)

    slow_print(
        "Thanks for your answers! Generating your lyrics now...\n"
        )
    time.sleep(0.3)

    # Progess bar for lyric generation
    pbar = tqdm (total=100, position=0, leave=False)
    for i in range(10):
        time.sleep(0.3)
        pbar.update(10)
    pbar.close()

    # Choose typing speed with a menu
    typing_speed = choose_typing_speed()

    # Create and print song lyrics
    song_lyrics = create_song_lyrics(lyrics_template, words)
    time.sleep(0.5)
    cls()
    slow_print(
        "Here are your song lyrics:\n"
        )
    slow_print(song_lyrics, typing_speed)

    return song_lyrics


def ask_for_next_action(song_lyrics):
    """
    This function asks the user for the 
    next action after generating lyrics.
    """
    time.sleep(0.5)
    options = [
        "Choose another topic", "Save Lyrics", "Exit the game"
        ]
    terminal_menu = TerminalMenu(
        options, 
        title="\nWhat do you want to do now?\n"
        )
    chosen_index = terminal_menu.show()
    time.sleep(0.5)
    cls()

    if chosen_index == 0:
        return "choose_topic"
    elif chosen_index == 1:
        save_lyrics(song_lyrics)
        return "save_lyrics"
    elif chosen_index == 2:
        slow_print(
            """
            Exiting the game. Goodbye!\n
            To restart the game hit the 'Run' option on top of the screen.\n
            """
        )
        sys.exit()
    else:
        return "quit"
    

def handle_next_action(song_lyrics, chosen_topic):
    """
    This function ask the user for the next action
    after downloading the lyric file.
    """
    while True:
        # Ask the user for the next action
        next_action = ask_for_next_action(song_lyrics)

        if next_action == "choose_topic":
            chosen_topic = choose_topic()
            return chosen_topic, song_lyrics

        elif next_action == "save_lyrics":
            while True:
                # Ask if the user wants to quit or choose another topic
                exit_options = [
                    "Exit the game", "Choose another topic", "Save lyrics"
                    ]
                exit_menu = TerminalMenu(
                    exit_options, 
                    title="What do you want to do now?"
                    )
                exit_choice_index = exit_menu.show()
                time.sleep(0.5)
                cls()

                if exit_choice_index == 0:
                    slow_print(
                        "\nExiting the game. Goodbye!\n"
                        )
                    sys.exit()
                elif exit_choice_index == 1:
                    chosen_topic = choose_topic()
                    return chosen_topic, song_lyrics
                elif exit_choice_index == 2:
                    save_lyrics(song_lyrics)
                    return "save_lyrics"
                
        elif next_action == "quit":
            sys.exit()


def save_lyrics_to_file(song_lyrics, file_path):
    """
    This function allows you to save
    the generated lyrics to a local file.
    """
    try:
        with open(file_path, "w") as file:
            file.write(song_lyrics)
        slow_print(
            f"\nLyrics saved to {file_path}\n"
            )
    except Exception as e:
        slow_print(f"Error: {str(e)}")


def save_lyrics(song_lyrics):
    """
    This function prompts the user to choose a file location and then
    saves the generated lyrics to that file.
    """
    slow_print(
        "\nPlease specify the file path where you want to save the lyrics."
        )
    file_path = input("File path (e.g., /path/to/lyrics.txt): ").strip()

    if not file_path:
        slow_print(
            "File path cannot be empty. Lyrics were not saved.\n"
            )
    else:
        save_lyrics_to_file(song_lyrics, file_path)


def main():
    """
    This main function displays a welcome message,
    starts the topic chooser,
    starts the game,
    starts the questions for the keywords,
    and generates and prints the lyrics.
    """

    # Welcome message for the game
    welcome_message()

    # Choose a topic
    chosen_topic = choose_topic()

    # Start the game
    start_game()

    while True:
        # Get user input for lyrics
        words = get_user_input(chosen_topic)

        # Generate and print lyrics
        song_lyrics = generate_song(chosen_topic, words)

        # Ask the user for the next action
        chosen_topic, song_lyrics = handle_next_action(chosen_topic, song_lyrics)

if __name__ == "__main__":
    main()
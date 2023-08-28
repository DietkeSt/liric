import sys
import time
import random
import re
import os
import textwrap
from tqdm import tqdm
from simple_term_menu import TerminalMenu
from colorama import Fore, Style, Back, init

# Initialize Colorama for Windows
init()

# Global variables to store game state
game_state = {
    "chosen_topic": None,
    "generated_lyrics": None,
}

# Global menu styles
menu_style = {
    "menu_cursor": "❯ ",
    "menu_cursor_style": ("fg_cyan", "bold"),
    "menu_highlight_style": ("fg_cyan", "bold"),
    "cycle_cursor": True,
}


# Dictionary to map topic colors
topic_colors = {
    "beach": Fore.YELLOW + Style.BRIGHT,
    "love": Fore.MAGENTA + Style.BRIGHT,
    "nature": Fore.GREEN + Style.BRIGHT,
    }


def continue_cls():
    """
    This function is used to clear the screen
    of the console.
    """
    options = ["Yes", "No"]
    menu_title = "Ready to continue?\n"
    terminal_menu = TerminalMenu(
        options,
        title=menu_title,
        **menu_style
    )

    continue_choice = terminal_menu.show()
    if continue_choice == 0:
        cls()
    else:
        exit_cls()


def exit_cls():
    cls()
    exit_options = ["Yes, exit the game", "No, continue the game"]
    menu_title = "\nAre you sure you want to exit the game?\n"
    exit_menu = TerminalMenu(
        exit_options,
        title=menu_title,
        **menu_style
    )

    exit_choice_index = exit_menu.show()

    if exit_choice_index == 1:
        cls()
    else:
        slow_print(textwrap.dedent(
            f"""
            Okay, exiting the game. Goodbye!\n
            Hit {Fore.CYAN}{Style.BRIGHT}'Run'{Style.RESET_ALL} to restart.
            """
            )
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


def add_spaces_to_text(text, num_spaces=3):
    """
    This function adds spaces to text.
    It splits the text into lines and then adds
    the spaces and recombines the line afterwards.
    """
    lines = text.split('\n')
    indented_lines = [f"{' ' * num_spaces}{line}" for line in lines]
    indented_text = '\n'.join(indented_lines)
    return indented_text


def choose_typing_speed():
    """
    This function allows the user to choose
    the typing speed with a terminal menu.
    """
    cls()
    slow_print(textwrap.dedent(
        f"""
        {Fore.CYAN}{Style.BRIGHT}
        Ready!
        {Style.RESET_ALL}
        """
        )
    )
    time.sleep(0.5)
    options = ["Slow", "Medium", "Fast", "Lightning Speed"]
    menu_title = "\nChoose a printing speed:\n"
    terminal_menu = TerminalMenu(
        options,
        title=menu_title,
        **menu_style
    )

    chosen_index = terminal_menu.show()

    typing_speeds = [90, 180, 270, 900]
    chosen_typing_speed = typing_speeds[chosen_index]

    chosen_option_text = options[chosen_index]
    cls()
    slow_print(textwrap.dedent(
        f"""
        You have chosen: {Fore.CYAN}{Style.BRIGHT}{chosen_option_text}
        {Style.RESET_ALL}
        """
        )
    )
    time.sleep(0.5)
    cls()
    return chosen_typing_speed


def get_valid_input(prompt, max_length=25, input_color=Fore.CYAN):
    """
    This function gets valid text input from the user.
    It ensures that the input meets specified criteria
    and provides custom error messages.
    """
    def err_color(message):
        return Fore.RED + Style.BRIGHT + message

    while True:
        user_input = input(prompt).strip()

        if not user_input:
            slow_print(err_color(
                "You did not type anything, please enter your answer below.\n"
                )
            )
            
        elif not any(char.isalpha() for char in user_input):
            slow_print(err_color(
                "Please enter at least one letter in your answer.\n"
                )
            )
        elif len(user_input) < 2:
            slow_print(err_color(
                "Please enter a word with at least 2 characters.\n"
                )
            )
        elif len(user_input) > max_length:
            slow_print(err_color(
                "Text too long. Max. characters: {max_length}\n"
                )
            )
        elif not re.match(r'^[A-Za-z0-9À-ÖØ-öø-ÿ\s\'-]+$', user_input):
            slow_print(err_color(
                "Only use special characters within words, e.g. ', -, ñ.\n"
                )
            )
        else:
            return input_color + user_input + Style.RESET_ALL


def welcome_message():
    """
    This function is the introductory text
    when starting the game.
    It starts with the title animation and text.
    """
    title_txt = textwrap.dedent("""
    ♫ ♩ ♪ ♬ ♫ ♩ ♪ ♬ ♫ ♩ ♪ ♬ ♫ ♩ ♪ ♬ ♫ ♩ ♪ ♬ ♫ ♩ ♪ ♬ ♫ ♩ ♪ ♬ ♫ ♩ ♪ ♬
    ♩                                                             ♫
    ♪                           LIRIC                             ♩
    ♬                                                             ♪
    ♫ ♩ ♪ ♬ ♫ ♩ ♪ ♬ ♫ ♩ ♪ ♬ ♫ ♩ ♪ ♬ ♫ ♩ ♪ ♬ ♫ ♩ ♪ ♬ ♫ ♩ ♪ ♬ ♫ ♩ ♪ ♬
    """)

    title_blank = textwrap.dedent("""
    ♫ ♩ ♪ ♬ ♫ ♩ ♪ ♬ ♫ ♩ ♪ ♬ ♫ ♩ ♪ ♬ ♫ ♩ ♪ ♬ ♫ ♩ ♪ ♬ ♫ ♩ ♪ ♬ ♫ ♩ ♪ ♬
    ♩                                                             ♫
    ♪                                                             ♩
    ♬                                                             ♪
    ♫ ♩ ♪ ♬ ♫ ♩ ♪ ♬ ♫ ♩ ♪ ♬ ♫ ♩ ♪ ♬ ♫ ♩ ♪ ♬ ♫ ♩ ♪ ♬ ♫ ♩ ♪ ♬ ♫ ♩ ♪ ♬
    """)
    slow_print(Fore.CYAN + Style.BRIGHT + title_txt)

    for _ in range(3):  # Title animation loop
        cls()
        print(Fore.CYAN + Style.BRIGHT + title_blank)
        time.sleep(0.3)
        cls()
        print(Fore.CYAN + Style.BRIGHT + title_txt)
        time.sleep(0.3)
        cls()
        print(Fore.CYAN + Style.BRIGHT + title_blank)
        time.sleep(0.3)
        cls()
        print(Fore.CYAN + Style.BRIGHT + title_txt)
        time.sleep(0.3)
        
    time.sleep(1)

    slow_print( 
        Style.RESET_ALL +
        "Welcome to the song lyric MadLibs game!\n".center(63)
    )
    time.sleep(0.5)


def choose_topic():
    """
    This function gives the user a topic chooser
    option using a terminal menu.
    """

    topics = [
        "beach", "love", "nature"
        ]
    capitalized_topics = [topic.capitalize() for topic in topics]

    menu_title = "\nChoose a topic for your song lyrics:\n"
    terminal_menu = TerminalMenu(
        capitalized_topics,
        title=menu_title,
        **menu_style
    )

    chosen_index = terminal_menu.show()
    time.sleep(0.5)
    cls()
    time.sleep(0.5)

    chosen_topic = topics[chosen_index]
    topic_color = topic_colors.get(chosen_topic, Fore.RESET)

    slow_print(textwrap.dedent(
        f"""
        You chose the topic: {topic_color}{capitalized_topics[chosen_index]}
        {Style.RESET_ALL}
        """
        )
    )
    game_state["chosen_topic"] = chosen_topic
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
    continue_cls()
    time.sleep(0.5)
    slow_print(textwrap.dedent(
        f"""
        Great, let's get started.\n
        I will ask you for some info shortly...
        """
        )
    )
    time.sleep(1)
    cls()

    slow_print(textwrap.dedent(
        f"""
        Please keep these rules in mind:
        """
        )
    )
    time.sleep(0.5)

    slow_print(textwrap.dedent(
        f"""
        {Fore.CYAN}{Style.BRIGHT}
        1. You have to enter at least 1 letter.\n
        2. The word can contain between 2-25 characters.\n
        3. You are not allowed to enter nothing, or just a space.\n
        4. Standalone special characters are not allowed.\n
        5. Words like 'C3PO' are allowed.\n
        {Style.RESET_ALL}
        """
        )
    )
    time.sleep(0.5)
    continue_cls()
    return True


def get_user_input(chosen_topic):
    """
    Function to ask user for input.
    Defining the keywords for the lyric placeholders.
    """
    topic_color = topic_colors.get(chosen_topic, Fore.RESET)

    def get_colored_input(prompt):
        """
        This function gets user input with a specific color prompt.
        """
        return get_valid_input(
            Fore.CYAN + Style.BRIGHT + prompt + Style.RESET_ALL
            )

    slow_print(textwrap.dedent(
        f"""
        I will ask you for the needed info now...
        """
        )
    )
    time.sleep(1)
    cls()

    slow_print(textwrap.dedent(
        f"""
        Remember, your topic is: {topic_color}{chosen_topic.capitalize()}
        {Style.RESET_ALL}
        """
        )
    )
    time.sleep(0.5)

    words = {
        "place1": get_colored_input("\nName a place with a beach: "),
        "partner_name": get_colored_input("\nYour partner's name: "),
        "pet_name": get_colored_input("\nYour pet's name: "),
        "place2": get_colored_input("\nName a place with mountains: "),
        "day_activity": get_colored_input("\nName a daytime activity: "),
        "flying_animal": get_colored_input("\nName a flying animal: "),
        "beautiful_place": get_colored_input("\nName a beautiful place: "),
        "night_activity": get_colored_input("\nName a nighttime activity: "),
        "swimming_animal": get_colored_input("\nName a swimming animal: "),
        "last_vacation_spot": get_colored_input("\nName a place by the sea: "),
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

    slow_print(textwrap.dedent(
        f"""
        {Fore.CYAN}{Style.BRIGHT}
        Thanks!
        {Style.RESET_ALL}
        """
        )
    )
    slow_print(textwrap.dedent(
        f"""
        Generating your lyrics...\n
        """)
    )
    time.sleep(0.3)

    # Progess bar for lyric generation
    pbar = tqdm(total=100, position=0, leave=False)
    for i in range(10):
        time.sleep(0.3)
        pbar.update(10)
    pbar.close()
    time.sleep(0.5)

    # Choose typing speed with a menu
    typing_speed = choose_typing_speed()

    # Create and print song lyrics
    song_lyrics = create_song_lyrics(lyrics_template, words)
    topic_color = topic_colors.get(chosen_topic, Fore.RESET)
    time.sleep(0.5)
    cls()

    slow_print(textwrap.dedent(
        f"""
        Your lyrics for the topic: {topic_color}{chosen_topic.capitalize()}
        {Style.RESET_ALL}
        """
        )
    )
    time.sleep(1)

    slow_print(song_lyrics, typing_speed)
    game_state["generated_lyrics"] = song_lyrics 
    return song_lyrics


def ask_for_next_action(song_lyrics):
    """
    This function asks the user for the
    next action after generating lyrics.
    """
    time.sleep(0.5)
    print(textwrap.dedent(
        f"""
        ___________________________________________________________________\n
        """
        )
    )
    options = [
        "Choose another topic", "Print lyrics again", "Exit the game"
        ]
    menu_title = "\nWhat do you want to do now?\n"
    terminal_menu = TerminalMenu(
        options,
        title=menu_title,
        **menu_style
    )

    chosen_index = terminal_menu.show()
    time.sleep(0.5)
    cls()

    if chosen_index == 0:
        return "choose_topic"
    elif chosen_index == 1:
        return "print_lyrics"
    elif chosen_index == 2:
        exit_cls()
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

        elif next_action == "print_lyrics":
            # Continue to print the lyrics and offer speed selection
            chosen_topic = game_state["chosen_topic"]
            generated_lyrics = game_state["generated_lyrics"]
            print_generated_lyrics(chosen_topic, generated_lyrics)

        elif next_action == "quit":
            sys.exit()


def print_generated_lyrics(chosen_topic, generated_lyrics):
    """
    Print the generated lyrics and allow the user to choose
    the typing speed.
    """
    topic_color = topic_colors.get(chosen_topic, Fore.RESET)

    cls()
    
    for _ in range(2):  # Loading animation loop
        print("\nReloading.")
        time.sleep(0.3)
        cls()
        
        print("\nReloading..")
        time.sleep(0.3)
        cls()
        
        print("\nReloading...")
        time.sleep(0.3)
        cls()

    print("\nReloading...")
    time.sleep(1)

    typing_speed = choose_typing_speed()
    cls()
    slow_print(textwrap.dedent(
        f"""
        Your lyrics for topic: {topic_color}{chosen_topic.capitalize()}
        {Style.RESET_ALL}
        """
        )
    )
    slow_print(generated_lyrics, typing_speed)


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

    while True:
        if not game_state["chosen_topic"]:
            # Choose a topic if not chosen yet
            chosen_topic = choose_topic()
            game_state["chosen_topic"] = chosen_topic

        # Start the game
        start_game()

        # Get user input for lyrics
        words = get_user_input(game_state["chosen_topic"])

        # Generate and print lyrics
        song_lyrics = generate_song(game_state["chosen_topic"], words)

        # Ask the user for the next action
        chosen_topic, song_lyrics = handle_next_action(song_lyrics, game_state["chosen_topic"])


if __name__ == "__main__":
    main()

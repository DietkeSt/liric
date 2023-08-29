# Liric - A Song Lyric MadLib Game ♪♫

Liric is a MadLibs-style game where you create song lyrics based on a chosen topic. You'll be asked for various words, and then the game will generate and display the song lyrics for you. You can choose from different topics such as beach, love, and nature to customize the theme of your lyrics. Enjoy creating your unique song!

- [Deployed Liric Game](https://liric-89f62d9dc0a4.herokuapp.com/)

- [Liric repository on GitHub](https://github.com/DietkeSt/liric)

 ![Liric Screenshot](documentation/liric_screenshot.png)

---
## How to Play

1. **Open the Link:** Open [this link](https://liric-89f62d9dc0a4.herokuapp.com/). Or copy this link text in your browser's address bar: `https://liric-89f62d9dc0a4.herokuapp.com/`

2. **Start the Game:** Click "Run Programm" on the page and you will be greeted by a welcome message.

3. **Choose a Topic:** Select a topic for your song lyrics from options like "Beach," "Love," or "Nature."

4. **Game Rules:** Read and understand the game rules, which ensure that your inputs will not be rejected.

6. **Print Lyrics:** After providing all the inputs, the game will generate song lyrics based on your choices. Choose a typing speed depending on how quickly you want to read the lyrics.

7. **View Lyrics:** Enjoy reading the song lyrics!

8. **More fun:** After viewing the lyrics, you have options like choosing another topic, printing the lyrics again, or exiting the game.

*Remember, the goal is to create entertaining and creative lyrics based on your chosen topic. Enjoy the process and get creative!*

---

## User Stories

### First Time Visitor Stories:

| Goal | Scenario |
| ------------- | ------------- |
| As a first-time visitor, I want to understand how to play the game quickly, so I can start creating lyrics.   | When I visit the game for the first time, I want to see a clear and concise tutorial or welcome message that explains the game's rules and how to choose a topic and provide input. I want the instructions to be easy to follow so I can get started right away.   |
| As a first-time visitor, I want to explore different topics for song lyrics, so I can see the game's variety.   | When I start the game, I want to have a menu where I can choose from various topics like "beach," "love," or "nature." I want to be able to select a topic that interests me, and I expect the game to generate lyrics related to that topic.   |
| As a first-time visitor, I want to enjoy a visually appealing and engaging experience, so I can have fun while playing the game.   | When I play the game, I want to see colorful text, animations, and an overall visually pleasing interface. I expect the game to provide an enjoyable experience with attention to detail, making it more entertaining.   |


### Frequent Visitor Stories:

| Goal | Scenario |
| ------------- | ------------- |
| As a frequent visitor, I want to challenge myself by choosing different topics each time, so I can explore various creative possibilities.   | When I play the game again, I want to deliberately choose different topics for song lyrics to challenge my creativity. I expect the game to remember my previous choices but allow me to start fresh with a new topic.   |
| As a frequent visitor, I want to have the option to replay the generated lyrics at different typing speeds, so I can enjoy the lyrics in different ways. | After generating lyrics, I want the ability to replay them at a slower or faster typing speed to experience the lyrics differently. I expect the game to provide a menu where I can choose the desired speed.   |
| As a frequent visitor, I want to see updates or new features in the game, so I can continue to enjoy and be engaged with it over time.   | When I return to the game, I hope to see updates such as new topics, additional rules, or improved visual elements that keep the game fresh and exciting. I expect the game to evolve and provide a reason to revisit it.   |

---

## Features

### Welcome, and Topic Chooser:

- The user is greeted by a title animation and a welcome message, which follows the first request to select a topic for the song lyrics.

![Liric Welcome Screen](documentation/features/welcome.png)

### Topic Confirmation:

- After choosing a topic the game confirms the choice and gives the user the option to exit, in case the user changes their mind and wants to start from the beginning.

![Topic Confirmation Screen](documentation/features/topic_confirmation.png)

### Game Input Rules:

- After the user continues the game presents the input rules to make it easier for the user to avoid any input errors.

![Input Rules Screen](documentation/features/rules.png)

### Input Request

- The user is prompted to provide words by naming different places, names and animals. After hitting enter the next prompt request is shown until all words are provided.

![Input Words Screen](documentation/features/input_words.png)

### Loading Bar

- For a better user experience to keep the user engaged a loading bar animation is displayed after all words are provided. 

![Loading Bar Screen](documentation/features/loading_bar.png)

### Printing Speed
- The user is then presented with a choice of different printing speeds, depending on how fast the lyrics should be typed out.

![Typing Speed Screen](documentation/features/typing_speed.png)

### Printed Lyrics

- The user gets a confirmation of the typing speed and the lyrics are printed right away with a typing effect.
- The lyrics highlight the words the user provided for a better reading experience.

![Lyric Screen](documentation/features/lyrics.png)

### Next Action

- An option menu is presented, the user can choose another topic and will be asked to provide words for that topic, print the lyrics again at a different speed, or exit the game. 

![Next Action Screen](documentation/features/next_action.png)

### Exit Screen

- When the user wants to exit the game a confirmation request opens, explaining that all progress will be lost upon exiting the game.
- The user is then shown an exit screen animation with instructions on how to restart the game.

![Exit Screen](documentation/features/exit_game.png)

### General UX Features

- Use of consistent color to highlight important text.
- Highlight topic names in their representative color.
- Use Terminal Menu options throughout for ease of navigation. The user does not have to input the choices themselves, but can just select them with the up and down arrows on the keyboard.
- Is not rushed through the game, as the terminal will ask the user if they want to continue or not at several checkpoints in the game.
- Use of typing speed options to make it easier to read the text while it is typed out.
- Use of typing effect that gives the sense of a human interaction experience.

---

## Flowchart

The flowchart presents the logic of the game:

  ![Liric Flowchart Picture](documentation/flowchart.png)

---

## Technologies Used

### Languages:

- [Python 3.11.5](https://www.python.org/downloads/release/python-3115/): used to create game app and direct all behavior.

### Frameworks/Libraries, Programmes and Tools:
#### Python modules/packages:

##### Standard library imports:

- [os](https://docs.python.org/3/library/os.html): The os library provides a way to interface with the operating system. It's used for clearing the terminal screen using os.system().

- [sys](https://docs.python.org/3/library/sys.html): The sys library is used to access system-specific parameters and functions. In this code, it's primarily used for exiting the game with sys.exit().

- [time](https://docs.python.org/3/library/time.html): The time library is used for managing time-related operations. It's used for adding delays, creating a typing effect, and controlling timing throughout the game.

- [random](https://docs.python.org/3/library/random.html): The random library is used for generating random numbers. In the code, it's used to introduce randomness in the typing speed for the simulated typing effect.

- [re](https://docs.python.org/3/library/re.html): The re library provides support for regular expressions. In this code, it's used for validating user input to ensure it meets certain criteria, such as containing at least one letter.

- [textwrap](https://docs.python.org/3/library/textwrap.html): The textwrap library is used for text formatting. It's employed to format and wrap text within the terminal to ensure readability.

##### Third-party imports:

- [tqdm](https://pypi.org/project/tqdm/): The tqdm library is used to create progress bars. In the code, it's utilized to display a progress bar during the lyric generation process to provide visual feedback to the user.

- [simple_term_menu](https://pypi.org/project/simple-term-menu/): The simple_term_menu library is used for creating terminal menus. It enables the game to present menu options to the user, such as choosing a topic or selecting a typing speed.

- [colorama](https://pypi.org/project/colorama/): The colorama library is used to add color and style to text printed in the terminal. It's employed to create visually appealing and colorful text elements in the game, such as titles and topic names.

#### Other tools:

- [VSCode](https://code.visualstudio.com/) was used as the Development Environment to maintain, write and edit code.
- [Git](https://git-scm.com/) was used for the Version Control of the game.
- [GitHub](https://github.com/) is used to host the code in the Version Control Repository.
- [Heroku](https://render.com/) was used to deploy the project and is hosting the game in the Cloud Infrastructure.
- [Canva](https://www.canva.com/) was used to create and resize images for the README file.
- [FigJam](https://www.figma.com/figjam/) was used to make a flowchart for the README file.

---

## Bugs

### Solved Bugs:

1. The function `slow_print()` was not working as expected. The slow typing effect was not applied.

    - **Solution:** The space in the `end=" "` parameter was causing the issue. Removing the space fixed it. 
    ```Python
    def slow_print(text):
    """
    This function uses the time module to delay
    printing each character to achieve a typing effect.
    """
    for char in text:
        print(char, end=" ", flush=True)
        time.sleep(0.05)
    print()
    ```

2. The error handling function `def get_valid_input()` was not allowing names like C3P0, even though I wanted to allow it.

    - **Solution:** The match checker line was the issue. It did not include numbers, so no numbers would be allowed for the user input.

        Changed from: `re.match(r'^[A-Za-z0-9À-ÖØ-öø-ÿ\s\'-]+$', user_input)`
                        
        To: `re.match(r'^[A-Za-z0-9À-ÖØ-öø-ÿ\s\'-]+$', user_input)`

---

## Testing

The code and game functionality were constantly tested, fixed and improved during the development process. The text and lyrics were also proofread by other people to spot potential errors.

### Validators

Code Institute's [CI Python Linter](https://pep8ci.herokuapp.com/#) was used to ensure that the code is Pep8-compliant.

No errors were found:

#### run.py

![run.py Linter Testing](documentation/testing/run.py_linter.png)

#### lyric_templates_py

![lyric_templates.py Linter Testing](documentation/testing/lyric_templates_linter.png)

#### Potential Issues

Please note that both code files have the required empty line at the end of the code. Github might not show the last empty line correctly, so I am adding the relevant screenshot to showcase this:

![Empty Line present in code](documentation/testing/code_line_present.png)

---

## Deployment


### README.md

```markdown
# Hangman Game

This is a simple Hangman game implemented using Python and Tkinter. The game generates a random word from a list and allows the user to guess the word one character at a time. The game displays the Hangman ASCII art as the user makes incorrect guesses.

## Requirements

- Python 3.x
- Tkinter

## Installation

1. Clone the repository or download the source code.
2. Install the required packages using the command:

   ```bash
   pip install -r requirements.txt
   ```

3. Ensure you have a `words.txt` file with a list of words in the same directory as the script.

## Running the Game

Run the `main.py` script to start the game:

```bash
python main.py
```

## Project Structure

- `main.py`: The main script that sets up the Tkinter window and game logic.
- `utils.py`: Contains utility functions, including `is_subpart`.
- `generateBoxes.py`: Contains the function to generate text boxes in Tkinter.
- `Hangman_Printer.py`: Contains the function to print the Hangman ASCII art.
- `wordGen.py`: Contains the function to generate a random word from a list.

## How to Play

1. The game will display a number of empty text boxes corresponding to the number of characters in the word to be guessed.
2. Enter your guesses in the text boxes and click the "Submit" button.
3. If your guess is correct, the corresponding boxes will be filled. If not, the Hangman art will be updated.
4. You win if you guess the word before the Hangman is fully drawn.

## License

This project is licensed under the Apache License.
```

### requirements.txt

```plaintext
tk
```

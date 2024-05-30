import tkinter as tk
from tkinter.font import BOLD
from PIL import Image, ImageTk

import generateBoxes as gb
import Hangman_Printer as hp
import utils
import wordGen as wg

# Global variables
fail_counter = 0
word = wg.wordGenerator()
while word is None:
    word = wg.wordGenerator()

size = len(word)
window = tk.Tk()
window.title("Hangman")
window.geometry("500x630")

user_input = tk.StringVar()
displayed_word = ["_" for _ in range(size-1)]

# Submit button logic
def on_button_click(data):
    global fail_counter, displayed_word
    inputs = gb.get_inputs(data)
    input_string_data = ''.join(inputs).lower()
    user_input.set(input_string_data)

    result = utils.is_subpart(user_input, word, size)

    if result:
        for i, char in enumerate(result):
            if char != "":
                displayed_word[i] = char
        result_label.config(text=' '.join(displayed_word))

        if "_" not in displayed_word:
            result_label.config(text="You win!")
            button.config(state=tk.DISABLED)
    else:
        fail_counter += 1
        image_hang = hp.printer(fail_counter)
        hangman_image_label.config(text=str(image_hang))
        if fail_counter >= 9:
            result_label.config(text=f"You lose! The word was '{word}'")
            button.config(state=tk.DISABLED)

# Reset button logic
def reset_logic():
    global fail_counter, word, displayed_word
    fail_counter = 0
    word = wg.wordGenerator()
    while word is None:
        word = wg.wordGenerator()
    displayed_word = ["_" for _ in range(size)]
    result_label.config(text=' '.join(displayed_word))
    hangman_image_label.config(text="")
    for textbox in data:
        textbox.delete("1.0", tk.END)
    button.config(state=tk.NORMAL)

label = tk.Label(window, text="Guess the word and \nyou don't have many choices\n¯\\_(^.^)_/¯")
label.pack(side="top")

hangman_image_label = tk.Label(window)
hangman_image_label.pack()  # Attach the image of hangman

data = gb.generateRow(window, size)

button = tk.Button(window, text="Submit", command=lambda: on_button_click(data))
button.pack(side="right", padx=5, pady=5)

reset_button = tk.Button(window, text="Reset", command=reset_logic)
reset_button.pack(side="top", padx=5, pady=5)



result_label = tk.Label(window, text=' '.join(displayed_word), font=('Helvetica', 16, BOLD))
result_label.pack(side="top", pady=10)

window.mainloop()

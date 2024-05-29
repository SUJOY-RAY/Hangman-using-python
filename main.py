import tkinter as tk

from PIL import Image, ImageTk

import generateBoxes as gb
import Hangman_Printer as hp
import utils
import wordGen as wg

fail_counter = 0
word = wg.wordGenerator()
while word is None:
    word = wg.wordGenerator()
# input_string_data = ""

# image_hang=hp.printer(fail_counter)
size = len(word)
window = tk.Tk()
window.title("Hangman")
window.geometry("400x300")

user_input = tk.StringVar()


#Submit button logic
def on_button_click(data):
    global fail_counter
    inputs = gb.get_inputs(data)
    input_string_data = ''.join(inputs)

    print(input_string_data)
    print(fail_counter)
    user_input.set(input_string_data)

    if utils.is_subpart(user_input, word):
        print("You win")
        image_path = "img.jpg"  
        img = Image.open(image_path)
        resized_img=img.resize((60,60))
        resized_img=ImageTk.PhotoImage(resized_img)
        panel=tk.Label(window, image=resized_img)
        panel.image=resized_img
        
        panel.pack(side="top", fill="both", expand=True )
        
    
    else:
        fail_counter += 1
        image_hang = hp.printer(fail_counter)
        hangman_image_label.config(text=str(image_hang))



#Reset button logic
def reset_logic():
    window.destroy()
    import os
    os.system("python main.py")






# input_string_data=on_button_click(data)

# print("hello",input_string_data)

label = tk.Label(window,
                 text="Guess the word and \nyou don't have many choices")
label.pack(side="top")

hangman_image_label = tk.Label(window)
hangman_image_label.pack()  #attach the image of hangman

data = gb.generateRow(window, size)
button = tk.Button(window,
                   text="Submit",
                   command=lambda: on_button_click(data))

# print(input_string_data)

reset_button=tk.Button(window,text="Reset",command=reset_logic)

reset_button.pack(side="bottom", padx=5, pady=5)


button.pack(side="right", padx=5, pady=5)

window.mainloop()

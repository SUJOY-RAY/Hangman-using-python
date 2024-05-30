import tkinter as tk


def generateRow(window, columns):
  textBoxes = []
  for _ in range(columns-1):
    textbox = tk.Text(window, height=1, width=2)
    textbox.pack(side="left", padx=5, pady=5)
    textbox.insert(tk.END, "")
    textBoxes.append(textbox)
  return textBoxes

def get_inputs(textBoxes):
  inputs = []
  for textbox in textBoxes:
    text = textbox.get("1.0", tk.END).strip()
    inputs.append(text)
  return inputs

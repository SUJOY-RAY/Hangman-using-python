import random


def wordGenerator():
  try:
    with open("words.txt", "r") as file:
      wordList = file.readlines()
      if not wordList:
        print("Error: The file is empty.")
        return None

      word = random.choice(wordList)
      word.strip()
      print(word)
      return word

  except FileNotFoundError:
    print("Error: File not found.")
    return None

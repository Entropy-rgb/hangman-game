import random
import nltk
from nltk.corpus import words

nltk.download('words')
word_list = words.words()

# adding a filter to the words to take words whose lenghts are from 5 to 9 letters
filtered_words = [words.lower() for word in word_list if 5 <= len(word) <= 9 and word.isalpha()]

randomWord = random.choice(filtered_words)
lenghtOfWord = len(randomWord)

HANGMAN_PICS = ['''
   +---+
       |
       |
       |
      ===''', '''
   +---+
   O   |
       |
       |
      ===''', '''
   +---+
   O   |
   |   |
       |
      ===''', '''
   +---+
   O   |
  /|   |
       |
      ===''', '''
   +---+
   O   |
  /|\  |
       |
      ===''', '''
   +---+
   O   |
  /|\  |
  /    |
      ===''', '''
   +---+
   O   |
  /|\  |
  / \  |
      ===''']

# mistakes = 0
# correct = 0

# print('''
# ==========================================

#        WELCOME TO THE HANGMAN GAME 

#               HAVE FUN :)

# ==========================================
# ''')
# print(HANGMAN_PICS[0] + '\n\n\n')
# print(lenghtOfWord*'_ ')

# guess = input('What\'s Your Guess : ')
# guess = guess.lower()

# for i in range(0,lenghtOfWord):
#     if randomWord[i] == guess[i]:
#         print(randomWord[i]+" ",end="")
#         correct = correct + 1
#     else:
#         print('_ ',end="")

# if correct == lenghtOfWord:
#     print("You Win ! The correct Word is "+ randomWord)
# else:
#     pass
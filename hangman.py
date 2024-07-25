#Step 0 : Creating ASCII Drawing
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

#Step 01 : Creating a list
word_list = ["spiderman","superman","batman","hulk","ironman","flash"]

#Step 02 : Choosing random word from the list
import random
chosen_word = random.choice(word_list)
print(chosen_word)

lives = 6

#Step 03 : Crating a blank list:
display = []

#Step 04 : Update display with same number of blanks as the chosen word
for a in range(len(chosen_word)):
  display += "-"
print(display)


#Step 05 : loop through the chosen_word if the letter of that position matches with user input, then replace the blank with the letter plus making winning condition

game_ended = False

while not game_ended :
  guess = input("guess the letter : ").lower()
 #Check the guessed letter
  for position in range(len(chosen_word)):
    letter = chosen_word[position]
    if letter == guess:
      display[position] = letter
      print(display)

  if guess not in chosen_word:
      lives -= 1
      if lives == 0 :
        game_ended = True
        print("You lose, person is hanged")


  if "-" not in display:
   game_ended = True
   print("You win")

  print(stages[lives])





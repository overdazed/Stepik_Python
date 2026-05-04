import random
from requests import get # Import to generate requests on the Internet
from bs4 import BeautifulSoup # For parsing

word_list = [] # list of the Top 1500 nouns
r = get('https://www.talkenglish.com/vocabulary/top-1500-nouns.aspx') # fetching data from the website
soup = BeautifulSoup(r.text, 'html.parser') # parsing the HTML content using BeautifulSoup
text = soup.find_all('a', {'target':'_blank'}) # Extracting all <a> tags with 'target' attribute set to '_blank'

# Iterating over the extracted tags to collect noun words
for i in range(len(text)): # Iterate over the list of <a> tags
    for j in text[i]: # Iterate over the content of each <a> tag
        word_list.append(j) # Append the content (word) to the word_list

# print(word_list[:10])

def get_word():
   """
    Selects a random word from the word list and converts it to uppercase.
    
    Returns:
    - result (str): Randomly selected word converted to uppercase.
    """
   result = random.choice(word_list).upper()
   return result

# Welcome message
def welcome():
   print('Let\'s play a word guessing game!')


def print_word(word_, list_):
   """
    Prints the word with guessed letters filled in and blanks for unguessed letters.
    
    Args:
    - word_ (str): The word to be printed.
    - list_ (list): List of guessed letters.
    """
   for c in word_: # Iterate over each character in the word
      if c in list_:  # If the character has been guessed
         print(c, end=' ') # Print the guessed letter
      else:
         print('_', end=' ') # Print a blank for unguessed letters
   print() # Move to the next line after printing the word

def play(word):
   """
   Function to play the word guessing game.

   Args:
   - word (str): The word to be guessed.

   Returns:
   - None
   """
   word_completion = '_ ' * len(word)  # a string containing _ characters for each letter of the intended word
   guessed = False                    # flag
   guessed_letters = []               # list of already named letters
   guessed_words = []                 # list of already named words
   tries = 6                          # number of attempts
   welcome()                          # print welcome() message
   print(display_hangman(tries))      # display the initial hangman stage
   print(word_completion)             # display the initial word with blanks for each letter
   while True:
      word_input = input('Input a letter or a word: ').upper() # get user input and convert to uppercase
      if not word_input.isalpha(): # check if input is a letter or a word
         print('That is not a letter or a word! Try again.')
         continue
      if word_input in guessed_words or word_input in guessed_letters: # check if input has already been guessed
         print('Already there')
         continue
      if len(word_input) > 1: # if input is a word
         if word_input == word: # if guessed word is correct
            print('Congratulations, you guessed the word!  You won!')
            break
         else:
            guessed_words.append(word_input) # add guessed word to list
            tries -= 1 # decrement remaining tries
            print(f'Not true, {tries} tries left')
            print(display_hangman(tries)) # print updated hangman stage
            print_word(word, guessed_letters) # print word with guessed letters
            if tries == 0:
               print(f'You failed, the word was: {word}')
               break
            continue
            
      if word_input in word: # if guessed letter is in the word
         guessed_letters.append(word_input) # add guessed letter to list
         for c in word:
            if c not in guessed_letters: # if letter not guessed yet
               print('You guessed the letter')
               print_word(word, guessed_letters) # print word with guessed letters
               guessed = False
               break
            guessed = True
         if guessed:
            print_word(word, guessed_letters) # print word with guessed letters
            print('Congratulations, you guessed the word! You won!')
            break
      else:
         guessed_letters.append(word_input) # add guessed letter to list
         tries -= 1 # decrement remaining tries
         if tries == 2: # If 2 tries are left, ask for a hint
            hint_choice = input('You have 2 tries left. Do you want a hint? (y/n): ').lower()
            if hint_choice == 'y':
               not_guessed_letters = [c for c in word if c not in guessed_letters]
               hint = random.choice(not_guessed_letters) if not_guessed_letters else 'No hint available.'
            print(f'Hint: Try letter "{hint}"')
         print(f'Incorrect, {tries} attempts left')
         print(display_hangman(tries))  # print updated hangman stage
         print_word(word, guessed_letters) # print word with guessed letters
      if tries == 0:
         print(f'You couldn\'t guess the word: {word}')
         break
         
               
# function for obtaining the current status
def display_hangman(tries):
    stages = [ # final state: head, torso, both arms, both legs
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # head, torso, both arms, one leg
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # head, torso and both arms
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     
                   -
                ''',
                # head, torso and one arm
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # head and torso
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # head
                '''
                   --------
                   |      |
                   |      O
                   |     
                   |      
                   |     
                   -
                ''',
                # initial state
                '''
                   --------
                   |      |
                   |      
                   |     
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]              
   

def play_again():
   """
   Asks the player if they want to play again.
   
   Returns:
   - True if the player wants to play again, False otherwise.
   """
   while True:
      choice = input('Do you want to play again? (y/n)').lower()
      if choice == 'yes' or choice == 'y':
         return True
      elif choice == 'no' or choice == 'n':
         return False
      else:
         print('Invalid input. Please enter "y" or "n".')
         
while True:
   play(get_word().upper())
   if not play_again():
      break
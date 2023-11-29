# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 


# Detailed Project Description and Aims 
![](images/Hangman.jpg "Hangman code task 4")


The game of Hangman involves the user attempting to guess a secret word, by guessing a letter. At the start of the game, the secret word will be displayed with an "_" for each unguessed letter. This will allow the user to understand how many letters the secret word contains in total. The game allows the user 5 lives, meaning that if they guess incorrectly 5 times, then they will lose the game.

The user inputs their letter guess. If the letter they guess is contained within the secret word, then a message will be printed that the guess was correct. The letter will then be displayed in the corresponding positions within the secret word, replacing the "_".

If the user guesses incorrectly, a message will be printed that the guess was incorrect. A corresponding message will be printed to display the number of lives remaining. The user starts the game with 5 lives.

The user will continue to guess letters within the secret word, until either:

-   The user correctly guesses all letters in the secret word, before they run out of lives. The game will print a message that they have won the game.
-   The user uses up all 5 lives with incorrect guesses. The game will print a message that they have lost the game.

## Coding Summary
The python code was started by defining a Hangman class under OOPs (Object Orientated Programming). The constructor for initialisation is shown below also:
```python
class Hangman:
    '''
    This class is used to represent a game of Hangman
    Attributes:
        word_list(list):        list of words from which the secret word to be guessed is selected.
        word (str):             secret word to be guessed, which is selected at random from word_list.
        word_guessed(list):     list of letters of the secret word, with "_" for each unguessed letter.
        num_letters(int):       number of unique letters in the word that have not yet been guessed.
        list_of_guesses(list):  list of guesses that have altready been tried.
        num_lives(int):         number of lives the user has at the start of the game.

    '''
    def __init__(self, word_list, num_lives=5):
        '''
        This is the constructor for the Hangman class.
        Parameters are word_list and num_lives, which is set to a default value of 5.

        '''

        self.word_list = word_list
        self.word = random.choice(self.word_list)
        self.word_guessed = ["_"] * len(self.word)
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []
        self.num_lives = num_lives
```
The code defines 3 further methods, check_guess, ask_for_input and play_game with descriptions as follows: 
```python
def check_guess(self, guess):
        '''
        This method will check to see if the letter guessed by the user is contained within the secret word, selected at random within the list of words (word_list).
        Arguments:  guess, which is a letter input guessed by the user.
        Return: the method will print a message depending on whether the guess is contained within the secret word or not.

        '''
```

```python

def ask_for_input(self):
        '''
        This method will ask for user to guess a letter contained within the secret word, which they will input. 
        It will test to see if the input is valid, or whether the letter had already been selected.
        It will then check to see if letter is in the secret word.
        Return: it will print out correct guesses in the appropriate positions

        '''
```
```python
def play_game(self, word_list):
        '''
        This method will enable user to play a game of Hangman. 
        It will test to see whether the user has either used up all their lives with incorrect guesses, or correctly guessed the secret word.
        Arguments: word_list, which is a list of words that the secret word is selected from at random.
        Return: the method will print out a message depending on whether the user had won or lost the game.

        '''
```
Finally, the list of words from which the secret word is chosen at random, word_list is defined. Hangman class is instantiated and the game is run.

```python
word_list = ["apple","banana","mango","pear","melon"]
game=Hangman(word_list)
game.play_game(word_list)
```





# Installation Instructions
Download copy of the game from Darren Levene github repo https://github.com/DARREN-LEVENE/hangman825

Clone onto local machine and run python milestone_5.py





# Usage Instructions
See example games below, which will give you an idea of what to expect from the game:

Game Scenario 1 - User wins!

```python
AzureAD+Darrenlevene@DESKTOP-P7SPGCS MINGW64 /e/Wilmington Consulting Limited ye Jan 2015/AI Core/Hangman Project/hangman825 (main)
$ python milestone_5.py
Guess a letter:a
Good guess! a is in the word.
['a', '_', '_', '_', '_']
Guess a letter:w
Sorry, w is not in the word. Try again!
You have 4 lives left.
['a', '_', '_', '_', '_']
Guess a letter:w
You have already tried that letter!
Guess a letter:3
Invalid letter. Please enter a single alphabetical character.
Guess a letter:q
Sorry, q is not in the word. Try again!
You have 3 lives left.
['a', '_', '_', '_', '_']
Guess a letter:p
Good guess! p is in the word.
['a', 'p', 'p', '_', '_']
Guess a letter:l
Good guess! l is in the word.
['a', 'p', 'p', 'l', '_']
Guess a letter:e
Good guess! e is in the word.
['a', 'p', 'p', 'l', 'e']
Congratulations! You have won the game!
```
Game Scenario 2 - User loses!

```python
AzureAD+Darrenlevene@DESKTOP-P7SPGCS MINGW64 /e/Wilmington Consulting Limited ye Jan 2015/AI Core/Hangman Project/hangman825 (main)
$ python milestone_5.py
Guess a letter:a
Sorry, a is not in the word. Try again!
You have 4 lives left.
['_', '_', '_', '_', '_']
Guess a letter:m
Good guess! m is in the word.
['m', '_', '_', '_', '_']
Guess a letter:a
You have already tried that letter!
Guess a letter:n
Good guess! n is in the word.
['m', '_', '_', '_', 'n']
Guess a letter:e
Good guess! e is in the word.
['m', 'e', '_', '_', 'n']
Guess a letter:f
Sorry, f is not in the word. Try again!
You have 3 lives left.
['m', 'e', '_', '_', 'n']
Guess a letter:y
Sorry, y is not in the word. Try again!
You have 2 lives left.
['m', 'e', '_', '_', 'n']
Guess a letter:w
Sorry, w is not in the word. Try again!
You have 1 lives left.
['m', 'e', '_', '_', 'n']
Guess a letter:k
Sorry, k is not in the word. Try again!
You have 0 lives left.
['m', 'e', '_', '_', 'n']
You lost!
```

GOOD LUCK!

# Licence Information
MIT license
https://opensource.org/license/mit/

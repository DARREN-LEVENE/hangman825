import random

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

    def check_guess(self, guess):
        '''
        This method will check to see if the letter guessed by the user is contained within the secret word, selected at random within the list of words (word_list).
        Arguments:  guess, which is a letter input guessed by the user.
        Return: the method will print a message depending on whether the guess is contained within the secret word or not.

        '''
        guess=guess.lower()

        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")     
            self.num_letters = self.num_letters-1

            for index, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[index] = guess

        else:    
            self.num_lives = self.num_lives-1
            print(f"Sorry, {guess} is not in the word. Try again!")
            print(f"You have {self.num_lives} lives left.")

    def ask_for_input(self):
        '''
        This method will ask for user to guess a letter contained within the secret word, which they will input. 
        It will test to see if the input is valid, or whether the letter had already been selected.
        It will then check to see if letter is in the secret word.
        Return: it will print out correct guesses in the appropriate positions

        '''
        
        guess = input("Guess a letter:")                                          
        if len(guess)!=1 or not guess.isalpha():                                                                            
            print("Invalid letter. Please enter a single alphabetical character.")  

        elif guess in self.list_of_guesses:
            print("You have already tried that letter!")
            
        else:
            self.check_guess(guess)
            self.list_of_guesses.append(guess)
            print(self.word_guessed)
    
    def play_game(self, word_list):
        '''
        This method will enable user to play a game of Hangman. 
        It will test to see whether the user has either used up all their lives with incorrect guesses, or correctly guessed the secret word.
        Arguments: word_list, which is a list of words that the secret word is selected from at random.
        Return: the method will print out a message depending on whether the user had won or lost the game.

        '''
         
        while True:
            if self.num_lives==0:
                print("You lost!")
                break
            
            elif self.num_letters > 0:
                self.ask_for_input()
            
            else:
                print("Congratulations! You have won the game!")
                break

word_list = ["apple","banana","mango","pear","melon"]
game=Hangman(word_list)
game.play_game(word_list)
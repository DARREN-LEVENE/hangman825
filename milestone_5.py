import random

class Hangman:
    def __init__(self, word_list, num_lives=5):

        self.word_list = word_list
        self.word = random.choice(self.word_list)
        self.word_guessed = ["_"] * len(self.word)
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []
        self.num_lives = num_lives

    def check_guess(self, guess):
        guess=guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")     

            for index, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[index] = guess

        else:    
            self.num_lives = self.num_lives-1
            print(f"Sorry, {guess} is not in the word. Try again!")
            print(f"You have {self.num_lives} lives left.")

        self.num_letters = self.num_letters-1

    def ask_for_input(self):
        
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
         
        while True:
            if self.num_lives==0:
                print("You lost!")
                break
            
            elif self.num_letters > 0:
                self.ask_for_input()
            
            elif self.num_lives >0 and self.num_letters ==0:
                print("Congratulations! You have won the game!")
                break

word_list = ["apple","banana","mango","pear","melon"]
game=Hangman(word_list)
game.play_game(word_list)


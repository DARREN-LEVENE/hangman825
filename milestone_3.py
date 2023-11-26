import random

word_list = ["apple","banana","mango","pear","melon"]

random_word_from_list = random.choice(word_list)                    #generates random word from the list
print(random_word_from_list)


def ask_for_input():
    while True:                                                         #runs loop while true
        guess = input("Guess a letter:")                                #input letter guess from user and assign to variable "guess"            
        if len(guess)==1 and guess.isalpha():                           #tests whether guess is a single alphabetical character
            check_guess(guess)
        else:                                                       #if conditions met will break out of loop
            print("Invalid letter. Please enter a single alphabetical character.")      #if not met, statement will print 

def check_guess(guess):
    guess=guess.lower()

    if guess in random_word_from_list:                                  #checks to see if guess is in the randomly generated word from the list
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")

ask_for_input()

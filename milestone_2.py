import random
word_list = ["apple","banana","mango","pear","melon"]
print(word_list)

random_word_from_list = random.choice(word_list)         #generates random word from the list
print(random_word_from_list)

letter_guess = input("Enter a letter:")                 #asks user to input letter
if len(letter_guess)==1 and letter_guess.isalpha():     #tests whether input is a single letter
    print("Good guess!")
else:
    print("Oops! That is not a valid input!")
    
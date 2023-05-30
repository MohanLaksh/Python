# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 15:59:49 2023

@author: 01001X744
"""
import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words) # randomly select a word from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)
        
    return word
#print(word)
#print(words)
def hangman():
    word = get_valid_word(words)
    word_letters = set(word) # letters in the word
    alphabet = set(string.ascii_lowercase)
    used_letters = set() # what the user has guessed
    lives = int(len(word)) - 1
    #get user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        # " ".join(['a', 'b', 'cd']) --> a b cd
        print("You have already used: ", " ".join(sorted(used_letters)).upper())
        # what the current word is (ie., W _ R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Current Word: ", " ".join(word_list).upper())
        print("lives remaining: ", lives)

        user_letter = input("Guess a letter: ").lower()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            
            else:
                #lives = lives - 1
                print(f"Letter '", user_letter, "' not in word")
                print("lives remaining: ", lives)

                
        elif user_letter in used_letters:
            print("You have already used that character. Please try again!")
            
        else:
            print("Invalid character. Please try again!")
    # gets here when len(word_letters) == 0:
    if lives == 0:
        print("Sorry, you died!. The word was ", str(word).upper())
    else:
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Current Word: '", " ".join(word_list).upper(), "'")
        print("You guessed the word '", str(word).upper(), "'!!!")
hangman()
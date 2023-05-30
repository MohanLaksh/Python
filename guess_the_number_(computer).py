# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 12:26:37 2023

@author: 01001X744
"""
import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_number:
            print("Sorry!, guess again. Too low.")
        elif guess > random_number:
            print("Sorry!, guess again. Too high.")
 
    print(f"Hurray!, congrats. You have guessed the number {random_number} correctly!")
        
guess(10)

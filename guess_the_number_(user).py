# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 12:27:29 2023

@author: 01001X744
"""
import random

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low # could also be high as low == high
        feedback = input(f"Is {guess} too high (H), too low (L) or Correct (C)?").lower()
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1

    print(f"Yay!, The computer has guessed the number {guess} correctly!")


computer_guess(100)
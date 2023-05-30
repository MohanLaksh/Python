# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 12:52:33 2023

@author: 01001X744
"""
import random

def play():
    user = input("Please select your choice:\n 'r' for rock, 'p' for paper, 's' for scissors\n")
    computer = random.choice(['r', 'p', 's'])
    if user == computer:
        return 'It\'s a tie!'
    # r > s, s > p, p > r
    if is_win(user, computer):
        return ("You Won!")
    return("You lost :( !")

def is_win(player, opponent):
    # return true if player wins
    # r > s, s > p, p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
print(play())
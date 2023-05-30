# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 10:48:15 2023

@author: 01001X744
"""

#string concatenation (aka how to put strings together)
#suppose we want to create a string that says "Subscribe to ______"
youtuber = "Mohan Laksh" #some string value

# a few ways to do this
print("Subscribe to " + youtuber)
print("Subscribe to {}".format(youtuber))
print(f"Subscribe to {youtuber}")

adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Famous Person: ")

madlib = f"Computer programming is so {adj}! It makes me so excited all the time because \
    I love to {verb1}.Stay hydrated and {verb2} like a {famous_person}!"
print(madlib)
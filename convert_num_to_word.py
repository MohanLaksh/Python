# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 12:56:02 2023
CONVERT A NUMBER TO ITS EQUIVALENT WORD USING PYTHON
@author: 01001X744
"""
#num = 123456 
num = int(input("Enter a less than six digit number : ")) #input from user
def number_to_word(num):
    units = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    if num < 20:
        return units[num]
    elif num < 100:
        return tens[num//10] + (" " if num % 10 == 0 else " " + units[num % 10])
    elif num < 1000:
        return units[num//100] + " Hundred" + (" " if num % 100 == 0 else " " + number_to_word(num % 100))
    elif num < 1000000:
        return number_to_word(num // 1000) + " Thousand" + (" " if num % 1000 == 0 else " " + number_to_word(num % 1000))
    else:
        return "Number out of range."
print(number_to_word(num))

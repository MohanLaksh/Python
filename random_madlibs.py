# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 11:57:28 2023

@author: 01001X744
"""

from sample_madlibs import hp, code, zombie, hungergames
import random

if __name__ == "__main__":
    m = random.choice([hp, code, zombie, hungergames])
    m.madlib()
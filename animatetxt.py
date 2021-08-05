#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 17:46:52 2021

@author: bmondal
"""

import time
import sys
def scroll_text(text):
  for char in str(text):
    print(char, end='', flush=True)
    time.sleep(0.1)
scroll_text("Hello World")



def anything(str):
  for letter in str:
    sys.stdout.write(letter)
    sys.stdout.flush()
    time.sleep(0.1)

anything("You have woken up in a mysterious maze")
# Author: Aaron Powell (Github user "maxnewton")
#
# game.py - Game Classes
#
# This module includes basic classes for a text-based game engine where
# a user is presented with a story and some options to choose from.

import textwrap

class Stage:
    ''' A basic stage class '''
    
    def __init__(self, title, description, gameover=False):
        self.title = title
        self.description = description
        self.options = []
        self.gameover = gameover

    def print_description(self):
        for char in range(1,71):
            print('-', end='')
        print()
        for p in self.description:
            if p == '\n':
                print()
            else:
                for line in textwrap.wrap(p,70):
                    print(line)
        print()

class Option:
    ''' A basic option class '''

    def __init__(self, description, stage):
        self.description = description
        self.stage = stage

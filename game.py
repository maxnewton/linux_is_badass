# Author: Aaron Powell (GitHub user "maxnewton")
#
# game.py - Game Classes
#
# This module includes basic classes for a text-based game engine where
# a user is presented with a story and some options to choose from.

class Stage:
    ''' A basic stage class '''
    
    def __init__(self, title, description, gameover=False):
        self.title = title
        self.description = description
        self.options = []
        self.gameover = gameover

class Option:
    ''' A basic option class '''

    def __init__(self, description, stage):
        self.description = description
        self.stage = stage

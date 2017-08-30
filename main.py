"""
This Module will be testing the abilities of various music modules.
"""

from music21 import *


def play_score(score):
    s = converter.parseFile(score)
    s.show('midi')


def show_basic():
    converter.parse("tinynotation: 3/4 c4 d8 f g16 a g f#").show()


if __name__ == '__main__':
    play_score('dont_fear.mxl')
    pass

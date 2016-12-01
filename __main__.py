# Linux is Badass - The Python Game
# Author: Aaron Powell (GitHub user "maxnewton")
#
# This is an interactive, text-based adventure game based on Bryan Lunduke's "Linux is
# Badass". Except, instead of a PDF, this is Python. Clearly.
#
# The original can be downloaded on GitHub: https://github.com/BryanLunduke/LinuxIsBadass.
#
# For more works by Bryan (and to donate some pocket change to that handsome motherf*****),
# visit his website at http://lunduke.com/.
#
# This game is licensed under an Attribution-NonCommercial-ShareAlike 4.0 International
# license. For more info, visit https://creativecommons.org/licenses/by-nc-sa/4.0/.

from game import Stage, Option
from os import listdir
from os.path import isfile, join
import textwrap

def wrap(string, length):
    result = ''
    for block in string:
        if block == '\n':
            result += '\n'
        else:
            for line in textwrap.wrap(block, length):
                result += line + '\n'
    return result

def print_divider(length):
    for i in range(0,length):
        print('-', end='')
    print()

def loop(stage):
    print_divider(70)
    print(wrap(stage.description, 70))

    if not stage.gameover:
        for i, option in enumerate(stage.options):
            print('%d. %s' % (i+1, option.description))

        c = input('>:')
        print()

        loop(stage.options[int(c)-1].stage)
    
if __name__ == '__main__':
    # Load stage descriptions from files
    descriptions = []

    files = [f for f in listdir('data') if isfile(join('data', f))]
    files.sort()

    for file in files:
        with open('data/'+file) as f:
            content = f.readlines()
        descriptions.append(content)

    # Set up stages
    s0 = Stage('Welcome', descriptions[0])
    s1 = Stage('Part 1', descriptions[1])
    s2 = Stage('Part 2', descriptions[2])
    s3 = Stage('Part 3', descriptions[3])
    s4 = Stage('Part 4', descriptions[4])
    s5 = Stage('Part 5', descriptions[5])
    s6 = Stage('Part 6', descriptions[6])
    s7 = Stage('Part 7', descriptions[7])
    s8 = Stage('Part 8', descriptions[8])
    s9 = Stage('Part 9', descriptions[9])
    s10 = Stage('Part 10', descriptions[10])
    s11 = Stage('Part 11', descriptions[11])
    s12 = Stage('Part 12', descriptions[12])
    s13 = Stage('Part 13', descriptions[13], gameover=True)
    s14 = Stage('Part 14', descriptions[14])
    s15 = Stage('Part 15', descriptions[15], gameover=True)

    # Add options for Part 0
    s0.options.append(Option('Begin the game', s1))

    # Add options for Part 1
    s1.options.append(Option('Choose Windows', s4))
    s1.options.append(Option('Choose macOS', s5))
    s1.options.append(Option('Choose Linux', s6))
    s1.options.append(Option('Choose DOS', s2))

    # Add options for Part 2
    s2.options.append(Option('Give up and install Windows', s4))
    s2.options.append(Option('Give up and install macOS', s5))
    s2.options.append(Option('Regain your sanity and install Linux', s6))
    s2.options.append(Option('Stick to the plan and make DOS work', s3))

    # Add options for Part 3
    s3.options.append(Option('Give up and install Windows', s4))
    s3.options.append(Option('Give up and install macOS', s5))
    s3.options.append(Option('Regain your sanity and install Linux', s6))

    # Add options for Part 4
    s4.options.append(Option('Head home and install Windows', s7))
    s4.options.append(Option('Get some froyo', s8))

    # Add options for Part 5
    s5.options.append(Option('Time to head home and install this bad mamajama', s11))

    # Add options for Part 6
    s6.options.append(Option('Celebrate with some froyo', s14))
    s6.options.append(Option('Head home and install Linux', s15))
    s6.options.append(Option('Throw the DVD in his face and install Windows', s4))
    s6.options.append(Option('Give up your dreams and buy a turtleneck', s5))
    s6.options.append(Option('Break the DVD, go home and install DOS', s2))

    # Add options for Part 7
    s7.options.append(Option('Go the the library and use their Internet', s9))
    s7.options.append(Option('Bag it, try macOS', s5))
    s7.options.append(Option('I bet Linux can access the Internet', s6))
    s7.options.append(Option('Who needs the Internet? Time for DOS!', s2))

    # Add options for Part 8
    s8.options.append(Option('Home. Windows. Install.', s7))

    # Add options for Part 9
    s9.options.append(Option('Head to the store and buy and new Ethernet card', s10))

    # Add options for Part 10
    s10.options.append(Option('Buy a copy of macOS to install on your PC at home', s5))
    s10.options.append(Option('Just install Linux, already', s6))
    s10.options.append(Option('Hey, I heard DOS is pretty cool', s2))

    # Add options for Part 11
    s11.options.append(Option('Back to the Apple Store for help!', s12))
    s11.options.append(Option('Give up and try Windows', s4))
    s11.options.append(Option('Why are you not using Linux?', s6))
    s11.options.append(Option('Desperate enough for DOS?', s2))

    # Add options for Part 12
    s12.options.append(Option('Break down and buy a new Mac', s13))
    s12.options.append(Option('Just freaking install Windows', s4))
    s12.options.append(Option('L.I.N.U.X.', s6))
    
    # Add options for Part 13
    # Just kidding. There are none.

    # Add options for Part 14
    s14.options.append(Option('Get home and install Linux', s15))

    # Add options for Part 15
    # None here, either.

    # Let's get this game started!
    print('Linux is Badass - The Python Game')
    loop(s0)

# Linux is Badass - The Python Game
# Author: Aaron Powell (Github user "maxnewton")
#
# This is an interactive, text-based adventure game based on Bryan Lunduke's "Linux is
# Badass". Except, instead of a PDF, this is Python. Clearly.
#
# The original can be downloaded on Github: https://github.com/BryanLunduke/LinuxIsBadass.
#
# For more works by Bryan (and to donate some pocket change to that handsome motherf*****),
# visit his website at http://lunduke.com/.
#
# This game is licensed under an Attribution-NonCommercial-ShareAlike 4.0 International
# license. For more info, visit https://creativecommons.org/licenses/by-nc-sa/4.0/.

from game import Location, Choice
from os import listdir
from os.path import isfile, join

def loop(stage):
    stage.print_description()

    if not stage.gameover:
        i = 1
        for choice in stage.choices:
            print('%d. %s' % (i, choice.description))
            i += 1

        c = input('>:')
        print()

        loop(stage.choices[int(c)-1].location)
    
if __name__ == '__main__':
    print('Linux is Badass - The Adventure Game')
    
    # Load stage descriptions from files
    descriptions = []

    files = [f for f in listdir('data') if isfile(join('data', f))]
    files.sort()

    for file in files:
        with open('data/'+file) as f:
            content = f.readlines()
        descriptions.append(content)

    # Set up stages
    s0 = Location('Welcome!', descriptions[0])
    s1 = Location('Part 1', descriptions[1])
    s2 = Location('Part 2', descriptions[2])
    s3 = Location('Part 3', descriptions[3])
    s4 = Location('Part 4', descriptions[4])
    s5 = Location('Part 5', descriptions[5])
    s6 = Location('Part 6', descriptions[6])
    s7 = Location('Part 7', descriptions[7])
    s8 = Location('Part 8', descriptions[8])
    s9 = Location('Part 9', descriptions[9])
    s10 = Location('Part 10', descriptions[10])
    s11 = Location('Part 11', descriptions[11])
    s12 = Location('Part 12', descriptions[12])
    s13 = Location('Part 13', descriptions[13], gameover=True)
    s14 = Location('Part 14', descriptions[14])
    s15 = Location('Part 15', descriptions[15], gameover=True)

    # Add choices for Part 0
    s0.choices.append(Choice('Begin the game', s1))

    # Add choices for Part 1
    s1.choices.append(Choice('Choose Windows', s4))
    s1.choices.append(Choice('Choose macOS', s5))
    s1.choices.append(Choice('Choose Linux', s6))
    s1.choices.append(Choice('Choose DOS', s2))

    # Add choices for Part 2
    s2.choices.append(Choice('Give up and install Windows', s4))
    s2.choices.append(Choice('Give up and install macOS', s5))
    s2.choices.append(Choice('Regain your sanity and install Linux', s6))
    s2.choices.append(Choice('Stick to the plan and make DOS work', s3))

    # Add choices for Part 3
    s3.choices.append(Choice('Give up and install Windows', s4))
    s3.choices.append(Choice('Give up and install macOS', s5))
    s3.choices.append(Choice('Regain your sanity and install Linux', s6))

    # Add choices for Part 4
    s4.choices.append(Choice('Head home and install Windows', s7))
    s4.choices.append(Choice('Get some froyo', s8))

    # Add choices for Part 5
    s5.choices.append(Choice('Time to head home and install this bad mamajama', s11))

    # Add choices for Part 6
    s6.choices.append(Choice('Celebrate with some froyo', s14))
    s6.choices.append(Choice('Head home and install Linux', s15))
    s6.choices.append(Choice('Throw the DVD in his face and install Windows', s4))
    s6.choices.append(Choice('Give up your dreams and buy a turtleneck', s5))
    s6.choices.append(Choice('Break the DVD, go home and install DOS', s2))

    # Add choices for Part 7
    s7.choices.append(Choice('Go the the library and use their Internet', s9))
    s7.choices.append(Choice('Bag it, try macOS', s5))
    s7.choices.append(Choice('I bet Linux can access the Internet', s6))
    s7.choices.append(Choice('Who needs the Internet? Time for DOS!', s2))

    # Add choices for Part 8
    s8.choices.append(Choice('Home. Windows. Install.', s7))

    # Add choices for Part 9
    s9.choices.append(Choice('Head to the store and buy and new Ethernet card', s10))

    # Add choices for Part 10
    s10.choices.append(Choice('Buy a copy of macOS to install on your PC at home', s5))
    s10.choices.append(Choice('Just install Linux, already', s6))
    s10.choices.append(Choice('Hey, I heard DOS is pretty cool', s2))

    # Add choices for Part 11
    s11.choices.append(Choice('Back to the Apple Store for help!', s12))
    s11.choices.append(Choice('Give up and try Windows', s4))
    s11.choices.append(Choice('Why are you not using Linux?', s6))
    s11.choices.append(Choice('Desperate enough for DOS?', s2))

    # Add choices for Part 12
    s12.choices.append(Choice('Break down and buy a new Mac', s13))
    s12.choices.append(Choice('Just freaking install Windows', s4))
    s12.choices.append(Choice('L.I.N.U.X.', s6))
    
    # Add choices for Part 13
    # Just kidding. There are none.

    # Add choices for Part 14
    s14.choices.append(Choice('Get home and install Linux', s15))

    # Add choices for Part 15
    # None here, either.
    
    loop(s0)

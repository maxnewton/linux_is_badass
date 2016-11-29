import textwrap

class Location:
    ''' A basic location class '''
    
    def __init__(self, title, description, gameover=False):
        self.title = title
        self.description = description
        self.choices = []
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

class Choice:
    ''' A basic choice class '''

    def __init__(self, description, location):
        self.description = description
        self.location = location

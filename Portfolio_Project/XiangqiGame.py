# Author:      Jacob Hendry
# Date:        03/04/2020
# Description: This is a python file called XiangqiGame.py. It will play an abstract board game
#              called xiangqui. It must include a class called XiangqiGame that will determine
#              the state of the game, whether or not a player (red or black) is in check, and
#              will also make moves. Optional classes will include the player and pieces.


class Pieces:
    """This is class called Pieces. It will be a parent class for all of the pieces needed to
    play the game. It will include an init method"""
    def __init__(self, player, location):
        self._player = player
        self._location = location

    def get_player(self):
        return self._player


class General(Pieces):
    """This is a class called General. It will be a child class to the Pieces parent class
    and will hold all of the attributes to identify the General"""
    def __init__(self, player, location):
        super().__init__(player, location)
        self._name = ''
        self._location = ''

    def get_name(self):
        return self._name


class Advisor(Pieces):
    """This is a class called Advisor. It will be a child class to the Pieces parent class
    and will hold all of the attributes to identify the Advisor"""
    def __init__(self, player, location):
        super().__init__(player, location)


class Elephant(Pieces):
    """This is a class called Elephant. It will be a child class to the Pieces parent class
    and will hold all of the attributes to identify the Elephant"""
    def __init__(self, player, location):
        super().__init__(player, location)


class Horse(Pieces):
    """This is a class called Horse. It will be a child class to the Pieces parent class
    and will hold all of the attributes to identify the Horse"""
    def __init__(self, player, location):
        super().__init__(player, location)


class Chariot(Pieces):
    """This is a class called Chariot. It will be a child class to the Pieces parent class
    and will hold all of the attributes to identify the Chariot"""
    def __init__(self, player, location):
        super().__init__(player, location)


class Cannon(Pieces):
    """This is a class called Cannon. It will be a child class to the Pieces parent class
    and will hold all of the attributes to identify the Cannon"""
    def __init__(self, player, location):
        super().__init__(player, location)


class Soldier(Pieces):
    """This is a class called Soldier. It will be a child class to the Pieces parent class
    and will hold all of the attributes to identify the Soldier"""
    def __init__(self, player, location):
        super().__init__(player, location)


class Board:
    """This a class called Board. It will contain all of the coordinates for the board and will
    also have a method called printBoard that will print the board as well"""

    myBoard = {'a1': '[C]', 'b1': '[H]', 'c1': '[E]', 'd1': '[A]', 'e1': '[G]', 'f1': '[A]',
               'g1': '[E]', 'h1': '[H]', 'i1': '[C]', 'a2': '[ ]', 'b2': '[ ]', 'c2': '[ ]',
               'd2': '[ ]', 'e2': '[ ]', 'f2': '[ ]', 'g2': '[ ]', 'h2': '[ ]', 'i2': '[ ]',
               'a3': '[ ]', 'b3': '[C]', 'c3': '[ ]', 'd3': '[ ]', 'e3': '[ ]', 'f3': '[ ]',
               'g3': '[ ]', 'h3': '[C]', 'i3': '[ ]', 'a4': '[S]', 'b4': '[ ]', 'c4': '[S]',
               'd4': '[ ]', 'e4': '[S]', 'f4': '[ ]', 'g4': '[S]', 'h4': '[ ]', 'i4': '[S]',
               'a5': '[ ]', 'b5': '[ ]', 'c5': '[ ]', 'd5': '[ ]', 'e5': '[ ]', 'f5': '[ ]',
               'g5': '[ ]', 'h5': '[ ]', 'i5': '[ ]', 'a6': '[ ]', 'b6': '[ ]', 'c6': '[ ]',
               'd6': '[ ]', 'e6': '[ ]', 'f6': '[ ]', 'g6': '[ ]', 'h6': '[ ]', 'i6': '[ ]',
               'a7': '[S]', 'b7': '[ ]', 'c7': '[S]', 'd7': '[ ]', 'e7': '[S]', 'f7': '[ ]',
               'g7': '[S]', 'h7': '[ ]', 'i7': '[S]', 'a8': '[ ]', 'b8': '[C]', 'c8': '[ ]',
               'd8': '[ ]', 'e8': '[ ]', 'f8': '[ ]', 'g8': '[ ]', 'h8': '[C]', 'i8': '[ ]',
               'a9': '[ ]', 'b9': '[ ]', 'c9': '[ ]', 'd9': '[ ]', 'e9': '[ ]', 'f9': '[ ]',
               'g9': '[ ]', 'h9': '[ ]', 'i9': '[ ]', 'a10': '[C]', 'b10': '[H]', 'c10': '[E]',
               'd10': '[A]', 'e10': '[G]', 'f10': '[A]', 'g10': '[E]', 'h10': '[H]', 'i10': '[C]'}

    @staticmethod
    def printBoard(self):
        """This is a static method that wil print the board."""

        print('   | a  b  c  d  e  f  g  h  i ')
        print('---+------------------------')
        print('1  |' + self.board['a1'] + self.board['b1'] + self.board['c1'] + self.board['d1'] + self.board['e1'] +
              self.board['f1'] + self.board['g1'] + self.board['h1'] + self.board['i1'])
        print('2  |' + self.board['a2'] + self.board['b2'] + self.board['c2'] + self.board['d2'] + self.board['e2'] +
              self.board['f2'] + self.board['g2'] + self.board['h2'] + self.board['i2'])
        print('3  |' + self.board['a3'] + self.board['b3'] + self.board['c3'] + self.board['d3'] + self.board['e3'] +
              self.board['f3'] + self.board['g3'] + self.board['h3'] + self.board['i3'])
        print('4  |' + self.board['a4'] + self.board['b4'] + self.board['c4'] + self.board['d4'] + self.board['e4'] +
              self.board['f4'] + self.board['g4'] + self.board['h4'] + self.board['i4'])
        print('5  |' + self.board['a5'] + self.board['b5'] + self.board['c5'] + self.board['d5'] + self.board['e5'] +
              self.board['f5'] + self.board['g5'] + self.board['h5'] + self.board['i5'])
        print('   ===========RIVER============')
        print('6  |' + self.board['a6'] + self.board['b6'] + self.board['c6'] + self.board['d6'] + self.board['e6'] +
              self.board['f6'] + self.board['g6'] + self.board['h6'] + self.board['i6'])
        print('7  |' + self.board['a7'] + self.board['b7'] + self.board['c7'] + self.board['d7'] + self.board['e7'] +
              self.board['f7'] + self.board['g7'] + self.board['h7'] + self.board['i7'])
        print('8  |' + self.board['a8'] + self.board['b8'] + self.board['c8'] + self.board['d8'] + self.board['e8'] +
              self.board['f8'] + self.board['g8'] + self.board['h8'] + self.board['i8'])
        print('9  |' + self.board['a9'] + self.board['b9'] + self.board['c9'] + self.board['d9'] + self.board['e9'] +
              self.board['f9'] + self.board['g9'] + self.board['h9'] + self.board['i9'])
        print('10 |' + self.board['a10'] + self.board['b10'] + self.board['c10'] + self.board['d10'] +
              self.board['e10'] + self.board['f10'] + self.board['g10'] + self.board['h10'] + self.board['i10'])


class XiangqiGame:
    """This is a class called XiangqiGame. It will include an init method plus multiple other
    methods to determine piece moves, the game state and whether a player is in check or not"""

    def __init__(self):
        """This is an init method. It will initialize all of the data members within the XiangqiGame
        class and will all be private"""

        self._game_state = "UNFINISHED"
        self._check = False

    def get_game_state(self):
        """This get method will return the games state as either "UNFINISHED", "RED_WON, or
        "BLACK_WON"."""
        return self._game_state

    def set_game_state(self, game_state):
        """This set method will set the games state based on the whether it's finished or not"""
        self._game_state = game_state

    def is_in_check(self, current_player):
        """This method will determine if a current player is in check and return True if they are
        or return False if they are not"""

        if current_player is self.check_player_check:
            return True
        else:
            return False

    def check_player_check(self, current_player):
        """This method will determine if a player will be in check and if they are it will return
        True or else it will return False"""

        if current_player.self_player is self._check:
            return True
        else:
            return False

    def make_move(self, old_spot, new_spot):
        """This method will make a piece on the board move and only move if the move is valid. If the
        move is valid, it will return True or else it will return False"""


"""I wrote my program multiple times and every time seemed to fail. I wanted to try and start from
scratch which was the worst decision on my part because I lost so much time in writing my full code
and not just trying to fix problems as I . I already know I will be getting a low or zero grade on this 
assignment. None of this is an excuse, python and coding is very new to me and this project was the hardest 
project I've ever had to try and complete within a two week period. I'm feel like a failure and have sooooo 
much to learn. """

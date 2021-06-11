import time
#Author: Ashley Johnson
#Date: 5/30/2021
#Description: Program has a playing board to play Kuba. A player wins by
#capturing seven red stones or by pushing off all opponent stones. A
#player can move forward, backward, left or right.
S = """class initializes players, the gameboard, gets current turn, validates the player's name, 
gets the name of the players, determines if a player has won and returns the name, gets the
number of captured marbles, switches player turns, validates the move and updates the board, and
updates the board based on direction player moved. 
"""

c_white = "W"
c_black = "B"
c_red = "R"
class Marble():
    """class is used to get marble color, determine if a square is occupied by
    a red, empty, white, or black marble, and returns character."""
    def __init__(self,color=None):
        """initializes color, is_red function to false, is_empty function to
        false, and sets is_red to true if the square is red and sets _empty to
        true if square is empty."""
        self._color = color
        self._is_red = False
        self._empty = False
        if color:
            self._my_char = color[0].upper()
            if color == c_red:
                self._is_red = True

        else:
            self._empty = True
            self._my_char = " "
    def get_color(self):
        """returns color called by get_color function."""
        if self._color:
            return self._color


    def get_char(self):
        """returns the character called by function."""
        return self._my_char
    def is_red(self):
        """returns red if square is occupied by red marble."""
        return self._is_red
    def is_empty(self):
        """returns empty is square is empty."""
        return self._empty


class Printer():
    """class prints the Kuba board."""
    def square_start(self, last=False):
        """function starts at first string character and prints "+" and then
        continues to print the string until the end of string. Takes a boolean
        parameter to print the end of string. """
        last_char = '+'
        str = "+-----"
        if last:
            print(last_char)
        else:
            print(str,end='')

    def grid_line(self,width):
        """takes width as parameter and prints grid line given width
        parameter"""
        for _ in range(width):
            self.square_start()
        self.square_start(True)

    def square_no_data(self, last=False):
        """prints squares in board given width."""
        last_char = '|'
        str = "|     "
        if last:
            print(last_char)
        else:
            print(str,end='')

    def print_top_square(self, width):
        """
        takes width as parameter and prints top half of squares in a row of
        given width
        """
        self.grid_line(width)
        for _ in range(width):
            self.square_no_data()
        self.square_no_data(True)

    def print_bottom_square(self, width):
        """
        takes width as parameter and prints bottom half of squares in a row
        of given width
        """
        for _ in range(width):
            self.square_no_data()
        self.square_no_data(True)

    def print_data_row(self, row_marbles):
        """takes a row of marbles as a parameter and prints it."""
        for marble in row_marbles:
            str = marble.get_char()
            print("|  {}  ".format(str),end='')
        print("|")

    def print_row(self, row_data):
        """takes row data as parameter and prints it."""
        width = len(row_data)
        self.print_top_square(width)
        self.print_data_row(row_data)
        self.print_bottom_square(width)

class Player():
    """class initializes player name, color, number of marbles on board, tracks whose
    turn it is, tracks number of marbles captured as well as color, determines if
    a player has won the game,sets opponents, and prints the statistics of
    captured marbles."""
    def __init__(self,name,my_color):
        """takes player name and color as parameters and initializes
        player name, color, the number of marbles a player
        has on board, number of captured opponent marbles to zero, number of
        captured red marbles to zero, and sets is_my_turn to false."""
        self._name = name
        self._on_board = 8
        self._captured_opponent = 0
        self._captured_red = 0
        self._color = my_color
        self._is_my_turn = False
    def is_my_turn(self):
        """initializes and returns is_my_turn function to call to keep track
        of turns."""
        print("returning is my turn set to {}{}".format(self._is_my_turn,self.get_name()))
        return self._is_my_turn
    def make_my_turn(self):
        """sets is my turn to true to indicate which player's turn it is."""
        print("making {} turn".format(self.get_name()))
        self._is_my_turn = True
        self.opponent.make_not_my_turn()

    def set_opponent(self,player):
        """sets opponent player"""
        self.opponent = player


    def make_not_my_turn(self):
        """"initializes _is_my_turn to False to switch turns"""
        self._is_my_turn = False

    def get_name(self):
        """returns name of player."""
        return self._name
    def lose_marble(self):
        """keeps track of lost marbles on board by subtracting one from marble count
        when a player loses a marble."""
        self._on_board -= 1
    def has_won(self):
        """determines if player has won game by capturing 7 red marbles and returns
        true if player won game."""
        if self._captured_red >6:
            return True
    def has_lost(self):
        """determines if player lost game by losing all marbles and returns true
        if player lost by removing all marbles on board."""
        if self._on_board == 0:
            return True

    def captured_marble(self, this_marble):
        """takes a captured marble as a parameter and if the marble is red, updates
        captured red marble count by calling add_red_marble function, otherwise
        updates captured opponent marble and updates opponent's marble count by
        calling add_opponent_marble function and opponent.lose_marble function."""
        if not this_marble.is_empty():
            if this_marble.is_red():
                self._add_red_marble()
            else:
                self._add_opponent_marble()
                self.opponent.lose_marble()

    def _add_red_marble(self):
        """keeps track of captured red marbles."""
        print("adding red marble")
        self._captured_red += 1
    def _add_opponent_marble(self):
        """keeps track of captured opponent marbles."""
        self._captured_opponent +=1
    def get_num_red(self):
        """returns number of red captured marbles."""
        return self._captured_red
    def get_num_opponent(self):
        """returns number of opponenet captured marbles."""
        return self._captured_opponent
    def get_color(self):
        """returns color of marble or player. """
        print("player is returning my color of {}".format(self._color))
        return self._color


    def print_stats(self):
        """prints statistics of game."""
        status_string = "no winner yet"
        if self.has_won():
            status_string = "HAS WON!!"
        elif self.has_lost():
            status_string = "BOO I lost"
        print("*************************************")
        print("player name: {}".format(self._name))
        print("my color is: {} ".format(self._color))
        print("marbles on board: {}".format(self._on_board))
        print("number of red marbles: {}".format(self.get_num_red()))
        print("number of opponent marbles: {}".format(self.get_num_opponent()))
        print("status of player: {}".format(status_string))
        print("*************************************\n\n")


class GameBoard():
    """
    Container for all functionality related to printing
    gameboard.
    """

    def __init__(self):
        """calls iniitalize_board function to initialze board"""
        self.initialize_board()

    def initialize_board(self):
        """initializes game board. """
        R = Marble(c_red)
        W = Marble(c_white)
        B = Marble(c_black)
        E = Marble(None)
        startup = {
            0: [W,W,E,E,E,B,B],
            1: [W,W,E,R,E,B,B],
            2: [E,E,R,R,R,E,E],
            3: [E,R,R,R,R,R,E],
            4: [E,E,R,R,R,E,E],
            5: [B,B,E,R,E,W,W],
            6: [B,B,E,E,E,W,W],
        }

        keys = startup.keys()
        self._height = len(keys)
        self._state = startup

    def get_state(self):
        return self._state
    def get_marble_count(self):
        """returns number of red, black, and white marbles on board."""
        status = self.get_state()
        num_red = 0
        num_black = 0
        num_white = 0
        for key in status:
            this_row = status[key]

            for marble in this_row:
                color = marble.get_color()
                if color:
                    if color == c_red:
                        num_red +=1
                    elif color == c_black:
                        num_black += 1
                    elif color == c_white:
                        num_white += 1
        return (num_white, num_black, num_red)


    def get_row(self, row_num):
        """takes a row number as a parameter, validates row numbers, and returns
        the row of marbles."""
        state = self.get_state()
        try:
            row = state[row_num]
        except KeyError:
            print("row number {} not available".format(row_num))
            return None
        return row
    def set_row(self, row_num, new_marbles):
        """returns the new row of marbles after player makes a move by
         taking the row numbers and new_marbles list as parameter."""
        if len(new_marbles) != 7:
            print("try again i need 7 marbles")
            return
        state = self.get_state()
        keys = state.keys()
        if row_num not in keys:
            print("row_number {} not available".format(row_num))
        state[row_num] = new_marbles
        self._state = state
    def set_column(self, column, new_marbles):
        """Takes a column and a list of marbles as parameter and
        returns a new column for board after player makes B or F move."""
        state = self.get_state()
        new_marble_index = 0
        new_state = {}
        for key in state:
            row = state[key]
            new_marble = new_marbles[new_marble_index]
            row[column] = new_marble
            new_marble_index += 1
            new_state[key] = row
        self._state = new_state

    def get_column(self, column_num):
        """gets column of gameboard by taking the column number in dictionary
        as a parameter."""
        state =  self.get_state()
        my_column = []
        for key in state:
            row = state[key]
            try:
                entry = row[column_num]
            except IndexError:
                print("invalid column number")
                return
            my_column.append(entry)
        return my_column


    def get_colors(self, row):
        """function gets colors of marble in the row. Takes the row as a parameter
        and returns a list of the marble colors."""
        my_colors = []
        if row:
            for marble in row:
                my_colors.append(marble.get_color())
        return my_colors


    def get_state(self):
        """returns state of game."""
        return self._state

    def print_board(self):
        """prints game board."""
        print("*********************gameboard*********************")
        state = self.get_state()
        printer = Printer()
        width = 0
        for key in state.keys():
            row_marbles = state[key]
            width = len(row_marbles)
            printer.print_row(row_marbles)
        printer.grid_line(width)
        print("****************************************************\n\n\n\n\n")
class KubaGame:
    """class inialized players, gets the current turn, validates the player's name, tracks
    number of marbles captured, gets the name of the player, determines if a player has won
    and returns the name, gets the number of marbles on the board, gets the location of a
    specific marble, updates board based on direction player moved, and returns the
    statistics of the game."""


    def __init__(self, player_1, player_2):
        """initializes player_1 and player_2, initializes board by calling
        GameBoard function, and sets the opponent for each player. """
        self.player_1 = Player(player_1[0],player_1[1])
        self.player_2 = Player(player_2[0], player_2[1])
        self.board = GameBoard()
        self.player_1.set_opponent(self.player_2)
        self.player_2.set_opponent(self.player_1)


    def get_current_turn(self):
        """returns the name of the player whose turn it is."""
        if self.player_1.is_my_turn():
            return self.player_1.get_name()
        elif self.player_2.is_my_turn():
            return self.player_2.get_name()
        else:
            return None

    def valid_name(self, name):
        """function determines if the name of the player is valid. Takes the
        player's name as a parameter and returns True if the player's name
        is valid."""
        name_1 = self.player_1.get_name()
        name_2 = self.player_2.get_name()
        if name == name_1:
            return True
        if name == name_2:
            return True

        return False
    def get_player_by_name(self, name):
        """take's the player as a parameter and
        returns the name of the player. """
        if name == self.player_1.get_name():
            return self.player_1
        if name == self.player_2.get_name():
            return self.player_2
        return None

    def get_winner(self):
        """returns status of game by printing string that states whether a
         player has won or not. """
        status_string = "no winner yet"
        if self.has_won():
            status_string = "HAS WON!!"
        elif self.has_lost():
            status_string = "BOO I lost"
    def has_won(self):
        """initializes the has_won function to be called throughout program and
        returns the player's name that has won the game. """
        player_1 = self.player_1
        player_2 = self.player_2
        if player_1.has_won():
            return player_1.get_name()
        elif player_2.has_won():
            return player_2.get_name()
        else:
            return None

    def has_lost(self):
        """initializes the has_won function to be called throughout program and
        returns the player's name that has won the game. """
        player_1 = self.player_1
        player_2 = self.player_2
        if player_1.has_lost():
            return player_1.get_name()
        elif player_2.has_lost():
            return player_2.get_name()
        else:
            return None

    def get_captured(self, name):
        """takes player name as a parameter and returns the
        number of red marbles captured by player."""
        player = self.get_player_by_name(name)
        if player:
            return player.get_num_red()

    def get_marble(self,coordinates):
        """takes coordinates as a tuple as a parameter and returns the marble present at the location."""
        my_row = self.board.get_row(coordinates[1])
        row_index = coordinates[0]
        board_marble = my_row[row_index]

        if board_marble.is_empty():
            print("no marble was found, returning x")
            return "X"
        return board_marble.get_char()


    def get_marble_count(self):
        """returns the number of white, black, and red marbles as a tuple in that order."""
        white, black, red = self.board.get_marble_count()
        print("number of white marbles {}".format(white))
        print("number of black marbles {}".format(black))
        print("number of red marbles {}".format(red))
        return (white, black, red)


    def switch_player(self, last_name):
        """function takes the player's last name as a parameter and
         switches player's turn"""
        print("i'm at the top of switch player")
        if self.player_1.is_my_turn():
            self.player_2.make_my_turn()
        else:
            self.player_1.make_my_turn()

    def make_move(self, name, coordinates, direction):
        """function takes player name, coordinates, and direction they move the
        marble as parameters and returns updated board and switches the player's
        turn. Function gets current player's turn, direction they want to move,
        and then updates the board by shifting marbles at the coordinate provided."""
        player = self.get_current_player(name)
        status = False
        if not player:
            print("can't make move player incorrect")
            return False
        if direction.upper() == "L":
            status = self.move_left(player, coordinates)


        elif direction.upper() == "R":
            status= self.move_right(player, coordinates)

        elif direction.upper() == "F":
            status= self.move_forward(player,coordinates)

        elif direction.upper() == "B":
            status = self.move_backward(player, coordinates)

        else:
            print("invalid move must be L,R,F,B")
            return False

        self.board.print_board()
        self.switch_player(name)
        return status

    def move_left(self,player, coordinates):
        """function determines if left move is valid and determines  what
        marbles to shift left. Takes player name and coordinates as parameters and returns
        updated board after player moved left."""
        my_row = self.board.get_row(coordinates[0])
        row_index = coordinates[1]
        print("moving left from row {} column {}".format(coordinates[1],row_index))
        player_color = player.get_color()
        board_marble = my_row[row_index]
        board_marble_color = board_marble.get_color()
        if not board_marble_color:
            print("trying to move from an empty spot")
            return False
        if player_color != board_marble_color:
            print("you don't own this spot")
            return False
        length = len(my_row)
        follow_index = row_index + 1
        while follow_index < length:
            board_marble = my_row[follow_index]
            if not board_marble.get_color():
                follow_index += 1
            else:
                print("invalid move following spots not empty ")
                return False

        current_marble = my_row[row_index]
        previous_index = row_index - 1
        empty_marble = Marble(None)
        my_row[row_index] = empty_marble
        while previous_index >= 0:
            previous_marble = my_row[previous_index]
            previous_marble_color = previous_marble.get_color()
            current_marble_color = current_marble.get_color()
            my_row[previous_index] = current_marble
            if previous_marble_color:
                current_marble = previous_marble
            else:
                print("got to an empty space")
                break
            previous_index -= 1

        # this means a marble was bumped off
        if previous_index < 0:
            captured_marble_color = current_marble.get_color()
            print("i captured a marble of color {}".format(captured_marble_color))
            if captured_marble_color == player_color:
                print("sorry you captured your own color.")
            else:
                player.captured_marble(current_marble)
        self.board.set_row(coordinates[0], my_row)
        return True


    def move_right(self, player, coordinates):
        """function determines if right move is valid and determines what
        marbles to shift right. Takes player name and coordinates as parameters and returns
        updated board after player moved right."""
        my_row = self.board.get_row(coordinates[0])
        row_index = coordinates[1]
        print("moving right from row {} column {}".format(coordinates[0], row_index))
        player_color = player.get_color()
        board_marble = my_row[row_index]
        board_marble_color = board_marble.get_color()
        if not board_marble_color:
            print("trying to move from an empty spot")
            return False
        if player_color != board_marble_color:
            print("you don't own this spot")
            return False
        length = len(my_row)
        index = 0
        while index < row_index:
            board_marble = my_row[index]
            if not board_marble.get_color():
                index += 1
            else:
                print("invalid move preceding spots are not empty ")
                return False

        current_marble = my_row[row_index]
        next_index = row_index + 1
        empty_marble = Marble(None)
        my_row[row_index] = empty_marble

        while next_index < length:
            next_marble = my_row[next_index]
            next_marble_color = next_marble.get_color()
            current_marble_color = current_marble.get_color()
            my_row[next_index] = current_marble
            if next_marble_color:
                current_marble = next_marble
            else:
                print("got to an empty space")
                break
            next_index += 1
        # this means a marble was bumped off

        if next_index == length:
            captured_marble_color = current_marble.get_color()
            if captured_marble_color == player_color:
                print("sorry you captured your own color.")
            else:
                player.captured_marble(current_marble)
        self.board.set_row(coordinates[0], my_row)
        return True

    def move_backward(self, player, coordinates):
        """determines if backward move is valid and determines which marbles to
        shift downward in grid. Takes the player name and coordinates as parameters
        to determine if move is valid."""
        my_row = self.board.get_column(coordinates[1])
        row_index = coordinates[0]
        player_color = player.get_color()
        board_marble = my_row[row_index]
        board_marble_color = board_marble.get_color()
        if not board_marble_color:
            print("trying to move from an empty spot")
            return False
        if player_color != board_marble_color:
            print("you don't own this spot")
            return False
        length = len(my_row)
        index = 0
        while index < row_index:
            board_marble = my_row[index]
            if not board_marble.get_color():
                index += 1
            else:
                print("invalid move preceding spots are not empty ")
                return False

        current_marble = my_row[row_index]
        next_index = row_index + 1
        empty_marble = Marble(None)
        my_row[row_index] = empty_marble

        while next_index < length:
            next_marble = my_row[next_index]
            next_marble_color = next_marble.get_color()
            current_marble_color = current_marble.get_color()
            my_row[next_index] = current_marble
            if next_marble_color:
                current_marble = next_marble
            else:
                print("got to an empty space")
                break
            next_index += 1
        # this means a marble was bumped off

        if next_index == length:
            captured_marble_color = current_marble.get_color()
            if captured_marble_color == player_color:
                print("sorry you captured your own color.")
            else:
                player.captured_marble(current_marble)
        self.board.set_column(coordinates[1], my_row)
        return True

    def move_forward(self,player, coordinates):
        """takes player name and coordinates as parameter to determine if move is valid
        and determines which marbles to shift forward in grid. """
        my_row = self.board.get_column(coordinates[1])
        row_index = coordinates[0]
        player_color = player.get_color()
        board_marble = my_row[row_index]
        board_marble_color = board_marble.get_color()
        if not board_marble_color:
            print("trying to move from an empty spot")
            return False
        if player_color != board_marble_color:
            print("you don't own this spot")
            return False
        length = len(my_row)
        follow_index = row_index + 1
        while follow_index < length:
            board_marble = my_row[follow_index]
            if not board_marble.get_color():
                follow_index += 1
            else:
                print("invalid move following spots not empty ")
                return False

        current_marble = my_row[row_index]
        previous_index = row_index - 1
        empty_marble = Marble(None)
        my_row[row_index] = empty_marble
        while previous_index >= 0:
            previous_marble = my_row[previous_index]
            previous_marble_color = previous_marble.get_color()
            current_marble_color = current_marble.get_color()
            my_row[previous_index] = current_marble
            if previous_marble_color:
                current_marble = previous_marble
            else:
                print("got to an empty space")
                break
            previous_index -= 1
        # this means a marble was bumped off
        if previous_index < 0:
            captured_marble_color = current_marble.get_color()
            print("i captured a marble of color {}".format(captured_marble_color))
            time.sleep(1)
            if captured_marble_color == player_color:
                print("sorry you captured your own color.")
            else:
                player.captured_marble(current_marble)
        self.board.set_column(coordinates[1], my_row)
        return True


    def get_current_player(self,name):
        """returns the player whose turn it is. Parameter is the player's name."""
        current_turn = self.get_current_turn()
        if not current_turn:
            print("nobody has started. Setting current player to {}".format(name))
            current_player = self.get_player_by_name(name)
            current_player.make_my_turn()
        else:
            if name != current_turn:
                print("this is not your turn")
                return
            else:
                current_player = self.get_player_by_name(name)
        return current_player
    def game_stat(self):
        """prints the board and statistics of each player. """
        self.board.print_board()
        self.player_1.print_stats()
        self.player_2.print_stats()
    def run(self):
        """tests for moves."""
        player_turn = self.get_current_turn()
        print("it is {} turn".format(player_turn))
        self.make_move("Chelsea",(6,5),"F")
        player_turn = self.get_current_turn()
        print("it is {} turn".format(player_turn))
        num_white, num_black, num_red = self.get_marble_count()
        print("i got {} red marbles".format(num_red))
        print("i got {} white marbles".format(num_white))
        print("i got {} black marbles".format(num_black))
        self.make_move("Ashley", (0, 6), "B")
        self.make_move("Chelsea", (5, 5), "F")
        self.make_move("Ashley", (1, 6), "B")
        self.make_move("Chelsea", (4, 5), "F")
        self.make_move("Ashley", (2, 6), "B")
        self.make_move("Chelsea", (3, 5), "F")
        self.make_move("Ashley", (3, 6), "B")
        self.make_move("Chelsea", (2, 5), "F")
        num_white, num_black, num_red = self.get_marble_count()
        print("i got {} red marbles".format(num_red))
        print("i got {} white marbles".format(num_white))
        print("i got {} black marbles".format(num_black))
        self.game_stat()







        R = Marble('red')
        W = Marble('white')
        B = Marble('black')
        E = Marble(None)
        new_list = [R,B,R,B,R,B,R]

def main():
    player_1 = ("Ashley", c_black)
    player_2 = ("Chelsea", c_white)
    game_player = KubaGame(player_1,player_2)
    game_player.run()

if __name__ == "__main__":

    main()
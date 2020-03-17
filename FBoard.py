# Name: Kyle Bingman
# Date: 3/8/2020
# Description: Enables a game of F-Board to be played by two players.

class FBoard:
    """Sets up the board and required moves for a game of F-Board"""

    def __init__(self):
        """Establishes and initializes the board and current state of the game"""
        self._game_board = [["x", " ", " ", " ", " ", " ", " ", " "],
                            [" ", " ", " ", " ", " ", " ", " ", " "],
                            [" ", " ", " ", " ", " ", " ", " ", " "],
                            [" ", " ", " ", " ", " ", " ", " ", " "],
                            [" ", " ", " ", " ", " ", " ", " ", " "],
                            [" ", " ", " ", " ", " ", " ", " ", "o"],
                            [" ", " ", " ", " ", " ", " ", "o", " "],
                            [" ", " ", " ", " ", " ", "o", " ", "o"]]
        self._game_state = "UNFINISHED"
        self._x_location = [0, 0]

    def win_check(self):
        """Performs Needed Checks to See if the Game Has Been Won"""

        # Generate Allowable X Moves for Later
        x_check_position = self._x_location
        x_move_options = []

        # Add 1 to Both
        move_option_win_check = [x + 1 for x in x_check_position]
        x_move_options.append(move_option_win_check)

        # Subtract 1 from Both
        move_option_win_check = [x - 1 for x in x_check_position]
        x_move_options.append(move_option_win_check)

        # +1 / - 1
        move_option_win_check2 = []
        move_option_win_check2.append(x_check_position[0] + 1)
        move_option_win_check2.append(x_check_position[1] - 1)
        x_move_options.append(move_option_win_check2)

        # - 1 / + 1
        move_option_win_check3 = []
        move_option_win_check3.append(x_check_position[0] - 1)
        move_option_win_check3.append(x_check_position[1] + 1)
        x_move_options.append(x_check_position)
        #print("Win Check - Allowed X Moves:", x_move_options)

        # Check of X Has Won
        if self._game_board[7][7] == "x":
            self._game_state = "X_WON"
            return True

        # Check if No Legal Moves for X / If O Has Won
        o_checks = []
        x_is_done = 0

        # Sees if the X Moves Are In Range
        for coordinate in range(4):
            x_coord = x_move_options[coordinate][0]
            y_coord = x_move_options[coordinate][1]

            if x_coord >= 0 and x_coord <= 7:
                if y_coord >= 0 and y_coord <= 7:
                    o_checks.append([x_coord, y_coord])
                    #print(o_checks)
                elif y_coord <= -1 or y_coord >= 8:
                    x_is_done += 1

            elif x_coord <= -1 or x_coord >= 8:
                if y_coord <= -1 or y_coord >= 8:
                    x_is_done += 1
                    #print("Out of Bounds:", x_is_done)

        # Sees if the X Move Is To A Space With An O Already
        for coordinate in range(len(o_checks)):
            x_coord2 = o_checks[coordinate][0]
            y_coord2 = o_checks[coordinate][1]

            if self._game_board[x_coord2][y_coord2] == "o":
                x_is_done += 1
                #print("Space is Filled:", x_is_done)

        #print("X Out of  Options Count", x_is_done)

        # Figures Out if X Can't Move Anywhere Else
        if x_is_done == 4:
            self._game_state = "O_WON"
            #print(game_state)

        # Otherwise Game Unfinished
        if self._game_state == "UNFINISHED":
            return True

    def move_x(self, row_x, column_x):
        """Moves the X Piece"""

        current_x_pos = self._x_location
        desired_move = [row_x, column_x]
        allowed_moves = []

        # Check if Game Has Already Been Won
        if self._game_state == "X_WON" or self._game_state == "O_WON":
            #print("Test: Quitting Now - Game Over")
            return False

        # Check if O is Occupying Space
        if self._game_board[row_x][column_x] == "o":
            #print("Space is occupied by O")
            return False

        if row_x < 0 or row_x > 7 or column_x < 0 or column_x > 7:
            return False

        # Check If Move Is Allowed and Make Move If It Is
        else:
             #Generate Allowed Moves
            # Add 1 to Both
            move_option = [x + 1 for x in current_x_pos]
            allowed_moves.append(move_option)

             # Subtract 1 from Both
            move_option = [x -1 for x in current_x_pos]
            allowed_moves.append(move_option)

            # +1 / - 1
            move_option2 = []
            move_option2.append(current_x_pos[0] + 1)
            move_option2.append(current_x_pos[1] - 1)
            allowed_moves.append(move_option2)

            # - 1 / + 1
            move_option3 = []
            move_option3.append(current_x_pos[0] - 1)
            move_option3.append(current_x_pos[1] + 1)
            allowed_moves.append(move_option3)
            #print("Allowed Moves:", allowed_moves)

            # Check if Desired Move in Allowed Moves
            #print("Desired Move:", desired_move)
            if desired_move in allowed_moves:
                #print("Move is Allowed")

                # Clear Previous X Position
                self._game_board[self._x_location[0]][self._x_location[1]] = " "

                # Make Move
                self._game_board[row_x][column_x] = "x"

                # Update Current X Position
                current_x_pos = [row_x, column_x]
                self._x_location = current_x_pos
                #print("New X Position Is:", current_x_pos)
                #print("self._x_location is now", self._x_location)
                #print(self._game_board)

                # Clear Allowed Moves
                allowed_moves.clear()

                # Check for Win
                self.win_check()
                return True

            else:
                #print("Move is Not Allowed")
                return False

    def move_o(self, row1_o, column1_o, row2_o, column2_o):
        """Moves the O Piece"""

        stated_current_o = [row1_o, column1_o]
        desired_o_location = [row2_o, column2_o]
        allowed_o_moves = []

        # Check if Game Already Won
        if self._game_state == "X_WON" or self._game_state == "O_WON":
            #print("Test: Quitting Now - Game Over")
            return False

        if row2_o < 0 or row2_o > 7 or column2_o < 0 or column2_o > 7:
            return False

        # Check to make sure there's an O to move
        if self._game_board[row1_o][column1_o] != "o":
            #print("Test: Not an O there to move")
            return False

        # Check if Desired Space to Move is Occupied
        if self._game_board[row2_o][column2_o] == "o" or self._game_board[row2_o][column2_o] == "x":
            #print("Space is occupied already by an X or O")
            return False

        # Check if Move is Allowed and Make Move If it Is
        else:
            # Generate Allowed Moves for O
            # Subtract 1 from Both
            move_option_o = [x - 1 for x in stated_current_o]
            allowed_o_moves.append(move_option_o)
            #print(allowed_o_moves)

            # +1 / - 1
            move_option_o2 = []
            move_option_o2.append(stated_current_o[0] + 1)
            move_option_o2.append(stated_current_o[1] - 1)
            allowed_o_moves.append(move_option_o2)
            #print(allowed_o_moves)

            # - 1 / + 1
            move_option_o3 = []
            move_option_o3.append(stated_current_o[0] - 1)
            move_option_o3.append(stated_current_o[1] + 1)
            allowed_o_moves.append(move_option_o3)
            #print("Allowed Moves:", allowed_o_moves)

            # Check if Desired Move in Allowed Moves
            #print("Desired Move:", desired_o_location)
            if desired_o_location in allowed_o_moves:
                #print("Move is Allowed")

                # Clear Previous 0 Position
                self._game_board[stated_current_o[0]][stated_current_o[1]] = " "

                # Make Move
                self._game_board[row2_o][column2_o] = "o"
                #print(self._game_board)

                # Clear Allowed Moves
                allowed_o_moves.clear()
                #print(allowed_o_moves)

                # Check for Win
                self.win_check()
                return True

    def get_game_state(self):
        """Returns the current state of the game: UNFINISHED, X_WON, or O_WON"""
        return self._game_state
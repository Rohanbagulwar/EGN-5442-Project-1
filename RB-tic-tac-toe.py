class TicTacToe:
    """
    simple tic tac toe 3 x 3 board game

    how use:
        game = TicTacToe()
        game.play()  # start interactive game loop with prompt
    """

    BOARD_SIDE = 3
    EMPTY_SYMBOL = " "

    def __init__(self):
        # prepare empty board with blanks
        self.play_area = []
        for row_counter in range(self.BOARD_SIDE):
            temp_row = []
            for col_counter in range(self.BOARD_SIDE):
                temp_row.append(self.EMPTY_SYMBOL)
            self.play_area.append(temp_row)

    def display_board(self):
        # print column headers
        header_line = "|R\\C| "

        
        for col_number in range(self.BOARD_SIDE):
            header_line += str(col_number) + " | "
        print(header_line)

        # print underline separator matching header length
        separator = "-" * len(header_line)
        print(separator)

        # print rows with indices and board cells
        for row_number in range(self.BOARD_SIDE):
            line_print = "| " + str(row_number) + " | "
            for col_number in range(self.BOARD_SIDE):
                line_print += self.play_area[row_number][col_number] + " | "
            print(line_print)
            print(separator)

    def clear_board(self):
        # set every spot to empty symbol
        for row_index in range(self.BOARD_SIDE):
            for col_index in range(self.BOARD_SIDE):
                self.play_area[row_index][col_index] = self.EMPTY_SYMBOL

    def input_valid(self, row, col):
        # check if coordinates are on board and spot free
        if row < 0 or row >= self.BOARD_SIDE:
            return False
        if col < 0 or col >= self.BOARD_SIDE:
            return False
        if self.play_area[row][col] != self.EMPTY_SYMBOL:
            return False
        return True

    def is_board_full(self):
        # returns True if no spot empty found
        for r in range(self.BOARD_SIDE):
            for c in range(self.BOARD_SIDE):
                if self.play_area[r][c] == self.EMPTY_SYMBOL:
                    return False
        return True

    def has_won(self, mark):
        # check for mark winning any row
        for r in range(self.BOARD_SIDE):
            is_winner = True
            for c in range(self.BOARD_SIDE):
                if self.play_area[r][c] != mark:
                    is_winner = False
                    break
            if is_winner:
                return True

        # check for mark winning any column
        for c in range(self.BOARD_SIDE):
            is_winner = True
            for r in range(self.BOARD_SIDE):
                if self.play_area[r][c] != mark:
                    is_winner = False
                    break
            if is_winner:
                return True

        # check major diagonal
        is_winner = True
        for i in range(self.BOARD_SIDE):
            if self.play_area[i][i] != mark:
                is_winner = False
                break
        if is_winner:
            return True

        # check both sides of diagonal
        is_winner = True
        for i in range(self.BOARD_SIDE):
            if self.play_area[i][self.BOARD_SIDE - 1 - i] != mark:
                is_winner = False
                break
        if is_winner:
            return True

        return False

    def game_finished(self, mark):
        # returns True if either player wins or board is filled than draw
        if self.has_won(mark):
            return True
        if self.is_board_full():
            return True
        return False

    def play(self):
        ## Main driver code
        # run interactive game while loop
        self.clear_board()
        print("New Game: X goes first.\n")
        self.display_board()

        current_mark = "X"
        while True:
            print(f"\n{current_mark}'s turn.")
            user_move = input(
                f"Where do you want your {current_mark} placed?\n"
                "Please enter row number and column number separated by a comma.\n"
            )

            try:
                row_str, col_str = user_move.split(",")
                row_input = int(row_str.strip())
                col_input = int(col_str.strip())
                print(f"You have entered row #{row_input}\n\tand column #{col_input}\n")
                print("Thank you for your selection.")
            except Exception:
                print("Invalid input format. Try again.")
                continue

            if not self.input_valid(row_input, col_input):
                if 0 <= row_input < self.BOARD_SIDE and 0 <= col_input < self.BOARD_SIDE:
                    print("That cell is already taken.")
                else:
                    print(
                        "Invalid entry: try again.\n"
                        "Row & column numbers must be either 0, 1, or 2."
                    )
                continue

            self.play_area[row_input][col_input] = current_mark
            self.display_board()

            if self.has_won(current_mark):
                print(f"\n{current_mark} IS THE WINNER!!!")
                break
            if self.is_board_full():
                print("\nDRAW! NOBODY WINS!")
                break

            # flip turn
            current_mark = "O" if current_mark == "X" else "X"

        reply = input("\n Another game? Enter Y or y for yes.\n")
        if reply.lower() == "y":
            self.play()
        else:
            print("Thank you for playing!")



if __name__ == "__main__":
    ## Start of the code.
    game_instance = TicTacToe()
    game_instance.play()

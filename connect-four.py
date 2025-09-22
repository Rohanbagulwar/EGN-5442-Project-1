class ConnectFour:
    """
    simple connect four game on 7-column by 6-row board

    how use:
        game = ConnectFour()
        game.play()   # start interactive game 
    """

    BOARD_ROWS = 6
    BOARD_COLUMNS = 7
    EMPTY_SLOT = " "

    def __init__(self):
        # prepare empty board with blanks
        self.play_area = []
        for r in range(self.BOARD_ROWS + 1):
            temp_row = []
            for c in range(self.BOARD_COLUMNS + 1):
                temp_row.append(self.EMPTY_SLOT)
            self.play_area.append(temp_row)

    def display_board(self):
        # print rows from top (6) down to 1
        for row_number in range(self.BOARD_ROWS, 0, -1):
            line_print = "| " + str(row_number) + " | "
            for col_number in range(1, self.BOARD_COLUMNS + 1):
                line_print += self.play_area[row_number][col_number] + " | "
            print(line_print)
            separator = "-" * len(line_print)
            print(separator)

        # print column header a to g
        header_line = "|R/C| "
        for i in range(self.BOARD_COLUMNS):
            header_line += chr(ord('a') + i) + " | "
        print(header_line)

    def is_valid_column(self, col):
        # Check if column is within bounds and not full
        col_index = self.col_letter_to_index(col)
        if col_index < 1 or col_index > self.BOARD_COLUMNS:
            return False
        # if top row at that column is empty, move is valid
        if self.play_area[self.BOARD_ROWS][col_index] == self.EMPTY_SLOT:
            return True
        else:
            return False

    def col_letter_to_index(self, col_letter):
        # Convert col letter a-g to index 1-7
        return ord(col_letter.lower()) - ord('a') + 1

    def find_lowest_empty_row(self, col_index):
        # Find lowest row in column that is empty
        for row in range(1, self.BOARD_ROWS + 1):
            if self.play_area[row][col_index] == self.EMPTY_SLOT:
                return row
        return None

    def is_board_full(self):
        # Board full if no columns have free space (top row filled)
        for col in range(1, self.BOARD_COLUMNS + 1):
            if self.play_area[self.BOARD_ROWS][col] == self.EMPTY_SLOT:
                return False
        return True

    def has_won(self, mark):
        row_count = self.BOARD_ROWS
        col_count = self.BOARD_COLUMNS

        # Check horizontal (row) for 4 in a row
        for r in range(1, row_count + 1):
            for c in range(1, col_count - 2):
                if (self.play_area[r][c] == mark and
                    self.play_area[r][c+1] == mark and
                    self.play_area[r][c+2] == mark and
                    self.play_area[r][c+3] == mark):
                    return True

        # Check vertical for 4 in a row
        for c in range(1, col_count + 1):
            for r in range(1, row_count - 2):
                if (self.play_area[r][c] == mark and
                    self.play_area[r+1][c] == mark and
                    self.play_area[r+2][c] == mark and
                    self.play_area[r+3][c] == mark):
                    return True

        # Check diagonal up-right
        for r in range(1, row_count - 2):
            for c in range(1, col_count - 2):
                if (self.play_area[r][c] == mark and
                    self.play_area[r+1][c+1] == mark and
                    self.play_area[r+2][c+2] == mark and
                    self.play_area[r+3][c+3] == mark):
                    return True

        # Check diagonal up-left
        for r in range(1, row_count - 2):
            for c in range(4, col_count + 1):
                if (self.play_area[r][c] == mark and
                    self.play_area[r+1][c-1] == mark and
                    self.play_area[r+2][c-2] == mark and
                    self.play_area[r+3][c-3] == mark):
                    return True

        return False

    def game_finished(self, mark):
        if self.has_won(mark):
            return True
        if self.is_board_full():
            return True
        return False

    def get_available_positions(self):
        # returns list of available positions as strings like 'a1', 'b1', 'c2' etc.
        positions = []
        for col in range(1, self.BOARD_COLUMNS + 1):
            row = self.find_lowest_empty_row(col)
            if row is not None:
                positions.append(chr(ord('a') + col - 1) + str(row))
        return positions

    def play(self):
        self.play_area = []
        for r in range(self.BOARD_ROWS + 1):
            row_array = []
            for c in range(self.BOARD_COLUMNS + 1):
                row_array.append(self.EMPTY_SLOT)
            self.play_area.append(row_array)

        print("New game: X goes first.\n")
        self.display_board()

        current_mark = "X"

        while True:
            print(f"\n {current_mark}'s turn.")
            print(f'Where do you want your {current_mark} placed?')
            available_positions = self.get_available_positions()
            print(f"Available positions are: {available_positions}\n")
            user_position = input("Please enter column-letter and row-number (e.g., a1): ")
            print("Thank you for your selection")

            if len(user_position) < 2:
                print("Invalid format input. Try again.")
                continue

            col_char = user_position[0].lower()
            row_char = user_position[1:]
            if not col_char.isalpha():
                print("Invalid column letter input. Try again.")
                continue
            if not row_char.isdigit():
                print("Invalid row number input. Try again.")
                continue

            if not self.is_valid_column(col_char):
                print("Invalid column or column is full. Try other column.")
                continue

            col_index = self.col_letter_to_index(col_char)
            try:
                row_input = int(row_char)
            except:
                print("Invalid row number input. Try again.")
                continue

            lowest_row = self.find_lowest_empty_row(col_index)
            if lowest_row != row_input:
                print(f"Invalid position: You must use lowest empty row in column {col_char}. It is {lowest_row}.")
                continue

            print("Thank you for your selection.")
            self.play_area[lowest_row][col_index] = current_mark
            self.display_board()

            if self.has_won(current_mark):
                print(f"\n{current_mark} IS THE WINNER!!!")
                break

            if self.is_board_full():
                print("\n DRAW! NOBODY WINS!")
                break

            # Switch players
            current_mark = "O" if current_mark == "X" else "X"

        again = input("\n Another game (y/n)? \n")
        if again.lower() == "y":
            self.play()
        else:
            print("Thank you for playing!")


if __name__ == "__main__":
    game = ConnectFour()
    game.play()

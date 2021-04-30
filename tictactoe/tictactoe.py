import os

os.system("clear")


class Board():
    def __init__(self):
        self.cells = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", ]

    #display of the board
    def display(self):
        print(" %s | %s | %s " % (self.cells[1], self.cells[2], self.cells[3]))
        print("-----------")
        print(" %s | %s | %s " % (self.cells[4], self.cells[5], self.cells[6]))
        print("-----------")
        print(" %s | %s | %s " % (self.cells[7], self.cells[8], self.cells[9]))

    #update the cell
    def update_cell(self, cell_no, player):
        if self.cells[cell_no] == " ":
            self.cells[cell_no] = player

    #way to win and enter the number fills in the slot
    def is_winner(self, player):
        if self.cells[1] == player and self.cells[2] == player and self.cells[3] == player:
            return True

        if self.cells[1] == player and self.cells[5] == player and self.cells[9] == player:
            return True

        if self.cells[3] == player and self.cells[5] == player and self.cells[7] == player:
            return True

        if self.cells[1] == player and self.cells[4] == player and self.cells[7] == player:
            return True

        if self.cells[3] == player and self.cells[6] == player and self.cells[9] == player:
            return True

        if self.cells[4] == player and self.cells[5] == player and self.cells[6] == player:
            return True

        if self.cells[7] == player and self.cells[8] == player and self.cells[9] == player:
            return True

        return False

    def is_tie(self):
        used_cells = 0
        for cell in self.cells:
            if cell != " ":
                used_cells += 1
        if used_cells == 9:
            return True
        else:
            return False

    def reset(self):
        self.cells = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", ]

    def ai_move(self, player):

        # Random
        for i in range(1, 10):
            if self.cells[i] == " ":
                self.update_cell(i, player)
                break


board = Board()

class Header():
    def print_Header(self):
        print("Welcome to Tic-Tac-Toe\n")

header = Header()

class Refresh(Board,Header):
    def refresh_screen(self):
        os.system("clear")

        header.print_Header()

        board.display()

refresh = Refresh()
while True:
    #refresh_screen()
    refresh.refresh_screen()
    x_choice = int(input("\nX) please chose 1-9. > "))

    # update cell
    board.update_cell(x_choice, "X")

    # refresh screen
    # check for winner

    if board.is_winner("X"):
        print("\nX wins!\n")
        play_again = input("Want to play again? (Y/N) > ").upper()
        if play_again == "Y":
            board.reset()
            continue
        else:
            break
    #check for tie
    if board.is_tie():
        print("\nTie Game!\n")
        play_again = input("Want to play again? (Y/N) > ").upper()
        if play_again == "Y":
            board.reset()
            continue
        else:
            break

    # o_choice = int(input("\nO) please chose 1-9. > "))
    # board.update_cell(o_choice, "O")

    #ai move
    board.ai_move("O")
    refresh.refresh_screen()
    #refesh the screen

    # check for winner
    if board.is_winner("O"):
        print("\n0 wins!\n")
        play_again = input("Want to play again? (Y/N) > ").upper()
        if play_again == "Y":
            board.reset()
            continue
        else:
            break
    # check for tie
    if board.is_tie():
        print("\nTie Game!\n")
        play_again = input("Want to play again? (Y/N) > ").upper()
        if play_again == "Y":
            board.reset()
            continue
        else:
            break

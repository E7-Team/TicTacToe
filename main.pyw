import tkinter as tk
import tkinter.messagebox
import random
import pygame

class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic-Tac-Toe")
        self.board = [" "]*9  # Empty board
        self.buttons = []
        self.current_player = "X"
        self.game_over = False

        pygame.mixer.init()
        pygame.mixer.music.load("music.mp3")
        pygame.mixer.music.play(-1)  # Play background music indefinitely

        self.create_board()

    def create_board(self):
        for i in range(3):
            for j in range(3):
                button = tk.Button(self.master, text=" ", font=("Arial", 30), width=6, height=3,
                                   command=lambda row=i, col=j: self.click(row, col))
                button.grid(row=i, column=j, padx=5, pady=5)
                self.buttons.append(button)

    def click(self, row, col):
        index = row * 3 + col
        if not self.game_over and self.board[index] == " ":
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player, font=("Arial", 30),
                                       fg="red" if self.current_player == "X" else "blue")
            if self.check_winner():
                tkinter.messagebox.showinfo("Winner", f"Player {self.current_player} wins!")
                self.game_over = True
            elif " " not in self.board:
                tkinter.messagebox.showinfo("Tie", "It's a tie!")
                self.game_over = True
            else:
                self.change_player()
                if self.current_player == "O":
                    self.ai_move()

    def change_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def ai_move(self):
        empty_cells = [i for i, cell in enumerate(self.board) if cell == " "]
        if empty_cells:
            move = random.choice(empty_cells)
            self.board[move] = self.current_player
            self.buttons[move].config(text=self.current_player, font=("Arial", 30),
                                       fg="red" if self.current_player == "X" else "red")
            if self.check_winner():
                tkinter.messagebox.showinfo("Winner", f"Player {self.current_player} wins!")
                self.game_over = True
            elif " " not in self.board:
                tkinter.messagebox.showinfo("Tie", "It's a tie!")
                self.game_over = True
            else:
                self.change_player()

    def check_winner(self):
        winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != " ":
                return True
        return False


root = tk.Tk()
game = TicTacToe(root)
root.mainloop()

from PIL import Image, ImageTk

import time
import itertools
import random
import tkinter as tk
from tkinter import messagebox
from pathlib import Path

ROOT = Path(__file__).parent
ASSETS_FOLDER = ROOT / "assets"


class GameStatusChecker:
    # HORIZONTAL_CHECKS = [
    #     [0, 1, 2],
    #     [3, 4, 5],
    #     [6, 7, 8]
    # ]

    # VERTICAL_CHECKS = [
    #     [0, 3, 6],
    #     [1, 4, 7],
    #     [2, 5, 8]
    # ]

    # DIAGONAL_CHECKS = [
    #     [0, 4, 8],
    #     [2, 4, 6]
    # ]
    def __init__(self):
        self._winner = None

    def check(self, matrix) -> tuple[str, str | None]:
        if (
            self._check_horizontal(matrix)
            or self._check_vertical(matrix)
            or self._check_diagonal(matrix)
            or self._draw(matrix)
        ):
            return True, self._winner

        return False, None

    def _check_horizontal(self, matrix):
        for row in matrix:
            # Match all the columns in the target row
            if self._match_all(row):
                return True

        return False

    def _check_vertical(self, matrix):
        # Build values by iterating by col first
        for col in range(len(matrix[0])):
            values = []

            for row in range(len(matrix)):
                values.append(matrix[row][col])

            if self._match_all(values):
                return True

        return False

    def _check_diagonal(self, matrix):
        def check_diagonal(matrix):
            values = []

            for row in range(len(matrix)):
                # Col must match row index
                col = row
                values.append(matrix[row][col])

            if self._match_all(values):
                return True

            return False

        # Check original matrix or reversed matrix for the other diagonal possibility
        return check_diagonal(matrix) or check_diagonal(list(reversed(matrix)))

    def _draw(self, matrix):
        for row in matrix:
            if not all(row):
                return False

        self._winner = None

        return True

    def _match_all(self, values):
        target = values[0]

        for value in values[1:]:
            if not value or value != target:
                return False

        self._winner = target

        return True


class TicTacToe:
    BUTTON_WIDTH = 150
    BUTTON_HEIGHT = 100
    BUTTON_BORDER_STYLE = "ridge"

    ICON_WIDTH = 40
    ICON_HEIGHT = 40

    COMPUTER_VALUE = "X"
    USER_VALUE = "O"

    def __init__(self):
        self._window = tk.Tk()
        self._window.title("Tic Tac Toe")

        self._x_icon = None
        self._o_icon = None
        self._empty_icon = None

        self._game_over = False
        self._widgets_matrix = []

        self._game_status_checker = GameStatusChecker()

    def run(self):
        self._load_icons()
        self._build_grid()
        self._window.after(1000, self._computer_choice)

        self._window.mainloop()

    def _load_icons(self):
        def load_icon(image_path):
            image = Image.open(ASSETS_FOLDER / image_path)
            image = image.resize((self.ICON_WIDTH, self.ICON_HEIGHT))

            return ImageTk.PhotoImage(image)

        self._x_icon = load_icon(ASSETS_FOLDER / "X.png")
        self._o_icon = load_icon(ASSETS_FOLDER / "O.png")
        self._empty_icon = tk.PhotoImage(width=1, height=1)

    def _build_grid(self):
        grid_rows = 3
        grid_columns = 3

        for row in range(grid_rows):
            column_widgets = []

            for column in range(grid_columns):
                button = tk.Button(
                    self._window,
                    width=self.BUTTON_WIDTH,
                    height=self.BUTTON_HEIGHT,
                    relief=self.BUTTON_BORDER_STYLE,
                    image=self._empty_icon,
                )

                # Adds a custom attribute for further lookup
                button.value = None

                # button value is saved in the lambda context on definition
                # due to the "b" attibution
                button.configure(command=lambda b=button: self._user_choice(b))
                button.grid(row=row, column=column)

                column_widgets.append(button)

            # For each row, append its column widgets, this will create a 2D matrix
            self._widgets_matrix.append(column_widgets)

    def _user_choice(self, button: tk.Button):
        if self._game_over:
            return

        self._mark_choice(button, value=self.USER_VALUE, player="USER")

        if not self._game_over:
            self._window.after(800, self._computer_choice)

    def _mark_choice(self, button: tk.Button, value, player):
        icon = self._x_icon if value == "X" else self._o_icon

        button.configure(
            image=icon,
            command=lambda: None,
        )
        button.value = value

        self._check_game_status(last_move_by=player)

    def _check_game_status(self, last_move_by):
        values = []

        for row in self._widgets_matrix:
            values.append([col.value for col in row])

        game_over, winner = self._game_status_checker.check(values)

        if game_over:
            if not winner:
                messagebox.showwarning("Tic Tac Toe", "Draw! Try again!")
                return

            if last_move_by == "COMPUTER":
                messagebox.showerror("Tic Tac Toe", "You failed!")
            else:
                messagebox.showinfo("Tic Tac Toe", "You won!")

            self._game_over = True

    def _computer_choice(self):
        remaining_choices = [
            widget
            for widget in itertools.chain.from_iterable(self._widgets_matrix)
            if not widget.value
        ]

        choice = random.choice(remaining_choices)
        self._mark_choice(choice, value=self.COMPUTER_VALUE, player="COMPUTER")


if __name__ == "__main__":
    app = TicTacToe()
    app.run()

    # print(
    #     GameStatusChecker().check(
    #         [
    #             ["X", "O", "O"],
    #             ["O", "X", "O"],
    #             ["O", "O", "X"],
    #         ]
    #     )
    # )

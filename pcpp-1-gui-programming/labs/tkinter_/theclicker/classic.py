import random
import dataclasses
import tkinter as tk
from tkinter import messagebox


@dataclasses.dataclass
class Options:
    COLUMNS_COUNT: int = 5
    ROWS_COUNT: int = 5

    BUTTON_WIDTH: int = 5
    BUTTON_HEIGHT: int = 3

    MIN_NUMBER: int = 1
    MAX_NUMBER: int = 999


class ClassicClicker:
    ONE_SECOND_IN_MILLISECONDS = 1000

    def __init__(self, **options):
        self._options = Options(**options)

        self._window = tk.Tk()
        self._window.title("The Clicker")

        self._game_numbers = []
        self._next_number = None
        self._buttons_clicked = 0

        self._timer = None
        self._timer_var = tk.IntVar(value=0)
        self._timer_event_id = None

    def run(self):
        self._build_buttons()
        self._build_timer()
        self._setup()

        self._window.mainloop()

    def _build_buttons(self):
        for row in range(self._options.ROWS_COUNT):
            for col in range(self._options.COLUMNS_COUNT):
                number = self._get_random_number()
                button = tk.Button(
                    self._window,
                    text=number,
                    width=self._options.BUTTON_WIDTH,
                    height=self._options.BUTTON_HEIGHT,
                )

                # button and number values are saved in the lambda context on definition
                # due to the "b" and "n" attibution
                button.configure(command=lambda b=button, n=number: self._clicked(b, n))
                button.grid(row=row, column=col)

    def _build_timer(self):
        self._timer = tk.Button(self._window, textvariable=self._timer_var)
        self._timer.grid(
            row=self._options.ROWS_COUNT + 1,
            columnspan=self._options.COLUMNS_COUNT,
            sticky="ew",
        )
        # Start the loop
        self._timer.after(self.ONE_SECOND_IN_MILLISECONDS, self._tick)

    def _tick(self):
        self._timer_var.set(self._timer_var.get() + 1)
        self._timer_event_id = self._timer.after(
            self.ONE_SECOND_IN_MILLISECONDS, self._tick
        )

    def _setup(self):
        self._game_numbers.sort()
        self._next_number = self._game_numbers[0]
        self._buttons_count = len(self._game_numbers)

    def _get_random_number(self):
        while True:
            number = random.randint(self._options.MIN_NUMBER, self._options.MAX_NUMBER)

            if number not in self._game_numbers:
                self._game_numbers.append(number)
                return number

    def _clicked(self, button, number):
        # Disable the clicked button if it was clicked in the right order
        if number == self._next_number:
            button.configure(state="disabled")
            self._buttons_clicked += 1

            self._check_next_number()

    def _check_next_number(self):
        try:
            self._next_number = self._game_numbers[self._buttons_clicked]
        except IndexError:
            # IndexError means the user exhausted the numbers and won the game
            self._timer.after_cancel(self._timer_event_id)

            messagebox.showinfo("Congratulations", "You won!")

    def _reechedule_tick_or_game_over(self) -> bool:
        if self._timer_var.get() < 0:
            self._timer.after_cancel(self._timer_event_id)
            messagebox.showerror("What a pitty!", "You failed!")
            return True

        return False

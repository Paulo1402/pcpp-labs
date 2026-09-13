import random
import tkinter as tk
from tkinter import messagebox


class CatchMe:
    MIN_WIDTH = 300
    MIN_HEIGHT = 300

    def __init__(self):
        self._window = tk.Tk()
        self._window.geometry("500x500")

        self._button = tk.Button(
            self._window,
            text="Catch me!",
            command=self._catched,
        )
        self._button.bind("<Enter>", self._move_button)
        self._button.bind("<space>", lambda _: self._catched(cheater=True))
        self._button.bind("<Return>", lambda _: self._catched(cheater=True))

        self._button.place(x=5, y=5)

        self._cheater = False

    def run(self):
        self._window.mainloop()

    def _move_button(self, _):
        window_width = self._window.winfo_width()
        window_height = self._window.winfo_height()

        button_width = self._button.winfo_width()
        button_height = self._button.winfo_height()

        new_x = random.randint(1, window_width - button_width)
        new_y = random.randint(1, window_height - button_height)

        self._button.place(x=new_x, y=new_y)

    def _catched(self, cheater=False):
        if self._cheater:
            self._cheater = False
            return

        window_width = self._window.winfo_width()
        window_height = self._window.winfo_height()

        min_window = window_width < self.MIN_WIDTH and window_height < self.MIN_HEIGHT

        if cheater or min_window:
            messagebox.showwarning("Cheater", "That doesn't count, you cheated!")
            self._cheater = True
            return

        messagebox.showinfo("Wow", "You caught me!")


if __name__ == "__main__":
    app = CatchMe()
    app.run()

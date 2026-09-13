import tkinter as tk


class TicTacToe:
    def __init__(self):
        self._window = tk.Tk()
        self._window.title = "Tic Tac Toe"

        self._build_grid()

    def run(self):
        self._window.mainloop()
        
    def _build_grid(self):
        pass

if __name__ == "__main__":
    app = TicTacToe()
    app.run()

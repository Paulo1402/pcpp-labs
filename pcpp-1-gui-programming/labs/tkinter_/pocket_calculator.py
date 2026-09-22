import tkinter as tk
from tkinter import messagebox


class Key:
    def __init__(self, operator, calculator, label=None):
        self._operator = operator
        self._calculator = calculator

        self.label = label if label else operator

    def handle(self):
        return self._calculator.append_on_display(self._operator)


class ClearKey(Key):
    def handle(self):
        return self._calculator.clear_display()


class ResultKey(Key):
    def handle(self):
        return self._calculator.result()


class SwitchOperatorKey(Key):
    def handle(self):
        return self._calculator.switch_operator()


class PocketCalculator:
    LAYOUT_MAP = [
        ["7", "8", "9", "", "+"],
        ["4", "5", "6", "", "-"],
        ["1", "2", "3", "=", "*"],
        ["0", "C", ".", "+/-", "/"],
    ]

    SPECIAL_KEYS = ["C", "=", "+/-"]

    DEFAULT_DISPLAY_VALUE = "0"
    ERROR_DISPLAY_VALUE = "Error!"

    def __init__(self):
        self._window = tk.Tk()

        self._showing_default = True

    def run(self):
        self._build_display()
        self._build_keys()

        self._window.mainloop()

    def _build_display(self):
        display_frame = tk.Frame(self._window)
        display_frame.pack()

        self._display_var = tk.StringVar(value=self.DEFAULT_DISPLAY_VALUE)
        self._display = tk.Entry(
            display_frame,
            textvariable=self._display_var,
            width=15,
            font=("Arial", 24, "bold"),
        )
        self._display.pack()

    def _build_keys(self):
        keys_frame = tk.Frame(self._window)
        keys_frame.pack()

        for row in range(len(self.LAYOUT_MAP)):
            for col in range(len(self.LAYOUT_MAP[0])):
                key = self.LAYOUT_MAP[row][col]

                # Skip empty key used only for layout logic
                if not key:
                    continue

                button = tk.Button(
                    keys_frame,
                    text=key,
                    command=lambda key=key: self._handle_key(key),
                    width=3,
                    font=("Arial", 12),
                )
                button.grid(row=row, column=col)

    def _handle_key(self, key):
        if self._is_special_key(key):
            self._handle_special_key(key)
            return

        if self._showing_default:
            self._display_var.set(value="")
            self._showing_default = False

        self._append_on_display(key)

    def _is_special_key(self, key):
        return key in self.SPECIAL_KEYS

    def _handle_special_key(self, key):
        match key:
            case "C":
                self._clear_display()
            case "=":
                self._result()
            case "+/-":
                self._switch_operator()
            case _:
                raise RuntimeError("Operator not known")

    def _clear_display(self):
        self._display_var.set(value=self.DEFAULT_DISPLAY_VALUE)
        self._showing_default = True

    def _result(self):
        equation = self._display_var.get()

        try:
            result = eval(equation)
        except Exception as e:
            print(e)
            result = self.ERROR_DISPLAY_VALUE
        finally:
            self._display_var.set(result)

    def _switch_operator(self):
        current = self._display_var.get()

        # 0 cannot be negative
        if current == "0":
            return

        if current.startswith("-"):
            new_value = current[1:]
        else:
            new_value = "-" + current

        self._display_var.set(new_value)

    def _append_on_display(self, value):
        current = self._display_var.get()
        new_value = current + value

        if current == self.ERROR_DISPLAY_VALUE:
            new_value = value

        self._display_var.set(new_value)


if __name__ == "__main__":
    app = PocketCalculator()
    app.run()

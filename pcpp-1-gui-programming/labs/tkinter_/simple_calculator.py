import operator
import tkinter as tk
from tkinter import messagebox


class Calculator:
    OPERATORS = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv,
    }

    DEFAULT_OPERATOR = "+"

    def __init__(self):
        self._window = tk.Tk()

        self._operation_switch = None
        self._input_1_var = None
        self._input_2_var = None
        
    def run(self):
        self._build_operators()
        self._build_inputs()
        self._build_evaluate_button()

        self._window.mainloop()

    def _build_operators(self):
        self._operation_switch = tk.StringVar(value=self.DEFAULT_OPERATOR)

        for row, operation in enumerate(self.OPERATORS.keys()):
            button = tk.Radiobutton(
                self._window,
                text=operation,
                variable=self._operation_switch,
                value=operation,
            )
            button.grid(row=row, column=1)

    def _build_inputs(self):
        self._input_1_var = tk.StringVar()
        self._input_2_var = tk.StringVar()

        input_1 = tk.Entry(self._window, textvariable=self._input_1_var)
        input_2 = tk.Entry(self._window, textvariable=self._input_2_var)

        input_1.grid(row=1, column=0)
        input_2.grid(row=1, column=2)

    def _build_evaluate_button(self):
        button = tk.Button(self._window, text="Evaluate", command=self._evaluate)
        button.grid(row=4, column=1)

    def _evaluate(self):
        try:
            value_1 = float(self._input_1_var.get())
            value_2 = float(self._input_2_var.get())
        except ValueError as e:
            messagebox.showerror(
                "Invalid values", "Please, ensure that both values are valid numbers!"
            )
            return

        operation = self._operation_switch.get()
        operation_func = self.OPERATORS.get(operation)

        try:
            result = operation_func(value_1, value_2)

            if result.is_integer():
                result = int(result)

            messagebox.showinfo("Result", f"Equation result: {result}")
        except ZeroDivisionError:
            messagebox.showerror(
                "Zero division error",
                "The second value can't be 0 for division operations!",
            )
        except Exception as e:
            messagebox.showerror("Something went wrong", f"Error: {e}")


if __name__ == "__main__":
    app = Calculator()
    app.run()

import dataclasses
import tkinter as tk
from tkinter import messagebox

from .classic import ClassicClicker, Options as ClassicOptions


@dataclasses.dataclass
class Options(ClassicOptions):
    WRONG_CLICK_PENALTY: int = 5
    TIME_BOUND_IN_SECONDS: int = 60


class TimeBoundClicker(ClassicClicker):
    def __init__(self, **options):
        super().__init__()
  
        self._options = Options(**options)
        self._timer_var = tk.IntVar(value=self._options.TIME_BOUND_IN_SECONDS)

    def _tick(self):
        # Subtract 1 second each tick
        self._timer_var.set(self._timer_var.get() - 1)
        self._reschedule_tick_or_game_over()

    def _clicked(self, button, number):
        if number == self._next_number:
            super()._clicked(button, number)
            return

        self._wrong_click()

    def _wrong_click(self):
        # Cancel the next update to avoid bugs
        self._timer.after_cancel(self._timer_event_id)

        self._timer_var.set(self._timer_var.get() - self._options.WRONG_CLICK_PENALTY)
        self._reschedule_tick_or_game_over()

    def _reschedule_tick_or_game_over(self):
        timer_value = self._timer_var.get()

        if timer_value > 0:
            # Reeschedule tick
            self._timer_event_id = self._timer.after(
                self.ONE_SECOND_IN_MILLISECONDS, self._tick
            )
            return

        # Cancel timer if there's any
        if self._timer_event_id:
            self._timer.after_cancel(self._timer_event_id)

        messagebox.showerror("What a pitty!", "You failed!")

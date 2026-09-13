import tkinter as tk


class TrafficLights:
    PHASES = (
        (True, False, False),
        # (True, True, False), # Not used in Brazil
        (False, False, True),
        (False, True, False),
    )
    COLORS = ["red", "yellow", "green"]

    LIGHT_RADIUS = 50
    LIGHT_GAP = 10
    LIGHT_X_REFERENCE = 75
    LIGHT_Y_REFERENCE = 65

    def __init__(self):
        self._window = tk.Tk()

        self._canvas = tk.Canvas(self._window, bg="dimgray", width=150, height=350)
        self._canvas.pack()

        self._next_button = tk.Button(
            self._window, text="Next", command=self._next_light
        )
        self._next_button.pack()

        self._quit_button = tk.Button(
            self._window, text="Quit", command=lambda: self._window.destroy()
        )
        self._quit_button.pack()

        self._phase_index = 0

    def run(self):
        self._draw_lights()
        self._window.mainloop()

    def _next_light(self):
        self._phase_index += 1

        if self._phase_index >= len(self.PHASES):
            self._phase_index = 0

        self._draw_lights()

    def _draw_lights(self):
        self._canvas.delete("all")

        phase = self.PHASES[self._phase_index]

        x = self.LIGHT_X_REFERENCE
        y = self.LIGHT_Y_REFERENCE

        for state, color in zip(phase, self.COLORS):
            self._canvas.create_oval(
                x - self.LIGHT_RADIUS,
                y - self.LIGHT_RADIUS,
                x + self.LIGHT_RADIUS,
                y + self.LIGHT_RADIUS,
                outline="black",
                fill=color if state else "gray",
                width=2,
            )

            # y => current value + 2x radius value + light gap
            y = y + (self.LIGHT_RADIUS * 2) + self.LIGHT_GAP


if __name__ == "__main__":
    app = TrafficLights()
    app.run()

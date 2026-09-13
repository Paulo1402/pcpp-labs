import tkinter
from tkinter import messagebox


def clicked():
    messagebox.showinfo("info", "some\ninfo")


window = tkinter.Tk()
button_1 = tkinter.Button(window, text="Show info", command=clicked)
button_1.pack()
button_2 = tkinter.Button(window, text="Quit", command=window.destroy)
button_2.pack()
label = tkinter.Label(window, text="Label")
window.bind("a", lambda event: print(event))
window.mainloop()

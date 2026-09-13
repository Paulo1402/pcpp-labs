import tkinter
from tkinter import messagebox


def Click():
    replay = messagebox.askquestion("Quit?", "Are you sure?")
    if replay == "yes":
        skylight.destroy()


skylight = tkinter.Tk()
skylight.title("Skylight")
button = tkinter.Button(skylight, text="Bye!", command=Click)
button.place(x=10, y=10)
button_2 = tkinter.Button(skylight, text="Bye!", command=Click)
button_2.pack()
skylight.mainloop()

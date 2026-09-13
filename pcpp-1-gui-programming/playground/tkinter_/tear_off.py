import tkinter as tk
from tkinter import messagebox


def about_app():
    messagebox.showinfo("App", "The application\nthat does nothing")


def are_you_sure():
    if messagebox.askyesno("", "Are you sure you want to quit the App?"):
        window.destroy()


window = tk.Tk()

main_menu = tk.Menu(window)
window.config(menu=main_menu)
# we don't want the tear-off here
sub_menu_file = tk.Menu(main_menu, tearoff=0)
main_menu.add_cascade(label="File", menu=sub_menu_file, underline=0)
sub_menu_file.add_command(label="Quit", underline=0, command=are_you_sure)
sub_menu_help = tk.Menu(main_menu)
main_menu.add_command(label="About...", command=about_app, underline=1)

window.mainloop()

import tkinter as tk

window = tk.Tk()

label = tk.Label(text="Name")
entry = tk.Entry()
entry.insert(0, "Python")

label.pack()
entry.pack()

window.mainloop()

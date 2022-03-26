# from tkinter import *
# from tkinter import ttk
#
# root = Tk()
# root.geometry("200x150")
#
# frame = Frame(root)
# frame.pack()
#
# vlist = ["Option1", "Option2", "Option3",
#          "Option4", "Option5"]
#
# Combo = ttk.Combobox(frame, values=vlist)
# Combo.set("Pick an Option")
# Combo.pack(padx=5, pady=5)
#
# root.mainloop()


# from tkinter import *
# from tkinter import ttk
#
#
# def f():
#     print(Combo.get())
#
#
# root = Tk()
# root.geometry("200x150")
#
# frame = Frame(root)
# frame.pack()
#
# vlist = ["tanlov1", "tanlov2", "tanlov3",
#          "tanlov4", "tanlov5"]
#
# Combo = ttk.Combobox(frame, values=vlist)
# Combo.set("Tanlovlar")
# Combo.pack(padx=5, pady=5)
#
# Button = Button(frame, text="Submit", command=f)
# Button.pack(padx=5, pady=5)
#
# root.mainloop()


# import tkinter as tk
# from tkinter import ttk
#
#
# class Window:
#     def __init__(self, master):
#         self.master = master
#
#         # Frame yaratish
#         self.frame = tk.Frame(self.master, width=200, height=200)
#         self.frame.pack()
#
#         self.vlist = ["Option1", "Option2", "Option3", "Option4", "Option5"]
#
#         self.combo = ttk.Combobox(self.frame, values=self.vlist, state="readonly")
#         self.combo.set("Options")
#         self.combo.place(x=20, y=50)
# root = tk.Tk()
# root.title("Class_tkinter")
#
# window = Window(root)
# root.mainloop()




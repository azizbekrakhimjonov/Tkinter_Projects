# import tkinter as tk
# import tkinter.ttk as ttk
#
#
# class Window:
#     def __init__(self, master):
#         self.master = master
#
#         frame = ttk.Frame(self.master)
#
#         label = ttk.Label(self.master, text="Hello World")
#         label.pack(padx=5, pady=5)
#
#         sizegrip = ttk.Sizegrip(frame)
#         sizegrip.pack(expand=True, fill=tk.BOTH, anchor=tk.SE)
#
#         frame.pack(padx=10, pady=10, expand=True, fill=tk.BOTH)
#
#
# root = tk.Tk()
# root.geometry("200x150")
# window = Window(root)
# root.mainloop()
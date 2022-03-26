# import tkinter as tk
#
#
# class Window:
#     def __init__(self, master):
#         self.master = master
#
#         self.frame = tk.Frame(self.master)
#         self.frame.pack(expand=True, fill=tk.BOTH)
#
#         self.label = tk.Label(self.frame, text="My NotePad")
#         self.label.pack()
#
#         self.text = tk.Text(self.frame, undo=True, height=20, width=70)
#         self.text.pack(expand=True, fill=tk.BOTH)
#
#
# root = tk.Tk()
# window = Window(root)
# root.mainloop()




# import tkinter as tk
#
# classWindow:
#     def __init__(self, master):
#         self.master = master
#
#         self.frame = tk.Frame(self.master)
#         self.frame.pack(expand=True, fill=tk.BOTH)
#
#         self.label = tk.Label(self.frame, text="My NotePad")
#         self.label.pack()
#
#         # Creating ScrollBars
#         self.scrolly = tk.Scrollbar(self.frame)
#         self.scrolly.pack(side=tk.RIGHT, fill=tk.Y)
#         self.scrollx = tk.Scrollbar(self.frame, orient=tk.HORIZONTAL)
#         self.scrollx.pack(side=tk.BOTTOM, fill=tk.X)
#
#         # Creating Text Widget
#         self.text = tk.Text(self.frame, wrap=tk.NONE, undo=True, yscrollcommand=self.scrolly.set,
#                             xscrollcommand=self.scrollx.set)
#         self.text.pack(expand=True, fill=tk.BOTH)
#
#         # Config the Scrollbars
#         self.scrolly.config(command=self.text.yview)
#         self.scrollx.config(command=self.text.xview)
#
#
#
# root = tk.Tk()
# window = classWindow(root)
# root.mainloop()










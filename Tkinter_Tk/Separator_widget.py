import tkinter as tk
import tkinter.ttk as ttk


class Window:
    def __init__(self, master):
        self.master = master

        frame = ttk.Frame(self.master)

        label = ttk.Label(frame, text="Hello World")
        label.pack(padx=5)

        separator = ttk.Separator(frame, orient=tk.HORIZONTAL)
        separator.pack(expand=True, fill=tk.X)

        label = ttk.Label(frame, text="GoodBye World")
        label.pack(padx=5)

        frame.pack(padx=10, pady=50, expand=True, fill=tk.BOTH)

root = tk.Tk()
root.geometry("200x150")
window = Window(root)
root.mainloop()





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
#         label = ttk.Label(frame, text="Hello World")
#         label.pack(padx=5, side=tk.RIGHT)
#
#         sep = ttk.Separator(frame, orient=tk.VERTICAL)
#         sep.pack(expand=True, fill=tk.Y, side=tk.RIGHT)
#
#         label = ttk.Label(frame, text="GoodBye World")
#         label.pack(padx=5, side=tk.RIGHT)
#
#         frame.pack(padx=10, pady=20, expand=True, fill=tk.BOTH)
#
#
# root = tk.Tk()
# root.geometry("200x150")
# window = Window(root)
# root.mainloop()





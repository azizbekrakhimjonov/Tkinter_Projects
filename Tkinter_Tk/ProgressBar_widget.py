import tkinter as tk
from tkinter import ttk


class Window:
    def __init__(self, master):
        self.master = master

        self.frame = ttk.Frame(self.master)

        self.progressBar = ttk.Progressbar(self.frame, mode='determinate')
        self.progressBar.pack(padx=10, pady=10)

        self.button = ttk.Button(self.frame, text="Increase",
                                 command=self.increment)
        self.button.pack(padx=10, pady=10, side=tk.LEFT)

        self.button = ttk.Button(self.frame, text="Decrease",
                                 command=self.decrement)
        self.button.pack(padx=10, pady=10, side=tk.LEFT)

        self.button = ttk.Button(self.frame, text="Display",
                                 command=self.display)
        self.button.pack(padx=10, pady=10, side=tk.LEFT)

        self.frame.pack(padx=5, pady=5)

    def increment(self):
        self.progressBar.step(20)

    def decrement(self):
        self.progressBar.step(-20)

    def display(self):
        print(self.progressBar["value"])


root = tk.Tk()
window = Window(root)
root.mainloop()








# import tkinter as tk
# from tkinter import ttk
#
#
# class Window:
#     def __init__(self, master):
#         self.master = master
#
#         self.frame = ttk.Frame(self.master)
#
#         self.progressBar = ttk.Progressbar(self.frame, mode='indeterminate')
#         self.progressBar.pack(padx=10, pady=10)
#
#         self.button = ttk.Button(self.frame, text="Start",
#                                  command=self.start)
#         self.button.pack(padx=10, pady=10, side=tk.LEFT)
#
#         self.button = ttk.Button(self.frame, text="Stop",
#                                  command=self.stop)
#         self.button.pack(padx=10, pady=10, side=tk.LEFT)
#
#         self.button = ttk.Button(self.frame, text="Display",
#                                  command=self.display)
#         self.button.pack(padx=10, pady=10, side=tk.LEFT)
#
#         self.frame.pack(padx=5, pady=5)
#
#     def start(self):
#         self.progressBar.start(interval=10)
#
#     def stop(self):
#         self.progressBar.stop()
#
#     def display(self):
#         print(self.progressBar["value"])
#
# root = tk.Tk()
# window = Window(root)
# root.mainloop()








# import tkinter as tk
# from tkinter import ttk
#
#
# class Window:
#     def __init__(self, master):
#         self.master = master
#
#         self.frame = ttk.Frame(self.master)
#
#         self.progressBar = ttk.Progressbar(self.frame, mode='determinate',
#                                            maximum=200, length=200, orient=tk.VERTICAL)
#         self.progressBar.pack(padx=10, pady=10, side=tk.RIGHT)
#
#         self.button = ttk.Button(self.frame, text="Reset",
#                                  command=self.reset)
#         self.button.pack(padx=10, pady=10, side=tk.BOTTOM)
#
#         self.button = ttk.Button(self.frame, text="Print",
#                                  command=self.display)
#         self.button.pack(padx=10, pady=10, side=tk.BOTTOM)
#
#         self.button = ttk.Button(self.frame, text="Increase",
#                                  command=self.increment)
#         self.button.pack(padx=10, pady=10, side=tk.BOTTOM)
#
#         self.button = ttk.Button(self.frame, text="Stop",
#                                  command=lambda: self.stop())
#         self.button.pack(padx=10, pady=10, side=tk.BOTTOM)
#
#         self.button = ttk.Button(self.frame, text="Start",
#                                  command=lambda: self.progressBar.start(10))
#         self.button.pack(padx=10, pady=10, side=tk.BOTTOM)
#
#         self.frame.pack(padx=5, pady=5)
#
#     def increment(self):
#         self.progressBar.step(20)
#
#     def display(self):
#         print(self.progressBar["value"])
#
#     def stop(self):
#         val = self.progressBar["value"]
#         self.progressBar.stop()
#         self.progressBar["value"] = val
#
#     def reset(self):
#         self.progressBar["value"] = 0
#
#
# root = tk.Tk()
# window = Window(root)
# root.mainloop()





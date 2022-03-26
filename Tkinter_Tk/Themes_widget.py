import tkinter as tk
import tkinter.ttk as ttk


class Window:
    def __init__(self, master):
        s = ttk.Style()
        print(s.theme_names())


root = tk.Tk()
window = Window(root)
root.mainloop()


# import tkinter as tk
# import tkinter.ttk as ttk
#
#
# class Window:
#     def __init__(self, master):
#         s = ttk.Style()
#         print(s.theme_use())
#
#
# root = tk.Tk()
# window = Window(root)
# root.mainloop()


# import tkinter as tk
# import tkinter.ttk as ttk
#
#
# class Window:
#     def __init__(self, master):
#         self.master = master
#
#         style = ttk.Style()
#         style.theme_settings("default", {
#             "TButton": {
#                 "configure": {"padding": 10},
#                 "map": {
#                     "background": [("active", "yellow3"),
#                                    ("!disabled", "yellow")],
#                     "foreground": [("focus", "Red"),
#                                    ("active", "green"),
#                                    ("!disabled", "Blue")]
#                 }
#             }
#         })
#
#         style.theme_use("default")
#
#         button = ttk.Button(self.master, text="Hello World")
#         button.pack(padx=5, pady=5)
#
#
# root = tk.Tk()
# window = Window(root)
# root.mainloop()


# import tkinter as tk
# import tkinter.ttk as ttk
#
#
# class Window:
#     def __init__(self, master):
#         self.master = master
#
#         style = ttk.Style()
#         style.theme_create("Code")
#         style.theme_settings("Code", {
#             "TButton": {
#                 "configure": {"padding": 10},
#                 "map": {
#                     "background": [("active", "yellow3"),
#                                    ("!disabled", "yellow")],
#                     "foreground": [("focus", "Red"),
#                                    ("active", "green"),
#                                    ("!disabled", "Blue")]
#                 }
#             }
#         })
#
#         style.theme_use("Code")
#
#         button = ttk.Button(self.master, text="Hello World")
#         button.pack(padx=5, pady=5)
#
#
# root = tk.Tk()
# window = Window(root)
# root.mainloop()






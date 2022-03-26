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
#         style = ttk.Style()
#         style.configure("Custom.TButton", foreground="black",
#                         background="white",
#                         padding=[10, 10, 10, 10],
#                         font="Verdana 12 underline")
#
#         button = ttk.Button(frame, text="Click Me!", style="Custom.TButton")
#         button.pack()
#
#         frame.pack(padx=5, pady=5)
#
#
# root = tk.Tk()
# root.geometry("200x150")
# window = Window(root)
# root.mainloop()




# import tkinter as tk
# import tkinter.ttk as ttk




# class Window:
#     def __init__(self, master):
#         self.master = master
#
#         frame = ttk.Frame(self.master)
#
#         style = ttk.Style()
#         style.configure("Custom.TLabel", foreground="white",
#                         background="black",
#                         padding=[10, 10, 10, 10],
#                         relief="raised")
#
#         label = ttk.Label(frame, text="Hello World", style="Custom.TLabel")
#         label.pack(padx=5, pady=5)
#
#         frame.pack(padx=5, pady=5)
#
#
# root = tk.Tk()
# root.geometry("200x150")
# window = Window(root)
# root.mainloop()


import tkinter as tk
import tkinter.ttk as ttk


class Window:
    def __init__(self, master):
        self.master = master

        button = ttk.Button(self.master, text="Click Me!")
        button.pack(padx=5, pady=5)

        label = ttk.Label(self.master, text="This is a Label!")
        label.pack(padx=5, pady=5)

        checkbox = ttk.Combobox(self.master, values=["Option 1", "Option 2"])
        checkbox.set("Option 1")
        checkbox.pack(padx=5, pady=5)

        radiobutton = ttk.Radiobutton(self.master, text="Radio Button")
        radiobutton.pack(padx=5, pady=5)

        checkbutton = ttk.Checkbutton(self.master, text="Check Button")
        checkbutton.pack(padx=5, pady=5)

        scale = ttk.Scale(self.master, from_=0, to=10)
        scale.pack(padx=5, pady=5)

        entry = ttk.Entry(self.master)
        entry.pack(padx=5, pady=5)


root = tk.Tk()
root.geometry('200x220')
window = Window(root)
root.mainloop()






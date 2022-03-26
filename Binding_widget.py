import tkinter as tk


class MainWindow:
    def __init__(self, master):
        self.master = master

        self.usernames = ["Player1", "CodersLegacy", "Knight"]

        self.frame = tk.Frame(self.master, width=300, height=300)
        self.frame.pack()

        self.label = tk.Label(self.frame, text="This is some sample text")
        self.label.place(x=80, y=20)

        self.button = tk.Button(self.frame, text="Button")
        self.button.place(x=120, y=80)

        self.entry = tk.Entry(self.frame)
        self.entry.place(x=80, y=160)

        self.entry2 = tk.Entry(self.frame)
        self.entry2.place(x=80, y=200)

        self.bindings()

    def bindings(self):
        self.master.bind('a', lambda event: print("A was pressed"))

        self.frame.bind('<Enter>', lambda event: print("Entered Frame"))

        self.label.bind('<Button-1>', lambda event: print("Mouse clicked the label"))

        self.button.bind('<Enter>', lambda event: self.color_change(self.button, "green"))
        self.button.bind('<Leave>', lambda event: self.color_change(self.button, "black"))

        self.entry.bind('<Key>', lambda event: self.pass_check())
        self.entry.bind('<FocusIn>', lambda event: self.Focused_entry())
        self.entry.bind('<FocusOut>', lambda event: self.UnFocused_entry())

    def color_change(self, widget, color):
        widget.config(foreground=color)

    def pass_check(self):
        text = self.entry.get()
        for username in self.usernames:
            if text == username:
                print("Username taken")

    def Focused_entry(self):
        print("Focused (Entered) the entry widget")

    def UnFocused_entry(self):
        print("UnFocused (Left) the entry widget")


root = tk.Tk()
window = MainWindow(root)
root.mainloop()

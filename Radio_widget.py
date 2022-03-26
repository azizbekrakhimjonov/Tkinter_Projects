# from tkinter import *
#
# root = Tk()
# root.geometry("200x150")
# frame = Frame(root)
# frame.pack()
#
# Var1 = StringVar()
#
# RBttn = Radiobutton(frame, text="Option1", variable=Var1,
#                     value=1)
#
# RBttn2 = Radiobutton(frame, text="Option2", variable=Var1,
#                      value=2)
#
# RBttn.pack(padx=5, pady=5)
# RBttn2.pack(padx=5, pady=5)
#
# root.mainloop()

# from tkinter import *
#
# def retrieve():
#     print(Var1.get())
#     if Var1.get()==1:
#         Label(frame, text='option1').pack()
#     else:
#         Label(frame, text='option2').pack()
#
# root = Tk()
# root.geometry("200x150")
# frame = Frame(root)
# frame.pack()
#
# Var1 = IntVar()
# RBttn = Radiobutton(frame, text="Burger", variable=Var1,
#                     value=1)
# RBttn.pack(padx=5, pady=5)
#
# RBttn2 = Radiobutton(frame, text="Pizza", variable=Var1,
#                      value=2)
# RBttn2.pack(padx=5, pady=5)
#
# Button = Button(frame, text="Submit", command=retrieve)
# Button.pack()
# root.mainloop()


# from tkinter import *
# def retrieve():
#     print(Var1.get())
#     if Var1.get() == 1:
#         frame.config(bg='red')
#         root.config(bg='red')
#         RBttn.config(bg='red')
#         RBttn2.config(bg='red')
#     else:
#         root['bg'] = 'blue'
#         frame['bg'] = 'blue'
#         RBttn.config(bg='blue')
#         RBttn2.config(bg='blue')
#
# root = Tk()
# root.geometry("200x150")
# frame = Frame(root)
# frame.pack()
# Var1 = IntVar()
# RBttn = Radiobutton(frame, text="Burger", variable=Var1,
#                     value=1, command=retrieve)
# RBttn2 = Radiobutton(frame, text="Pizza", variable=Var1,
#                      value=2, command=retrieve)
# RBttn.pack(padx=5, pady=5)
# RBttn2.pack(padx=5, pady=5)
# root.mainloop()


from tkinter import *

class Window:
    def __init__(self, master):
        self.master = master
        # Frame
        self.frame = Frame(self.master, width=200, height=200)
        self.frame.pack()
        # Radiobutton
        self.var1 = IntVar()
        self.radio = Radiobutton(self.frame, variable=self.var1, value=1,
                                 text="Option 1", command=self.submit)
        self.radio.place(x=30, y=30)
        self.radio2 = Radiobutton(self.frame, variable=self.var1, value=2,
                                   text="Option 2", command=self.submit)
        self.radio2.place(x=30, y=60)
    def submit(self):
        if self.var1.get() == 1:
            print("Option 1")
        elif self.var1.get() == 2:
            print("Option 2")

root = Tk()

window1 = Window(root)
window2 = Window(root)

root.mainloop()
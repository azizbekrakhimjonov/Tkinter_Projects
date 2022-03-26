# from tkinter import *
#
# root = Tk()
# root.geometry("200x150")
# frame = Frame(root)
# frame.pack()
#
# MenuBttn = Menubutton(frame, text="Favourite food", relief=RAISED)
#
# Var1 = IntVar()
# Var2 = IntVar()
# Var3 = IntVar()
#
# Menu1 = Menu(MenuBttn, tearoff=0)
#
# Menu1.add_checkbutton(label="Pizza", variable=Var1)
# Menu1.add_checkbutton(label="Cheese Burger", variable=Var2)
# Menu1.add_checkbutton(label="Salad", variable=Var3)
#
# MenuBttn["menu"] = Menu1
#
# MenuBttn.pack()
# root.mainloop()


# from tkinter import *
#
# root = Tk()
# root.geometry("200x150")
# frame = Frame(root)
# frame.pack()
#
# MenuBttn = Menubutton(frame, text="Favourite food", relief=RAISED)
#
# Var1 = IntVar()
#
# Menu1 = Menu(MenuBttn, tearoff=0)
#
# Menu1.add_radiobutton(label="Pizza", variable=Var1, value=1)
# Menu1.add_radiobutton(label="Cheese Burger", variable=Var1, value=2)
# Menu1.add_radiobutton(label="Salad", variable=Var1, value=3)
#
# MenuBttn["menu"] = Menu1
#
# MenuBttn.pack()
# root.mainloop()





# from tkinter import *
# from tkinter.ttk import Menubutton
#
#
# def f():
#     var.set("Food")
#
#
# root = Tk()
#
# var = StringVar()
#
# mb = Menubutton(root, textvariable=var)
# mb.pack()
# mb.menu = Menu(mb, tearoff=0)
# mb["menu"] = mb.menu
#
# b = Button(root, text="Click", command=f)
# b.pack()
#
# mayoVar = IntVar()
# ketchVar = IntVar()
#
# mb.menu.add_checkbutton(label="mayo",
#                         variable=mayoVar)
# mb.menu.add_checkbutton(label="ketchup",
#                         variable=ketchVar)
#
# mb.pack()
# root.mainloop()















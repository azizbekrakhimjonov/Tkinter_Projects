# from tkinter import *
#
# def set():
#     var.set("GoodBye")
# root = Tk()
# root.geometry("200x150")
#
# frame = Frame(root)
# frame.pack()
#
# var = StringVar()
# var.set("Hello World")
#
# label = Label(frame, textvariable=var)
# label.pack()
# button = Button(frame, text="set", command=set)
# button.pack()
#
# root.mainloop()


from tkinter import *

def changecolor():
    label.configure(fg="blue")

root = Tk()
button = Button(root, text='Choose Color', command=changecolor).pack(pady=20)
label = Label(root, text="Color", fg="black")
label.pack()

root.geometry('180x160')
root.mainloop()








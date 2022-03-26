from tkinter import *

def set():
    print("Hello World")

root = Tk()
root.geometry("200x150")

frame = Frame(root)
frame.pack()
button = Button(frame, text="Button1", command=set)
button.pack()

root.mainloop()


# from tkinter import *
#
# def set():
#     print("Hello World")
#
# root = Tk()
# root.geometry("200x150")
#
# frame = Frame(root)
# frame.pack()
# button = Button(frame, text="Button1", command=set,
#                 fg="red", font="Verdana 14 underline",
#                 bd=2, bg="light blue", relief="groove")
# button.pack(pady=5)
#
# root.mainloop()
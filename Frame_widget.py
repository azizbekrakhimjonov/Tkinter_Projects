from tkinter import *

root = Tk()
root.geometry("200x150")
frame = Frame(root)
frame.pack()

# leftframe = Frame(root)
# leftframe.pack(side=LEFT)
#
# rightframe = Frame(root)
# rightframe.pack(side=RIGHT)

frame = Frame(root, bd=5, bg="purple")
frame.pack()
#
leftframe = Frame(root, bg="blue", bd=3)
leftframe.pack(side=LEFT)

rightframe = Frame(root, bg="red", bd=3)
rightframe.pack(side=RIGHT)

label = Label(frame, text="Hello world")
label.pack()

button1 = Button(leftframe, text="Button1")
button1.pack(padx=3, pady=3)
button2 = Button(rightframe, text="Button2")
button2.pack(padx=3, pady=3)
button3 = Button(leftframe, text="Button3")
button3.pack(padx=3, pady=3)

root.title("Test")
root.mainloop()
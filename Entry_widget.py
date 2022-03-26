# from tkinter import *
#
# root = Tk()
# root.geometry("200x150")
#
# frame = Frame(root)
# frame.pack()
#
# my_entry = Entry(frame, width=20)
# my_entry.insert(0, 'Username')
# my_entry.pack(padx=5, pady=5)
#
# my_entry2 = Entry(frame, width=15)
# my_entry2.insert(0, 'password')
# my_entry2.pack(padx=5, pady=5)
#
# root.mainloop()





from tkinter import *

def retrieve():
    print(my_entry.get())
    print(my_entry2.get())

root = Tk()
root.geometry("200x150")

frame = Frame(root)
frame.pack()

my_entry = Entry(frame, width=20)
my_entry.insert(0, 'Username')
my_entry.pack(padx=5, pady=5)

my_entry2 = Entry(frame, width=15)
my_entry2.insert(0, 'password')
my_entry2.pack(padx=5, pady=5)

Button = Button(frame, text="Submit", command=retrieve)
Button.pack(padx=5, pady=5)

root.mainloop()





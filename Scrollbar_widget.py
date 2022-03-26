from tkinter import *

root = Tk()
root.geometry("200x250")

mylabel = Label(root, text='Scrollbars', font="30")
mylabel.pack()

myscroll = Scrollbar(root)\
myscroll.pack(side=RIGHT, fill=Y)

mylist = Listbox(root, yscrollcommand=myscroll.set)
for line in range(1, 100):
    mylist.insert(END, "Number " + str(line))
mylist.pack(side=LEFT, fill=BOTH)

myscroll.config(command=mylist.yview)

root.mainloop()







# from tkinter import *
#
# root = Tk()
#
# frame = Frame(root, width=300, height=300)
# frame.pack(expand=True, fill=BOTH)
#
# canvas = Canvas(frame, bg='white', width=300, height=300,
#                 scrollregion=(0, 0, 500, 500))
#
# hbar = Scrollbar(frame, orient=HORIZONTAL)
# hbar.pack(side=BOTTOM, fill=X)
# hbar.config(command=canvas.xview)
#
# vbar = Scrollbar(frame, orient=VERTICAL)
# vbar.pack(side=RIGHT, fill=Y)
# vbar.config(command=canvas.yview)
#
# canvas.config(width=300, height=300)
# canvas.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
# canvas.pack(side=LEFT, expand=True, fill=BOTH)
#
# root.mainloop()






# from tkinter import *
#
# root = Tk()
#
# frame = Frame(root, width=300, height=300)
# frame.pack(expand=True, fill=BOTH)
#
# canvas = Canvas(frame, bg='white', width=300, height=300)
#
# coordinates = 20, 50, 210, 230
# arc = canvas.create_arc(coordinates, start=0, extent=250, fill="blue")
# arc = canvas.create_arc(coordinates, start=250, extent=50, fill="red")
# arc = canvas.create_arc(coordinates, start=300, extent=60, fill="yellow")
#
# canvas.pack(expand=True, fill=BOTH)
#
# root.mainloop()




# from tkinter import *
#
# root = Tk()
#
# frame = Frame(root, width=300, height=300)
# frame.pack(expand=True, fill=BOTH)
#
# canvas = Canvas(frame, bg='white', width=300, height=300)
#
# coordinates = 50, 50, 250, 250
# arc = canvas.create_line(coordinates, fill="blue")
#
# coordinates = 250, 50, 50, 250,
# arc = canvas.create_line(coordinates, fill="red")
#
# canvas.pack(expand=True, fill=BOTH)
#
# root.mainloop()


# from tkinter import *
#
# root = Tk()
#
# frame = Frame(root, width=300, height=300)
# frame.pack(expand=True, fill=BOTH)
#
# canvas = Canvas(frame, bg='white', width=300, height=300)
#
# file = PhotoImage(file="download.png")
# image = canvas.create_image(150, 150, image=file)
#
# canvas.pack(expand=True, fill=BOTH)
#
# root.mainloop()




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
# canvas.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
# canvas.pack(side=LEFT, expand=True, fill=BOTH)
#
# root.mainloop()




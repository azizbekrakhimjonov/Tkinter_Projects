# import tkinter as tk
# import tkinter.ttk as ttk
# from tkinter import simpledialog
#
#
# class Window:
#     def __init__(self, master):
#         self.master = master
#         columns = ("email", "salary")
#
#         self.tree = ttk.Treeview(self.master, columns=columns, height=20)
#         self.tree.pack(padx=5, pady=5)
#
#         self.tree.heading('#0', text='Name')
#         self.tree.heading('email', text='Email')
#         self.tree.heading('salary', text='Salary')
#
#         self.read_data()
#
#     def read_data(self):
#         f = open("Data.txt", "r")
#
#         for index, line in enumerate(f):
#             temp = line.rstrip().split(',')
#             self.tree.insert('', tk.END, iid=index,
#                              text=temp[0], values=temp[1:])
#
# root = tk.Tk()
# window = Window(root)
# root.mainloop()


# import tkinter as tk
# import tkinter.ttk as ttk
# from tkinter import simpledialog
#
#
# class Window:
#     def __init__(self, master):
#         self.master = master
#         columns = ("email", "salary")
#
#         self.tree = ttk.Treeview(self.master, columns=columns, height=20)
#         self.tree.pack(padx=5, pady=5)
#
#         self.tree.heading('#0', text='Name')
#         self.tree.heading('email', text='Email')
#         self.tree.heading('salary', text='Salary')
#
#         button = ttk.Button(root, text="Add Record", command=self.add_data)
#         button.pack(padx=5, pady=10, side=tk.RIGHT)
#
#         button = ttk.Button(root, text="Delete Record", command=self.delete_data)
#         button.pack(padx=5, pady=10, side=tk.RIGHT)
#
#         self.read_data()
#
#     def read_data(self):
#         f = open("Data.txt", "r")
#
#         for index, line in enumerate(f):
#             temp = line.rstrip().split(',')
#             self.tree.insert('', tk.END, iid=index, text=temp[0],
#                              values=temp[1:])
#
#     def add_data(self):
#         parent = simpledialog.askstring("Input", "Parent? (if any)")
#         name = simpledialog.askstring("Input", "Enter the Name")
#         email = simpledialog.askstring("Input", "Enter the Email")
#         salary = simpledialog.askstring("Input", "Enter the Salary")
#
#         self.tree.insert(parent, tk.END, text=name, values=(email, salary))
#
#     def delete_data(self):
#         row_id = self.tree.focus()
#         if (row_id != ""):
#             self.tree.delete(row_id)
#
#
# root = tk.Tk()
# window = Window(root)
# root.mainloop()
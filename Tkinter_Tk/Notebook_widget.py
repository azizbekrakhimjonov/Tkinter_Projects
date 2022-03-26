# import tkinter as tk
# import tkinter.ttk as ttk
#
#
# class Window:
#     def __init__(self, master):
#         self.master = master
#
#         self.notebook = ttk.Notebook(self.master)
#
#         # Frame 1 and 2
#         frame1 = ttk.Frame(self.notebook)
#         frame2 = ttk.Frame(self.notebook)
#
#         label1 = ttk.Label(frame1, text="This is Window One")
#         label1.pack(pady=50, padx=20)
#         label2 = ttk.Label(frame2, text="This is Window Two")
#         label2.pack(pady=50, padx=20)
#
#         frame1.pack(fill=tk.BOTH, expand=True)
#         frame2.pack(fill=tk.BOTH, expand=True)
#
#         self.notebook.add(frame1, text="Window 1")
#         self.notebook.add(frame2, text="Window 2")
#
#         # Frame 3
#         frame3 = ttk.Frame(self.notebook)
#
#         label3 = ttk.Label(frame3, text="This is Window Three")
#         label3.pack(pady=50, padx=20)
#
#         frame3.pack(fill=tk.BOTH, expand=True)
#
#         self.notebook.insert("end", frame3, text="Window 3")
#         self.notebook.pack(padx=5, pady=5, expand=True)
#
# root = tk.Tk()
# window = Window(root)
# root.mainloop()





# import tkinter as tk
# import tkinter.ttk as ttk
#
#
# class Window:
#     def __init__(self, master):
#         self.master = master
#
#         self.notebook = ttk.Notebook(self.master)
#
#         # Frame 1, 2 and 3
#         frame1 = ttk.Frame(self.notebook)
#         frame2 = ttk.Frame(self.notebook)
#         frame3 = ttk.Frame(self.notebook)
#
#         label1 = ttk.Label(frame1, text="This is Window One")
#         label1.pack(pady=50, padx=20)
#         label2 = ttk.Label(frame2, text="This is Window Two")
#         label2.pack(pady=50, padx=20)
#         label3 = ttk.Label(frame3, text="This is Window Three")
#         label3.pack(pady=50, padx=20)
#
#         frame1.pack(fill=tk.BOTH, expand=True)
#         frame2.pack(fill=tk.BOTH, expand=True)
#         frame3.pack(fill=tk.BOTH, expand=True)
#
#         self.notebook.add(frame1, text="Window 1")
#         self.notebook.add(frame2, text="Window 2")
#         self.notebook.add(frame3, text="Window 3")
#
#         self.notebook.select(frame2)
#         print(self.notebook.tab(frame2))
#         print(self.notebook.tab(1, "text"))
#
#         self.notebook.pack(padx=5, pady=5, expand=True, fill=tk.BOTH)
#
#
# root = tk.Tk()
# window = Window(root)
# root.mainloop()






# import tkinter as tk
# import tkinter.ttk as ttk
#
#
# class Window:
#     def __init__(self, master):
#         self.master = master
#
#         self.notebook = ttk.Notebook(self.master)
#
#         # Frame 1, 2 and 3
#         frame1 = ttk.Frame(self.notebook)
#         frame2 = ttk.Frame(self.notebook)
#         frame3 = ttk.Frame(self.notebook)
#
#         label1 = ttk.Label(frame1, text="This is Window One")
#         label1.pack(pady=50, padx=20)
#         label2 = ttk.Label(frame2, text="This is Window Two")
#         label2.pack(pady=50, padx=20)
#         label3 = ttk.Label(frame3, text="This is Window Three")
#         label3.pack(pady=50, padx=20)
#
#         frame1.pack(fill=tk.BOTH, expand=True)
#         frame2.pack(fill=tk.BOTH, expand=True)
#         frame3.pack(fill=tk.BOTH, expand=True)
#
#         self.tab1_image = tk.PhotoImage(file="plus.png")
#         self.tab2_image = tk.PhotoImage(file="minus.png")
#
#         self.notebook.add(frame1, text="Window 1", image=self.tab1_image,
#                           compound="left", padding=[10, 0, 10, 0])
#         self.notebook.add(frame2, text="Window 2")
#         self.notebook.add(frame3, text="Window 3", image=self.tab2_image,
#                           compound="left", padding=[10, 0, 10, 0])
#
#         self.notebook.pack(padx=5, pady=5, expand=True, fill=tk.BOTH)
#
#
# root = tk.Tk()
# window = Window(root)
# root.mainloop()





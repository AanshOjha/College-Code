import tkinter as tk

root = tk.Tk()

text = tk.Text(root)
text.pack()
text.insert('1.0', "HI!!!")
root.mainloop()
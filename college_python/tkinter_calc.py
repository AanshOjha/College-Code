import tkinter as tk

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = str(eval(screen.get()))
            screen_var.set(result)
        except:
            screen_var.set("Error")
    elif text == "Clear":
        screen_var.set("")
    else:
        screen_var.set(screen_var.get() + text)

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Display screen
screen_var = tk.StringVar()
screen = tk.Entry(root, textvar=screen_var, font="Arial 20", bd=10, justify="right")
screen.pack(fill="both", ipadx=8)

# Button layout
buttons = [
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", "9"],
    ["0"],
    ["+", "-", "*"],
    ["/", "=", "Clear"]
]

for row in buttons:
    frame = tk.Frame(root)
    frame.pack()
    for btn_text in row:
        btn = tk.Button(frame, text=btn_text, padx=20, pady=20, font="Arial 15", bg="purple", fg="white")
        btn.pack(side="left", padx=5, pady=5)
        btn.bind("<Button-1>", click)

root.mainloop()
import tkinter as tk

# def calculate_bmi():
#     try:
#         height = float(height_entry.get())
#         weight = float(weight_entry.get())
#         bmi = weight / (height ** 2)
#         result_label.config(text=f"BMI: {bmi:.2f}")
#         print("HEYAAAAA")
#     except ValueError:
#         result_label.config(text="Please enter valid numbers.")

root = tk.Tk()
root.title("BMI Calculator")

# tk.Label(root, text="Height (m):").grid(row=0, column=0, padx=10, pady=5)
# height_entry = tk.Entry(root)
# height_entry.grid(row=0, column=1, padx=10, pady=5)

# tk.Label(root, text="Weight (kg):").grid(row=1, column=0, padx=10, pady=5)
# weight_entry = tk.Entry(root)
# weight_entry.grid(row=1, column=1, padx=10, pady=5)
tk.Label(root, text="This is a simple BMI calculator.").grid(row=0, column=0, columnspan=2, padx=10, pady=5)
# tk.Button(root, text="Calculate BMI", command=calculate_bmi).grid(row=2, column=0, columnspan=2, pady=10)

# result_label = tk.Label(root, text="")
# result_label.grid(row=3, column=0, columnspan=2, pady=5)
root.mainloop()
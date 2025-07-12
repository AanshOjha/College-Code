# def perfect_square(num):
#     if num < 0:
#         return False  # Negative numbers can't be perfect squares

#     root = int(num ** 0.5)
#     if root * root == num:
#         return root 
#     else:
#         return -1

# print(perfect_square(225))

# # Open the file in read mode
# with open("fi.txt", "r") as file:
#     content = file.read()

# # Split each character with a comma
# new_content = ",".join(list(content.strip()))

# # Open the file in write mode to overwrite it with new content
# with open("file.txt", "w") as file:
#     file.write(new_content)

# matplotlib
import matplotlib.pyplot as plt
import numpy as np

food = np.array(['meat', 'banana', 'avocados', 'sweet potato'])
calories = np.array([250,130,140,120])
potas = np.array([40,55,20,30])
fat = np.array([8,5,3,6])

# Plotting three lines
plt.plot(food, calories, label='Calories', marker='o')
plt.plot(food, potas, label='Potassium', marker='s')
plt.plot(food, fat, label='Fat', marker='^')

# Adding title and axis labels
plt.title("Ques e")
plt.xlabel("Food")
plt.ylabel("Values")

# Showing legend
plt.legend()

# Show the plot
plt.show()

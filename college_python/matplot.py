import matplotlib.pyplot as plt
import numpy as np
# xpoints = [1,2,3,4,5, 6,7,8]
ypoints = [1,2,3,4,5,6,7,8]
xpoints = np.array([155, 205, 254, 320, 535, 340, 545, 850])
labels = np.array(['A', 'B', 'C', 'D', 'E', 'F', 'G'])
# plt.pie(xpoints, labels=labels)
plt.bar(xpoints, ypoints, color='blue', width=30) # Increased width for thicker bars
plt.title("My first graph")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid()
plt.show()
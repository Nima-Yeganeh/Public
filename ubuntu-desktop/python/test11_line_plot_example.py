# pip install matplotlib

import matplotlib.pyplot as plt

# Define the data to plot
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Create a line plot of the data
plt.plot(x, y)

# Add labels and a title to the plot
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Line Plot of Data')

# Display the plot
plt.show()

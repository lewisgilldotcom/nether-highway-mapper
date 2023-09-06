import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.widgets import CheckButtons

# Read the CSV file
csv_file = "/home/lewis/Documents/Nether_Highway_Stops.csv"
df = pd.read_csv(csv_file)

# Extract data
names = df['Name']
roads = df['Road']
x_coordinates = df['X']
y_coordinates = df['Y']
z_coordinates = df['Z']

# Create a scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(x_coordinates, z_coordinates, c=y_coordinates, cmap='viridis', s=100, alpha=0.5)

# Add labels to the points
for i, name in enumerate(names):
    plt.annotate(name, (x_coordinates[i], z_coordinates[i]), fontsize=8, ha='left', va='bottom')

# Set plot labels and title
plt.xlabel('X Coordinate')
plt.ylabel('Z Coordinate')  # Change the Y-axis label to Z Coordinate
plt.title('Stop Locations')

# Add a colorbar to represent Z values
cbar = plt.colorbar()
cbar.set_label('Y Value')

# Show the plot
plt.grid(True)
plt.tight_layout()
plt.show()

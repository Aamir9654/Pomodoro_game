from tkinter import Tk, Canvas

# Create the main window
window = Tk()
window.title("Graph with Grids")

# Set the canvas dimensions
canvas_width = 400
canvas_height = 400
canvas = Canvas(window, width=canvas_width, height=canvas_height, bg='white')
canvas.pack()

# Function to draw grid lines
def draw_grid(canvas, width, height, spacing=20):
    # Draw vertical grid lines
    for x in range(0, width, spacing):
        canvas.create_line(x, 0, x, height, fill="lightgray")
    
    # Draw horizontal grid lines
    for y in range(0, height, spacing):
        canvas.create_line(0, y, width, y, fill="lightgray")

# Draw the grid with 20-pixel spacing
draw_grid(canvas, canvas_width, canvas_height)

# Example: Plotting a line graph
# Points to plot on the graph (x, y)
points = [(50, 350), (100, 300), (150, 250), (200, 150), (250, 100), (300, 50)]

# Draw the points as small circles and connect them with lines
for i in range(len(points) - 1):
    x1, y1 = points[i]
    x2, y2 = points[i + 1]
    # Draw a line between points
    canvas.create_line(x1, y1, x2, y2, fill="blue", width=2)
    # Draw a small circle at each point
    canvas.create_oval(x1 - 3, y1 - 3, x1 + 3, y1 + 3, fill="red")

# Draw a small circle for the last point
last_x, last_y = points[-1]
canvas.create_oval(last_x - 3, last_y - 3, last_x + 3, last_y + 3, fill="red")

# Run the GUI event loop
window.mainloop()

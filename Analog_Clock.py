
import tkinter as tk
import math
import time

# Function to draw the clock
def update_clock():
    canvas.delete("all")  # Clear previous drawing

    # Drawing the clock face
    canvas.create_oval(cx - r, cy - r, cx + r, cy + r, outline="black", width=4)

    # Get current time
    current_time = time.localtime()
    hours = current_time.tm_hour % 12  # Convert 24-hour time to 12-hour
    minutes = current_time.tm_min
    seconds = current_time.tm_sec

    # Calculate angles for each hand
    second_angle = math.radians(seconds * 6)  # 360 degrees / 60 seconds
    minute_angle = math.radians(minutes * 6 + seconds * 0.1)  # 360 degrees / 60 minutes + adjustment for seconds
    hour_angle = math.radians((hours + minutes / 60) * 30)  # 360 degrees / 12 hours

    # Draw the clock hands
    draw_hand(second_angle, r - 20, "red", 2)  # Second hand
    draw_hand(minute_angle, r - 40, "blue", 4)  # Minute hand
    draw_hand(hour_angle, r - 60, "green", 6)  # Hour hand

    # Repeat after 1000 ms (1 second)
    canvas.after(1000, update_clock)

# Function to draw the hands of the clock
def draw_hand(angle, length, color, width):
    x_end = cx + length * math.sin(angle)
    y_end = cy - length * math.cos(angle)
    canvas.create_line(cx, cy, x_end, y_end, fill=color, width=width)

# Main Tkinter window
root = tk.Tk()
root.title("Analog Clock")

# Set up canvas
r = 150  # Radius of the clock
cx, cy = r + 20, r + 20  # Center coordinates of the clock

canvas = tk.Canvas(root, width=cx * 2, height=cy * 2, bg="white")
canvas.pack()

# Start updating the clock
update_clock()

# Start the Tkinter event loop
root.mainloop()
import cv2
import numpy as np

# Define the dimensions of the frame
# resolution = (2160,3840)
resolution = (3840,2160)

# Define the dimensions of the rectangle
rect_width = 500
rect_height = 200
rect_top = (resolution[1] - rect_height) // 2
rect_bottom = rect_top + rect_height

# Define the initial position and speed of the rectangle
rect_left = 0
rect_dx = 5

# Define the background color (white)
bg_color = (255, 255, 255)

# Create a VideoWriter object to write the video
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
video_writer = cv2.VideoWriter("vid/4.mp4", fourcc, 30.0, resolution, isColor=True)

# Generate the frames of the video
for i in range(700):
    # Create a new frame with the background color
    frame = np.zeros((resolution[1], resolution[0], 3), dtype=np.uint8)
    frame[:, :] = bg_color

    # Draw the green rectangle at the current position
    rect_right = rect_left + rect_width
    cv2.rectangle(frame, (rect_left, rect_top), (rect_right, rect_bottom), (0, 255, 0), -1)

    # Write the frame to the video
    video_writer.write(frame)

    # Update the position of the rectangle
    rect_left += rect_dx
    if rect_left < 0 or rect_left + rect_width > resolution[0]:
        rect_dx = -rect_dx

# Release the VideoWriter object
video_writer.release()

import cv2 # for image processing 
import numpy as np # for numerical operations
import random # for random numbers
import math # for math operations
import csv # for handling CSV files
import os # for interaction with the OS to create directory 

# Define the file to save images
rectangles_folder = 'generated_images/' # to save images
csv_filename = 'rectangle_angles.csv' # to save angles 

os.makedirs(rectangles_folder, exist_ok=True) # Create the directory for images if it doesn't exist

angles = [] # Empty array to store angle data 

for i in range(100):
    # Generate a random floating-point number between a specified range 
    random_float = random.uniform(-10, 11)

    # Define the properties of the rotating rectangle
    width, height = 600, 400 # Image size 
    rectangle_width, rectangle_height = int(0.6 * width), int(0.6 * height)  # Rectangle size: 60% of the image dimensions
    angle_degrees = random_float  # Rotation angle in degrees

    # Create an empty image (all pixels with the same grayscale intensity)
    image = np.zeros((height, width, 3), dtype=np.uint8)

    # Calculate the corner points of the rectangle
    center_x = width // 2
    center_y = height // 2

    rect_points = np.array([
        [center_x - rectangle_width // 2, center_y - rectangle_height // 2],  # Top-left
        [center_x + rectangle_width // 2, center_y - rectangle_height // 2],  # Top-right
        [center_x + rectangle_width // 2, center_y + rectangle_height // 2],  # Bottom-right
        [center_x - rectangle_width // 2, center_y + rectangle_height // 2]  # Bottom-left
    ], np.float32)

    # Create a rotation matrix
    rotation_matrix = cv2.getRotationMatrix2D((center_x, center_y), angle_degrees, scale=1.0)

    # Apply the rotation to the rectangle points
    rotated_points = cv2.transform(rect_points.reshape(-1, 1, 2), rotation_matrix)

    # Draw the rotated rectangle on the canvas
    cv2.fillPoly(image, [np.int32(rotated_points)], color=(255, 0, 0))  # Fill rectangle with blue color

    # Display the rotated rectangle with text
    cv2.imshow('my_rectangle_images', image) 
    cv2.waitKey(0) # Wait for a key press

    # Store the angle and rectangle number in the list
    angles.append((i, angle_degrees))

    # Save the image with a unique filename
    image_filename = f'{rectangles_folder}rotated_rectangle_{i}.png'
    cv2.imwrite(image_filename, image)

# Save the angles list to a CSV file
with open(csv_filename, 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['Rectangle Number', 'Angle (degrees)'])  # Header row
    csv_writer.writerows(angles)

print(f'Angles saved to {csv_filename}')
print(f'Images saved to {rectangles_folder}')






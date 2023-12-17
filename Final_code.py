import cv2 #for image processing 
import numpy as np #for numerical operations
from cv2 import imshow #for image show
import random #for random numbers
import math #for math operations
import csv #for excel
import os # for interaction with the OS to create directory 

# Define the file to save images
image_folder = 'generated_images/' #to save image
csv_filename = 'rectangle_angles.csv' # to save angles 

os.makedirs(image_folder, exist_ok=True)  #exit_ok if directory already exist then no errors should raise

angles = [] #empty array 

for i in range(100):
    # Generate a random floating-point number between a specified range 
    random_float = random.uniform(-10, 11)

    # Define the properties of the rotating rectangle
    width, height = 600, 400 #image size 
    rectangle_width, rectangle_height = int(0.6 * width), int(0.6 * height)  # Rectangle occupies 60% of the image dimensions
    angle_degrees = random_float  # Rotation angle in degrees

    # Create an empty image (all pixels with the same grayscale intensity)
    image = np.zeros((height, width, 3), dtype=np.uint8)

    # Calculate the corner points of the rectangle
    angle_radians = math.radians(angle_degrees)
   
    center_x = width // 2
    center_y = height // 2

    rect_points = np.array([
        [center_x - rectangle_width // 2, center_y - rectangle_height // 2],  # Top-left
        [center_x + rectangle_width // 2, center_y - rectangle_height // 2],  # Top-right
        [center_x + rectangle_width // 2, center_y + rectangle_height // 2],  # Bottom-right
        [center_x - rectangle_width // 2, center_y + rectangle_height // 2]  # Bottom-left
    ], np.float32) #npfloat converts the point into floats which are a direct input to cv2

    # Create a rotation matrix
    rotation_matrix = cv2.getRotationMatrix2D((center_x, center_y), angle_degrees, scale=1.0) #cv2 getrotation function generates a rotation matrix
     #the rotation must perform at the center and scale 1 means no zoom in our out of the image 
    # Apply the rotation to the rectangle points
    rotated_points = cv2.transform(rect_points.reshape(-1, 1, 2), rotation_matrix) #calculating the new rotatating points
    #this transformation effectively rotates each corner point of the rectangle around the image's center. 

    # Draw the rotated rectangle on the canvas
    cv2.fillPoly(image, [np.int32(rotated_points)], color=(255, 0, 0))  # Fill rectangle with blue color, cv2 takes integer points and darw rectangle on an empty image

 # Display the rotated rectangle with text
   
    cv2.imshow('image' , image)
    cv2.waitKey(0) #keybard binding, if any key is pressed then it will continue the execution

    # Store the angle and rectangle number in the list 
    angles.append((i, angle_degrees))

    # Save the image with a unique filename
    image_filename = f'{image_folder}rotated_rectangle_{i}.png'
    cv2.imwrite(image_filename, image)

# Save the angles list to a CSV file
with open(csv_filename, 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['Rectangle Number', 'Angle (degrees)'])  # Header row
    csv_writer.writerows(angles)

print(f'Angles saved to {csv_filename}')
print(f'Images saved to {image_folder}')

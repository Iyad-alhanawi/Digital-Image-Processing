import cv2
import numpy as np
from skimage.filters import sobel
import matplotlib.pyplot as plt

# Load the image in grayscale
file_path = 'file path'  # Specify your image file path
img = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)

# Check if the image was loaded successfully
if img is None:
    raise ValueError("Image not found. Please check the file path.")

# Edge detection using Sobel filter
sobel_img = sobel(img)

# Normalize the Sobel image for better visualization
sobel_img = (sobel_img * 255).astype(np.uint8)

# Create a subplot to display images
plt.figure(figsize=(10, 5))

# Original image
plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(img, cmap='gray')
plt.axis('off')

# Sobel edge-detected image
plt.subplot(1, 2, 2)
plt.title('Sobel Edge Detection')
plt.imshow(sobel_img, cmap='gray')
plt.axis('off')

# Show the plots
plt.tight_layout()
plt.show()

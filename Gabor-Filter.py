import numpy as np
import cv2
import matplotlib.pyplot as plt

# Gabor filter parameters
ksize = 15 
sigma = 5  
theta = 1 * np.pi / 2  
lamda = 1 * np.pi / 4   
gamma = 0.9  
phi = 0.8  

# Create the Gabor kernel
kernel = cv2.getGaborKernel((ksize, ksize), sigma, theta, lamda, gamma, phi, ktype=cv2.CV_32F)

# Load and process the image
img = cv2.imread('image path') 
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
fimg = cv2.filter2D(img_gray, cv2.CV_8UC3, kernel)

# Set up the plot
plt.figure(figsize=(12, 10))

# Display the Gabor kernel
plt.subplot(2, 2, 1)
plt.imshow(kernel, cmap='gray')
plt.title('Gabor Kernel', fontsize=16)
plt.axis('off')

# Display the original image
plt.subplot(2, 2, 2)
plt.imshow(img_gray, cmap='gray')
plt.title('Original Image', fontsize=16)
plt.axis('off')

# Display the filtered image
plt.subplot(2, 2, 3)
plt.imshow(fimg, cmap='gray')
plt.title('Filtered Image', fontsize=16)
plt.axis('off')

# Resize and display the kernel for clarity
kernel_resized = cv2.resize(kernel, (400, 400))
plt.subplot(2, 2, 4)
plt.imshow(kernel_resized, cmap='gray')
plt.title('Resized Gabor Kernel', fontsize=16)
plt.axis('off')

# Show the plots
plt.tight_layout()
plt.show()

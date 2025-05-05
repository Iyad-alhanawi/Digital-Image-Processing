import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the main image and the template
img = cv2.imread("image path")
img_grey = cv2.imread("image path", 0)
temp = cv2.imread("image path", 0)

# Get dimensions of the template
h, w = temp.shape[:2]

# Perform template matching
res = cv2.matchTemplate(img_grey, temp, cv2.TM_CCOEFF_NORMED)
loc = np.where(res > 0.8)

# Draw rectangles around matched regions
for pt in zip(*loc[::-1]):
    cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (255, 0, 0), 6)

# Set up the plot for visualization
plt.figure(figsize=(10, 6))
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))  # Convert BGR to RGB
plt.title('Template Matching Result', fontsize=20)
plt.axis('off')  # Turn off axis

# Show the image using matplotlib
plt.show()

# Save the result
cv2.imwrite("image path.jpg", img)

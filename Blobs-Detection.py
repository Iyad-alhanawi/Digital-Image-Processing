import matplotlib.pyplot as plt
import numpy as np
import cv2

# Load the input image in grayscale
image = cv2.imread("file path", 0)

# Setup SimpleBlobDetector parameters.
params = cv2.SimpleBlobDetector_Params()
params.filterByArea = True
params.minArea = 100
params.filterByCircularity = True
params.minCircularity = 0.5

# Create a detector with the parameters
detector = cv2.SimpleBlobDetector_create(params)

# Detect blobs
keypoints = detector.detect(image)

# Draw blobs on the image
img_with_blobs = cv2.drawKeypoints(image, keypoints, np.array([]), (0, 0, 255), 
                                    cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# Set up the plot
plt.figure(figsize=(10, 6))
plt.imshow(img_with_blobs, cmap='gray')
plt.title('Blob Detection', fontsize=20)
plt.axis('off')  # Turn off axis
plt.xlabel('X-axis', fontsize=14)
plt.ylabel('Y-axis', fontsize=14)

# Show the image in a window
cv2.imshow("Keypoints", img_with_blobs)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save result
cv2.imwrite("file path.jpg", img_with_blobs)

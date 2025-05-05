# Digital Image Processing Techniques

## Overview

This repository showcases a collection of image processing techniques implemented in Python, leveraging the power of OpenCV and Matplotlib. The techniques included are:

1. **Blob Detection**: Identifying key features in images based on shape and size.
2. **Template Matching**: Locating specific patterns or objects within images.
3. **Gabor Filter**: Analyzing textures and patterns using frequency-based filtering.
4. **Sobel Edge Detection**: Detecting edges in images to highlight transitions in intensity.

## Description of Techniques

### 1. Blob Detection

Blob detection is a technique used to identify regions in an image that differ in properties like color or brightness compared to surrounding areas. This implementation uses OpenCV's SimpleBlobDetector to find and visualize blobs based on specified parameters, such as area and circularity.

### 2. Template Matching

Template matching is a method for finding and locating a template image within a larger image. This technique is useful in scenarios where you need to identify specific objects. The code applies template matching with OpenCV and draws rectangles around the detected matches, providing a clear visualization of where the template appears in the main image.

### 3. Gabor Filter

The Gabor filter is a powerful tool for texture analysis and feature extraction. It operates by convolving the image with a Gabor kernel, which can be tuned to capture specific frequencies and orientations. This implementation demonstrates how to create a Gabor kernel, apply it to an image, and visualize both the kernel and the filtered results to analyze textures effectively.

### 4. Sobel Edge Detection

Sobel edge detection is a widely used technique to identify edges within an image. By applying the Sobel operator in both the horizontal and vertical directions, this method highlights areas of high gradient, indicating significant changes in intensity. The resulting edge map provides valuable information for further image analysis and processing.


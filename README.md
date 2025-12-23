# Template Matching Using OpenCV (Image Pattern Detection)

## Project Overview
This project implements **template matching** using **OpenCV** to detect the presence and location of a smaller image (template) within a larger image. Template matching is a classical computer vision technique widely used for **object localization**, **pattern detection**, and **image comparison**.

The system compares pixel-level similarity between the template image and regions of the target image and highlights matching areas with bounding boxes.

---

## Objective
- Detect a specific object or pattern inside a larger image
- Apply template matching using correlation-based similarity
- Visualize detected matches with bounding boxes
- Understand grayscale-based image comparison

---

## Technologies Used
- Python 3
- OpenCV (cv2)
- NumPy

---

## Core Concepts Used
- Template Matching
- Grayscale Image Processing
- Normalized Cross-Correlation
- Threshold-Based Detection
- Bounding Box Visualization

---

## How the System Works

### 1. Image Loading
- **Template Image**: The object or pattern to be found
- **Original Image**: The larger image where the template is searched

Both images are loaded using OpenCV.

---

### 2. Grayscale Conversion
- Both images are converted to grayscale
- Reduces computational complexity
- Improves template matching consistency

---

### 3. Template Matching
- OpenCV’s `matchTemplate()` function is used
- Method applied: `TM_CCORR_NORMED`
- Produces a similarity map where higher values indicate better matches

---

### 4. Thresholding
- A strict threshold value (`0.99`) is applied
- Only highly confident matches are considered
- Helps eliminate false positives

---

### 5. Bounding Box Drawing
- Locations exceeding the threshold are extracted
- Green rectangles are drawn around detected template positions
- Bounding box size matches the template dimensions

---

### 6. Visualization
- Original image displayed with detected regions highlighted
- Template image shown separately for reference
- Images resized for better on-screen visualization

---

## Output
- Highlighted bounding box where the template is detected
- Visual confirmation of template-image similarity
- Side-by-side viewing of template and original image

---

## How to Run the Project

### Prerequisites
Ensure the following libraries are installed:
- opencv-python
- numpy

---

### Execution Steps
1. Place the template image and original image on your system
2. Update file paths in the script accordingly
3. Run the Python script
4. View detected regions in the displayed window
5. Press any key to close the application

---

## Applications
- Object detection in static images
- Logo or symbol detection
- Quality inspection
- Image comparison tasks
- Surveillance and monitoring systems

---

## Limitations
- Sensitive to scale changes
- Sensitive to rotation
- Works best when template size matches object size
- Lighting variations may reduce accuracy

---

## Possible Enhancements
- Multi-scale template matching
- Rotation-invariant detection
- Adaptive thresholding
- Combining with feature-based methods (ORB, SIFT)
- Real-time video-based template matching

---

## Learning Outcomes
- Practical understanding of template matching
- Experience with correlation-based similarity methods
- Hands-on OpenCV image processing
- Visual debugging of computer vision pipelines

---

## Author
This project was developed as a practical demonstration of classical computer vision techniques using OpenCV, focusing on template matching and object localization.

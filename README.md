# HSV Color Segmentation & Object Counting (PCD)

[![DOI](https://zenodo.org/badge/493963340.svg)](https://doi.org/10.5281/zenodo.18732226)

This project implements color-based object segmentation using the HSV color space combined with connected component analysis for object counting.

The system is implemented in two versions:
1. Web-based application using OpenCV.js
2. Python application using OpenCV (cv2)

This project was developed for Pengolahan Citra Digital (Digital Image Processing).

Author:
I Wayan Pio Pratama


------------------------------------------------------------
OVERVIEW
------------------------------------------------------------

The system performs:

- RGB to HSV color conversion
- HSV thresholding using adjustable lower and upper bounds
- Mask generation using inRange operation
- Morphological operations (erosion and dilation)
- Connected component labeling
- Object counting
- Bitwise masking for visualization


------------------------------------------------------------
FEATURES
------------------------------------------------------------

Web Version (OpenCV.js)

- Upload image input
- Adjustable HSV sliders (Lower H, S, V and Upper H, S, V)
- Real-time mask generation
- Erosion and dilation operations
- Connected component object counting
- RGB and HSV result visualization

Python Version (OpenCV)

- Trackbar-based HSV adjustment
- Mask generation
- Connected component detection
- Object count displayed on output image


------------------------------------------------------------
ALGORITHMS USED
------------------------------------------------------------

- HSV Color Space Conversion
- Thresholding (cv.inRange / cv2.inRange)
- Bitwise AND Masking
- Morphological Erosion
- Morphological Dilation
- Connected Component Labeling


------------------------------------------------------------
PROJECT STRUCTURE
------------------------------------------------------------

Web Version:
- index.html
- css/
- js/
- opencv.js

Python Version:
- main.py (HSV + connected components implementation)
- dataset/


------------------------------------------------------------
REQUIREMENTS
------------------------------------------------------------

Web Version:
- Modern web browser
- OpenCV.js
- Bootstrap
- jQuery

Python Version:
- Python 3.x
- OpenCV
- NumPy

Install Python dependencies:

pip install opencv-python numpy


------------------------------------------------------------
HOW TO RUN
------------------------------------------------------------

Web Version:

1. Open index.html in a browser.
2. Upload an image.
3. Adjust HSV sliders to segment objects.
4. Optionally apply erosion or dilation.
5. The system will display the detected object count.

Python Version:

1. Place an image inside the dataset folder.
2. Update the image path if needed.
3. Run:

python main.py

4. Adjust HSV trackbars to segment objects.
5. Press ESC to exit.


------------------------------------------------------------
ACADEMIC CONTEXT
------------------------------------------------------------

This project was created as part of coursework in Digital Image Processing (PCD). It demonstrates fundamental image processing concepts including color segmentation and object counting using connected components.


------------------------------------------------------------
CITATION
------------------------------------------------------------

If you use this software in academic work, please cite:

Pratama, I. W. P. (2026). HSV Color Segmentation & Object Counting (PCD) [Software]. https://doi.org/10.5281/zenodo.18732226


------------------------------------------------------------
LICENSE
------------------------------------------------------------

This project is intended for academic and educational use.

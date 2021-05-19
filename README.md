# ShapeDetection
Uses OpenCV to detect multiple shapes. to detect shapes with this method all of your shapes have to be the same color (mine were all red and had upper hsv values of [0, 100, 151] and lower hsv values of [179, 193, 206]). After detecting that certain color, I drew contours around that shape and counted the approximated number of points to determine the name of the shape.

# How To Use 
- Use this HSV Color finder to get the HSV values of your shape. 
  - https://github.com/kyl3ru1z/HSV_ColorFinder

# What I Learned 
- Color detection
- Implementing Contours 
- Utilizing OpenCV to draw text and rectangles 

# Object Detection, Tracking of Basketballs
## Failure Experience:
1. cv2.HoughCircles only find object with ball shape, but there are many similar objects in the real world can be classified as ball object

## A. Basket ball features
### A1. General feautures
- shape: ball / circle
- color: organge
### A2. Minor features
- line: black_line
- size in real world: 12-12.1 cm radius
![plot](./img/ball_radius.png)

## B. Solutions
1. HSV Color Filter
2. Gray Image and Blur
3. Erosion, Dialate and closing: [Reference link](https://opencv24-python-tutorials.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_morphological_ops/py_morphological_ops.html)
4. HoughCircles


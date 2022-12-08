# Template Matching
## :+1:Outcome
![alt text](https://github.com/hmlaiac/NEW_AI/blob/main/opencv/Corner%20Detection/img/img2.png)

## :+1:Usage
- Calculate differentiation of regions to identify the corner of image
- Check boards, Grids (A solution to detect edge but not very useful)


## :+1:Limitation
- Depend on color intensity (greatly affected by surrounding enviroment)
- Model isn't flexible enought 

## :+1:Code highlight
### Harris Corner Detection
```
@widgets.interact(x=(0, 1.00000), blockSize=(1,10), ksize=(3,30))
def f(x=0, blockSize=1, ksize=3):
    if ksize%2==0:
        ksize+=1
    dst = cv2.cornerHarris(src=img2_gray,blockSize=blockSize,ksize=ksize,k=0.04)
    dst = cv2.dilate(dst,None)
    img2_copy = img2.copy()
    img2_copy[dst>x*dst.max()]=[255,0,0]

    plt.imshow(img2_copy)

```
#### Parameters
- double x: Ajust threshold (0.0, 1.0)
- int blockSize: Neighborhood size (It is the size of neighbourhood considered for corner detection.)
- int ksize: Aperture parameter for the Sobel operator (Size of sober kernel, should be odd number)  size increases, more pixels are part of each convolution process and the edges will get more blurry.
- double k: Harris detector free parameter (0.0, 1.0)
### Shi-Tomasi Corner Detector
```
@widgets.interact(maxCorners=(1,30), qualityLevel=(1,100), minDistance=(1,100))
def f(maxCorners=1, qualityLevel=1, minDistance=1):
    img2_copy = img2.copy()

    corners = cv2.goodFeaturesToTrack(image=img2_gray, maxCorners=maxCorners, qualityLevel=qualityLevel/100, minDistance=minDistance)
    corners = np.int0(corners)

    for i in corners:
        x,y = i.ravel()
        cv2.circle(img2_copy,(x,y),3,255,-1)

    plt.imshow(img2_copy)
```
#### Parameters
- int maxCorners: Maximum point to detect
- double qualityLevel: Parameter characterizing the minimal accepted quality of image. (A threshold to reject some scores, similar to x)
- double minDistance: Set up minimum Euclidean distance
## :+1:Reference
- [Use slide bar in Jupyter notebook](https://ipython-books.github.io/33-mastering-widgets-in-the-jupyter-notebook)
- [Theory](https://docs.opencv.org/3.4/dc/d0d/tutorial_py_features_harris.html) 

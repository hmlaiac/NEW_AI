# Template Matching
## :+1:Outcome
![alt text](https://github.com/hmlaiac/NEW_AI/blob/main/opencv/Edge%20Detection/img/result.png)

## :+1:Usage
- Find Edge of an image
- This is an image processing skill


## :+1:Limitation
- None

## :+1:Code highlight
### Canny with Manual Justification
```
threshold1 = 17
threshold2 = 65

edges = cv2.Canny(image=blurred_img, threshold1=threshold1, threshold2=threshold2)

plt.subplot(1,2,1)
plt.imshow(edges, cmap='gray_r')
plt.subplot(1,2,2)
plt.imshow(img)
plt.show()

```
#### Parameters
- int threshold1: [0, 255]
- int threshold2: [0, 255]
### Canny with Auto Median Detection
```
blurred_img = cv2.blur(img,ksize=(5,5))
median_val = np.median(img)

@widgets.interact(const1=(0, 1, 0.1), const2=(0, 1, 0.1))
def f(const1=0, const2=1):
    
    lower = int(max(0, const1* median_val))
    upper = int(min(255,const2 * median_val))

    edges = cv2.Canny(image=blurred_img, threshold1=lower, threshold2=upper)
    plt.imshow(edges, cmap='gray_r')
```

## :+1:Reference
- [Canny](https://docs.opencv.org/4.x/da/d22/tutorial_py_canny.html)

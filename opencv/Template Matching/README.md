# Template Matching
## Usage
- Detect a croped image inside a image
- Text Recognition in early age (Fixed size)
- Detection of 2D game

![alt text](https://github.com/hmlaiac/NEW_AI/blob/main/opencv/Template%20Matching/img/outcome.png)

## Limitation
- Fixed size of target (If target is blend or modified, hardly to detect the image)
- The croped image should exited in the image

## Time complexity
- matchTemplate: O(n^3)
- minMaxLoc: O(n^2)
- Total: O(n^3)

## Code highlight
### Simple matching
```
full_copy = img.copy()

method = eval('cv2.TM_CCOEFF')
res = cv2.matchTemplate(full_copy,target1,method)

height, width,channels = target1.shape
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

# Assign the Bottom Right of the rectangle
top_left = max_loc
bottom_right = (top_left[0] + width, top_left[1] + height)

# Draw the Red Rectangle
cv2.rectangle(full_copy,top_left, bottom_right, 255, 10)
plt.imshow(full_copy)
plt.show()
```
### Trick code

```
if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc    
    else:
        top_left = max_loc
```

## Other concepts
- Calculate shape of result = W-w+1, H-h+1
- [Original Documentation](https://docs.opencv.org/4.x/d4/dc6/tutorial_py_template_matching.html)
- [Equations of mathcing](https://docs.opencv.org/4.x/df/dfb/group__imgproc__object.html#gga3a7850640f1fe1f58fe91a2d7583695dab65c042ed62c9e9e095a1e7e41fe2773) 

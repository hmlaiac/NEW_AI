# Template Matching
## Usage
- Detect a croped image inside a image
- Text Recognition in early age (Fixed size)
- Detection of 2D game

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

```
### Trick code

```
```

## Other concepts
- Calculate shape of result = W-w+1, H-h+1
- [Original Documentation](https://docs.opencv.org/4.x/d4/dc6/tutorial_py_template_matching.html)
- [Equations of mathcing](https://docs.opencv.org/4.x/df/dfb/group__imgproc__object.html#gga3a7850640f1fe1f58fe91a2d7583695dab65c042ed62c9e9e095a1e7e41fe2773) 
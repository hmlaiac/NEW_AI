import cv2
import numpy as np
import matplotlib.pyplot as plt

class Detect:
    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2

    def findBallByColorDetection(self, img_path):
        im = cv2.imread(img_path)

        # convert to HSV space
        im_hsv = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)
        # take only the orange, highly saturated, and bright parts
        # im_hsv = cv2.inRange(im_hsv, (7, 180, 180), (11, 255, 255))
        im_hsv = cv2.inRange(im_hsv, self.param1, self.param2)

        # To show the detected orange parts:
        im_orange = im.copy()
        im_orange[im_hsv == 0] = 0
        # cv2.imshow('im_orange',im_orange)

        # Perform opening to remove smaller elements (filtering)
        element = np.ones((5, 5)).astype(np.uint8)
        im_hsv = cv2.erode(im_hsv, element)
        im_hsv = cv2.dilate(im_hsv, element)

        points = np.dstack(np.where(im_hsv > 0)).astype(np.float32)
        # fit a bounding circle to the orange points
        center, radius = cv2.minEnclosingCircle(points)
        print(center)
        cv2.circle(im, (int(center[1]), int(center[0])), int(radius), (255, 0, 0), thickness=3)
        out = np.vstack([im_orange, im])
        out = cv2.cvtColor(out, cv2.COLOR_BGR2RGB)
        return out

    # def plot_example(self):
    #     # draw this circle
    #     cv2.circle(im, (int(self.center[1]), int(self.center[0])), int(self.radius), (255, 0, 0), thickness=3)
    #
    #     out = np.vstack([im_orange, im])
    #     out = cv2.cvtColor(out, cv2.COLOR_BGR2RGB)
    #     plt.imshow(out)
    #     plt.show()

if __name__ == "__main__":
    import cv2
    import numpy as np

    frameWidth = 640
    frameHeight = 480
    cap = cv2.VideoCapture(1)
    cap.set(3, frameWidth)
    cap.set(4, frameHeight)
    cap.set(10, 150)


    def empty(a):
        pass


    cv2.namedWindow("HSV")
    cv2.resizeWindow("HSV", 640, 240)
    cv2.createTrackbar("HUE Min", "HSV", 0, 179, empty)
    cv2.createTrackbar("SAT Min", "HSV", 0, 255, empty)
    cv2.createTrackbar("VALUE Min", "HSV", 0, 255, empty)
    cv2.createTrackbar("HUE Max", "HSV", 179, 179, empty)
    cv2.createTrackbar("SAT Max", "HSV", 255, 255, empty)
    cv2.createTrackbar("VALUE Max", "HSV", 255, 255, empty)
    img = cv2.imread("..\\data\\png_ball1.png")
    print(img)
    while True:
        # _, img = cap.read(0)
        imgHsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        h_min = cv2.getTrackbarPos("HUE Min", "HSV")
        h_max = cv2.getTrackbarPos("HUE Max", "HSV")
        s_min = cv2.getTrackbarPos("SAT Min", "HSV")
        s_max = cv2.getTrackbarPos("SAT Max", "HSV")
        v_min = cv2.getTrackbarPos("VALUE Min", "HSV")
        v_max = cv2.getTrackbarPos("VALUE Max", "HSV")
        print(h_min)

        lower = np.array([h_min, s_min, v_min])
        upper = np.array([h_max, s_max, v_max])
        mask = cv2.inRange(imgHsv, lower, upper)
        result = cv2.bitwise_and(img, img, mask=mask)

        mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
        # hStack = np.hstack([img, mask, result])
        img = cv2.resize(img, (960, 540))
        cv2.imshow('Original', img)
        imgHsv = cv2.resize(imgHsv, (960, 540))
        cv2.imshow('HSV Color Space', imgHsv)
        # img = cv2.resize(img, (960, 540))
        # cv2.imshow('Mask', mask)
        result = cv2.resize(result, (960, 540))
        cv2.imshow('Result', result)
        # cv2.imshow('Horizontal Stacking', hStack)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
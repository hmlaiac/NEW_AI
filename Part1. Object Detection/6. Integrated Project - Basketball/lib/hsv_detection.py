from __future__ import print_function
import cv2 as cv
import numpy as np
import argparse

src = None
erosion_size = 0
max_elem = 2
max_kernel_size = 21
# Trackbar name for hsvFilter
title_trackbar_hue_min = 'Hue Min'
title_trackbar_saturation_min = 'Saturation Min'
title_trackbar_value_min = 'Value Min'
title_trackbar_hue_max = 'Hue Max'
title_trackbar_saturation_max = 'Saturation Max'
title_trackbar_value_max = 'Value Max'

# Trackbar name for erosion and dialate
title_trackbar_element_shape = 'Element:\n 0: Rect \n 1: Cross \n 2: Ellipse'
title_trackbar_kernel_size = 'Kernel size:\n 2n +1'

title_hsvFilter_window = 'HSVFilter Demo'
title_erosion_window = 'Erosion Demo'
title_dilation_window = 'Dilation Demo'


def main(image):
    global src
    src = cv.imread(image)
    if src is None:
        print('Could not open or find the image: ', image)
        exit(0)

    cv.namedWindow(title_hsvFilter_window)
    cv.createTrackbar(title_trackbar_hue_min, title_hsvFilter_window, 0, 255, hsvFilter)
    cv.createTrackbar(title_trackbar_saturation_min, title_hsvFilter_window, 0, 255, hsvFilter)
    cv.createTrackbar(title_trackbar_value_min, title_hsvFilter_window, 0, 255, hsvFilter)
    cv.createTrackbar(title_trackbar_hue_max, title_hsvFilter_window, 0, 255, hsvFilter)
    cv.createTrackbar(title_trackbar_saturation_max, title_hsvFilter_window, 0, 255, hsvFilter)
    cv.createTrackbar(title_trackbar_value_max, title_hsvFilter_window, 0, 255, hsvFilter)

    cv.namedWindow(title_erosion_window)
    cv.createTrackbar(title_trackbar_element_shape, title_erosion_window, 0, max_elem, erosion)
    cv.createTrackbar(title_trackbar_kernel_size, title_erosion_window, 0, max_kernel_size, erosion)

    cv.namedWindow(title_dilation_window)
    cv.createTrackbar(title_trackbar_element_shape, title_dilation_window, 0, max_elem, dilatation)
    cv.createTrackbar(title_trackbar_kernel_size, title_dilation_window, 0, max_kernel_size, dilatation)

    # Display functions
    hsvFilter(0)
    erosion(0)
    dilatation(0)
    cv.waitKey()


# optional mapping of values with morphological shapes
def morph_shape(val):
    if val == 0:
        return cv.MORPH_RECT
    elif val == 1:
        return cv.MORPH_CROSS
    elif val == 2:
        return cv.MORPH_ELLIPSE


def hsvFilter(val):
    # Get Bar Value
    hue_min = cv.getTrackbarPos(title_trackbar_hue_min, title_hsvFilter_window)
    saturation_min = cv.getTrackbarPos(title_trackbar_saturation_min, title_hsvFilter_window)
    value_min = cv.getTrackbarPos(title_trackbar_value_min, title_hsvFilter_window)
    hue_max = cv.getTrackbarPos(title_trackbar_hue_max, title_hsvFilter_window)
    saturation_max = cv.getTrackbarPos(title_trackbar_saturation_max, title_hsvFilter_window)
    value_max = cv.getTrackbarPos(title_trackbar_value_max, title_hsvFilter_window)

    hsv_min = (hue_min, saturation_min, value_min)
    hsv_max = (hue_max, saturation_max, value_max)

    im_hsv = cv.cvtColor(src, cv.COLOR_BGR2HSV)
    # take only the orange, highly saturated, and bright parts
    # im_hsv = cv2.inRange(im_hsv, (7, 180, 180), (11, 255, 255))
    im_hsv = cv.inRange(im_hsv, hsv_min, hsv_max)

    # To show the detected orange parts:
    im_orange = src.copy()
    im_orange[im_hsv == 0] = 0
    # plt.imshow(cv.cvtColor(im_orange, cv2.COLOR_BGR2RGB))
    # plt.plot()
    resized = cv.resize(im_orange, (1000,600))
    cv.imshow(title_hsvFilter_window, resized)

def erosion(val):
    erosion_size = cv.getTrackbarPos(title_trackbar_kernel_size, title_erosion_window)
    erosion_shape = morph_shape(cv.getTrackbarPos(title_trackbar_element_shape, title_erosion_window))

    element = cv.getStructuringElement(erosion_shape, (2 * erosion_size + 1, 2 * erosion_size + 1),
                                       (erosion_size, erosion_size))

    erosion_dst = cv.erode(src, element)
    cv.imshow(title_erosion_window, erosion_dst)



def dilatation(val):
    dilatation_size = cv.getTrackbarPos(title_trackbar_kernel_size, title_dilation_window)
    dilation_shape = morph_shape(cv.getTrackbarPos(title_trackbar_element_shape, title_dilation_window))
    element = cv.getStructuringElement(dilation_shape, (2 * dilatation_size + 1, 2 * dilatation_size + 1),
                                       (dilatation_size, dilatation_size))
    dilatation_dst = cv.dilate(src, element)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Code for Eroding and Dilating tutorial.')
    parser.add_argument('--input', help='Path to input image.', default='..\\data\\png_ball2.png')
    args = parser.parse_args()
    main(args.input)
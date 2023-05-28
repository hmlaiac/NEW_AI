```angular2html
To use OpenCV to detect basketballs in a video, you can follow these general steps:

Load the video: Use OpenCV's VideoCapture class to read the video frames.

Preprocess the frames: Convert the frames to grayscale, blur them to remove noise, and perform any other necessary preprocessing steps.

Detect edges: Use an edge detection algorithm, such as Canny edge detection, to detect the edges in the video frames.

Find contours: Use OpenCV's findContours function to identify the contours in the edge-detected frames.

Filter contours: Filter out any contours that don't have the expected size or shape of a basketball.

Draw bounding boxes: Draw bounding boxes around the remaining contours to highlight the detected basketballs.

Display the results: Display the processed frames with the detected basketballs.

Here's some sample code to get you started:

import cv2

# Load the video
cap = cv2.VideoCapture('video.mp4')

# Loop through the video frames
while cap.isOpened():

    # Read the frame
    ret, frame = cap.read()

    if ret:

        # Preprocess the frame
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)

        # Detect edges
        edges = cv2.Canny(blurred, 50, 150)

        # Find contours
        contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Filter contours
        for contour in contours:
            if cv2.contourArea(contour) > 500 and cv2.contourArea(contour) < 5000:
                (x, y, w, h) = cv2.boundingRect(contour)
                if w / h > 0.7 and w / h < 1.3:
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Display the processed frame
        cv2.imshow('Basketball Detection', frame)

        # Exit on key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    else:
        break

# Release the video capture and close the window
cap.release()
cv2.destroyAllWindows()
This code detects contours in each frame of the video, filters them based on area and aspect ratio, and draws a green bounding box around the remaining contours. You can adjust the filtering parameters to improve the accuracy of the detection.
```
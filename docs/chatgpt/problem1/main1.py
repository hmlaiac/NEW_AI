import cv2
import numpy as np
import time
# Load the video
cap = cv2.VideoCapture('video.mp4')
i = 0

# Loop through the video frames
while cap.isOpened():
    # Read the frame
    ret, frame = cap.read()

    if ret:

        # Preprocess the frame
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)

        # Detect circles
        circles = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT, 1, 20,
                                   param1=50, param2=30, minRadius=10, maxRadius=50)

        # Draw bounding boxes around the detected balls
        if circles is not None:
            circles = np.round(circles[0, :]).astype("int")
            for (x, y, r) in circles:
                # Crop the image
                # try:
                #     cropped_image = frame[y-r:y +r, x-r:x + r]
                #
                #     # Save the cropped image
                #
                #     name = "raw\\"+str(i)+".jpg"
                #     i = i+1
                #     print(name)
                #     cv2.imwrite(name, cropped_image)
                #     time.sleep(0.01)
                # except:
                #     pass

                cv2.circle(frame, (x, y), r, (0, 255, 0), -1)

        # Display the processed frame
        cv2.imshow('Ball Detection', frame)

        # Exit on key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    else:
        break
print(i)
# Release the video capture and close the window
cap.release()
cv2.destroyAllWindows()
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
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), -1)

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
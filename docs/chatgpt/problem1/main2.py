import cv2

# Load the video
cap = cv2.VideoCapture('video.mp4')

# Initialize the tracker
tracker = cv2.TrackerCSRT_create()

# Select the ROI
ret, frame = cap.read()
roi = cv2.selectROI('Select Ball', frame, False)
tracker.init(frame, roi)

# Loop through the video frames
while cap.isOpened():

    # Read the frame
    ret, frame = cap.read()

    if ret:

        # Preprocess the frame
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)

        # Track the ball
        success, roi = tracker.update(blurred)

        # Draw bounding box around the tracked ball
        if success:
            (x, y, w, h) = [int(i) for i in roi]
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), -1)

        # Display the processed frame
        cv2.imshow('Ball Tracking', frame)

        # Exit on key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    else:
        break

# Release the video capture and close the window
cap.release()
cv2.destroyAllWindows()
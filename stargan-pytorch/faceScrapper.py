import cv2
import face_recognition

# Get a reference to webcam
video_capture = cv2.VideoCapture("video/tbbt.mp4")

print("video capture::", video_capture)
length = int(video_capture.get(cv2.CAP_PROP_FRAME_COUNT))
print("Number of frames:", length)
# Initialize variables
face_locations = []

count = 0
while True:
    # Grab a single frame of video
    ret, frame = video_capture.read()

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_frame = frame[:, :, ::-1]

    print("Processing frame [{}/{}]".format(count, length))
    # print("finding the face")
    # Find all the faces in the current frame of video
    face_locations = face_recognition.face_locations(rgb_frame)

    # print("Writing a face image...")
    # Display the results
    extra = 100
    for top, right, bottom, left in face_locations:
        # Draw a box around the face

        top = top - extra
        bottom = bottom + extra
        left = left - extra
        right = right + extra
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        crop_img = frame[top:bottom, left:right]
        cv2.imwrite("data/sample/" + str(count) + ".jpg", crop_img)
    # Display the resulting image
    cv2.imshow('Video', frame)
    count += 1

    # print("Face image saved")
    # print("\n\n")
    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()
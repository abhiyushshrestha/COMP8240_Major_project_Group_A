import face_recognition
import os
import cv2
import glob

BASE_DIRECTORY = os.getcwd()
IMAGE_DIRECTORY = "/images"

FINAL_DIRECTORY = BASE_DIRECTORY+ IMAGE_DIRECTORY
FINAL_IMAGE_PATH = FINAL_DIRECTORY + "/final_image"
if not os.path.exists(BASE_DIRECTORY + "/final_image"):
    os.makedirs(BASE_DIRECTORY + "/final_image")


# image = cv2.imread("/media/abhiyush/New Volume/Macquarie/master_of_data_science/semester_3(session_2_2020)/COMP8240-Application_of_Data_Science/project/COMP8240_Major_project_Group_A/stargan-pytorch/data/celeba/000001.jpg")
# face_locations = face_recognition.face_locations(image)

image_folders = glob.glob(FINAL_DIRECTORY + "/*")
count = 0
for image_folder in image_folders:
    print("Processing folder {}".format(image_folder.split("/")[-1]))
    image_paths = glob.glob(image_folder + "/*.jpg")

    try:
        for image_path in image_paths:
            print("Processing image {}".format(image_path.split("/")[-1]))
            image = cv2.imread(image_path)
            face_locations = face_recognition.face_locations(image)

            # print("Writing a face image...")
            # Display the results
            extra = 100
            for top, right, bottom, left in face_locations:
                # Draw a box around the face

                top = top - extra
                bottom = bottom + extra
                left = left - extra
                right = right + extra
                cv2.rectangle(image, (left, top), (right, bottom), (0, 0, 255), 2)
                crop_img = image[top:bottom, left:right]

                cv2.imwrite(FINAL_IMAGE_PATH + "/" + str(count) + ".jpg", crop_img)
                count += 1

    except Exception as exec:
        print("There is an error...", exec)
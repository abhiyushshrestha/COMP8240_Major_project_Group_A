import face_recognition
import os
import cv2
import glob

BASE_DIRECTORY = os.getcwd()
IMAGE_DIRECTORY = "images2/raw"
FINAL_IMAGE_DIRECTORY = "images2"

FINAL_DIRECTORY = os.path.join(BASE_DIRECTORY, IMAGE_DIRECTORY)
FINAL_IMAGE_PATH = os.path.join(FINAL_IMAGE_DIRECTORY, "final_image")
if not os.path.exists(FINAL_IMAGE_PATH):
    os.makedirs(FINAL_IMAGE_PATH)


# image = cv2.imread("/media/abhiyush/New Volume/Macquarie/master_of_data_science/semester_3(session_2_2020)/COMP8240-Application_of_Data_Science/project/COMP8240_Major_project_Group_A/stargan-pytorch/data/celeba/000001.jpg")
# face_locations = face_recognition.face_locations(image)

image_folders = glob.glob(FINAL_DIRECTORY + "/*")
count = 0
# image_folder = '/media/abhiyush/New Volume/Macquarie/master_of_data_science/semester_3(session_2_2020)/COMP8240-Application_of_Data_Science/project/COMP8240_Major_project_Group_A/stargan-pytorch/images2/raw/youtube'
for image_folder in image_folders:
    print("Processing folder {}".format(image_folder.split("/")[-1]))
    image_paths = glob.glob(os.path.join(image_folder, "*.jpg"))
    try:
        for image_path in image_paths:
            # image_path = '/media/abhiyush/New Volume/Macquarie/master_of_data_science/semester_3(session_2_2020)/COMP8240-Application_of_Data_Science/project/COMP8240_Major_project_Group_A/stargan-pytorch/images2/raw/youtube/video_image_1.jpg'
            print("Processing image :: {}".format(image_path.split("/")[-1]))
            # try:
            image = cv2.imread(image_path)
            face_locations = face_recognition.face_locations(image)
            # print("Writing a face image...")
            # Display the results
            extra = 50
            height = image.shape[0]
            width = image.shape[1]
            # top, right, bottom,left = face_locations[0]
            for top, right, bottom, left in face_locations:
                # Draw a box around the face

                top = top - extra
                if top < 0:
                    top = 0

                bottom = bottom + extra
                if bottom > height:
                    bottom = height

                left = left - extra
                if left < 0:
                    left = 0

                right = right + extra
                if right > width:
                    right = width

                # cv2.rectangle(image, (left, top), (right, bottom), (0, 0, 255), 2)
                crop_img = image[top:bottom, left:right]
                cv2.imwrite(FINAL_IMAGE_PATH + "/" + str(count) + ".jpg", crop_img)
                count += 1
            # except Exception as exe:
            #     print("Error while processing image...")

    except Exception as exec:
        print("There is an error...", exec)
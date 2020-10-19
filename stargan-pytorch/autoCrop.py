from PIL import Image
from autocrop import Cropper
import glob
import os
import os
import cv2
import glob

cropper = Cropper()

# YOUTUBE_IMAGE_PATH = "/images/content/gdrive/My Drive/aods/images"
# YOUTUBE_CROPPES_IMAGE_PATH = "/images/content/gdrive/My Drive/aods/cropped_images"
#
# if not YOUTUBE_CROPPES_IMAGE_PATH:
# 	os.makedirs(YOUTUBE_CROPPES_IMAGE_PATH)
#
# YOUTUBE_IMAGE_LIST = os.path.join(YOUTUBE_IMAGE_PATH + "*.jpg")
# # Get a Numpy array of the cropped image
#
# for image_path in YOUTUBE_IMAGE_LIST:
# 	cropped_array = cropper.crop(image_path)
#
# 	# Save the cropped image with PIL
# 	cropped_image = Image.fromarray(cropped_array)
# 	cropped_image.save('cropped.jpg')
# 	cropped_image_path = os.path.join(YOUTUBE_CROPPES_IMAGE_PATH, image_path.split("/")[-1])
# 	cropped_image.save(cropped_image_path)


BASE_DIRECTORY = os.getcwd()
IMAGE_DIRECTORY = "images2/raw"
FINAL_IMAGE_DIRECTORY = "images2"

FINAL_DIRECTORY = os.path.join(BASE_DIRECTORY, IMAGE_DIRECTORY)
# FINAL_IMAGE_PATH = os.path.join(FINAL_DIRECTORY, "final_image")
FINAL_IMAGE_PATH_AC = os.path.join(FINAL_IMAGE_DIRECTORY, "final_image_ac")

if not os.path.exists(FINAL_IMAGE_PATH_AC):
	os.makedirs(FINAL_IMAGE_PATH_AC)

# image = cv2.imread("/media/abhiyush/New Volume/Macquarie/master_of_data_science/semester_3(session_2_2020)/COMP8240-Application_of_Data_Science/project/COMP8240_Major_project_Group_A/stargan-pytorch/data/celeba/000001.jpg")
# face_locations = face_recognition.face_locations(image)

image_folders = glob.glob(FINAL_DIRECTORY + "/*")
count = 0
image_folder = '/media/abhiyush/New Volume/Macquarie/master_of_data_science/semester_3(session_2_2020)/COMP8240-Application_of_Data_Science/project/COMP8240_Major_project_Group_A/stargan-pytorch/images1/youtube'
for image_folder in image_folders:
	print("Processing folder {}".format(image_folder.split("/")[-1]))
	image_paths = glob.glob(os.path.join(image_folder, "*.jpg"))
	try:
		for image_path in image_paths:
			print("Processing image :: {}".format(image_path.split("/")[-1]))
			image_path =  '/media/abhiyush/New Volume/Macquarie/master_of_data_science/semester_3(session_2_2020)/COMP8240-Application_of_Data_Science/project/COMP8240_Major_project_Group_A/stargan-pytorch/images1/youtube/video_image_1.jpg'
			cropped_array = cropper.crop(image_path)

			# Save the cropped image with PIL
			try:
				cropped_image = Image.fromarray(cropped_array)
				# cropped_image_path = os.path.join(YOUTUBE_CROPPES_IMAGE_PATH, image_path.split("/")[-1])
				image_filename = os.path.join(FINAL_IMAGE_PATH_AC, str(count) + ".jpg")
				cropped_image.save(image_filename)
				count += 1
			except Exception as e:
				print("ERROR:::", e)

	except Exception as exec:
		print("There is an error...", exec)
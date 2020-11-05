import cv2
import glob
import os 

BASE_DIRECTORY = os.getcwd()
IMAGE_DIRECTORY = "images2/final_image"
FINAL_RESIZED_IMAGE = "images2\\resized_final_image"

IMAGE_TO_CROPPED_DIRECTORY = os.path.join(BASE_DIRECTORY, IMAGE_DIRECTORY)
FINAL_RESIZED_IMAGE_DIRECTORY = os.path.join(BASE_DIRECTORY, FINAL_RESIZED_IMAGE)

if not os.path.exists(FINAL_RESIZED_IMAGE_DIRECTORY):
    os.makedirs(FINAL_RESIZED_IMAGE_DIRECTORY)

images= glob.glob(os.path.join(IMAGE_TO_CROPPED_DIRECTORY, "*.jpg"))
count = 0
# image_folder = '/media/abhiyush/New Volume/Macquarie/master_of_data_science/semester_3(session_2_2020)/COMP8240-Application_of_Data_Science/project/COMP8240_Major_project_Group_A/stargan-pytorch/images2/raw/youtube'
width = 178
height = 218
dim = (width, height)

for image in images:
	image_name = image.split("/")[-1]
	print("Processing image:: {}".format(image_name))
	try:
		img = cv2.imread(image, cv2.IMREAD_UNCHANGED)

		print('Original Dimensions : ',img.shape)
		# resize image
		resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
		 
		print('Resized Dimensions : ',resized.shape)

		SAVE_IMAGE_PATH = os.path.join(FINAL_RESIZED_IMAGE_DIRECTORY, image_name)
		cv2.imwrite(SAVE_IMAGE_PATH, resized)

	except Exception as exec:
		print("There is an error...", exec)


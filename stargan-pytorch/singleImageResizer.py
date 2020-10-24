import cv2

width = 178
height = 218
dim = (width, height)

img = cv2.imread("b.png", cv2.IMREAD_UNCHANGED)

print('Original Dimensions : ',img.shape)
# resize image
resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
 
print('Resized Dimensions : ',resized.shape)

cv2.imwrite("b_resized.jpg", resized)
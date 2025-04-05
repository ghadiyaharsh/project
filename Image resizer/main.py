#dimension of image 275*183
#height 183 pixels
#width  275 pixels

import cv2 #importing opencv library

image = cv2.imread("D:\pii\PYP-Project\project\Image resizer\download(nature).jpg",cv2.IMREAD_UNCHANGED)  #reading image from the path
#cv2.IMREAD_UNCHANGED is used to read the image as it is without any changes

cv2.imshow("titel",image) #displaying image in a window with title "titel"

scale_percent = 50 # percent of original size
new_width = int(image.shape[1] * scale_percent / 100)  #calculating new width
#image.shape[1] gives the width of the image
new_height = int(image.shape[0] * scale_percent / 100)  #calculating new height
#image.shape[0] gives the height of the image

output = cv2.resize(image, (new_width, new_height))
cv2.imwrite("resized_image.jpg", output)
cv2.waitKey(0)  #wait for a key event indefinitely
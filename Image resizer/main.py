#dimension of image 275*183
#height 183 pixels
#width  275 pixels

import cv2

image = cv2.imread("D:\pii\PYP-Project\project\Image resizer\download(nature).jpg",cv2.IMREAD_UNCHANGED)
cv2.imshow("titel",image)

scale_percent = 50 # percent of original size
new_width = int(image.shape[1] * scale_percent / 100)
new_height = int(image.shape[0] * scale_percent / 100)

output = cv2.resize(image, (new_width, new_height))
cv2.imwrite("resized_image.jpg", output)
cv2.waitKey(0)
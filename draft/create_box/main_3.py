import numpy as np
import cv2
from PIL import Image, ImageDraw

img = np.zeros((512, 512, 3), dtype = "uint8")
img = Image.open('white_img.png')
img = cv2.imread('white_img.png')
penta = np.array([[[40,160],[120,100],[200,160],[160,240],[80,240]]], np.int32)
triangle = np.array([[[240, 130], [380, 230], [190, 280]]], np.int32)
cv2.polylines(img, [triangle], True, (0,255,0), thickness=3)

img_mod = cv2.polylines(img, [penta], True, (255,120,255),3)

cv2.imshow('Shapes', img_mod)

cv2.waitKey(0)
cv2.destroyAllWindows()
# USAGE
# python stitch.py --first images/bryce_left_01.png --second images/bryce_right_01.png 

# import the necessary packages
from panorama import Stitcher
import imutils
import cv2
import time

start_time = time.time()
# load the two images and resize them to have a width of 400 pixels
# (for faster processing)
imageA = cv2.imread("images/left2.png")
imageB = cv2.imread("images/right2.png")
imageA = imutils.resize(imageA, width=400)
imageB = imutils.resize(imageB, width=400)

# stitch the images together to create a panorama
stitcher = Stitcher()
(result, vis) = stitcher.stitch([imageA, imageB], showMatches=True)
print("--- %s seconds ---" % (time.time() - start_time))




# show the images
cv2.imshow("Image A", imageA)
cv2.imshow("Image B", imageB)
cv2.imshow("Keypoint Matches", vis)
cv2.imshow("Result", result)

cv2.waitKey(0)
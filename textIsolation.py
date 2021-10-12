import cv2 as cv
import sys

img = cv.imread(cv.samples.findFile("C:\\Users\\97152\\Source\\Repos\\bandi72006\\IICH\\Images\\testText.png"))

if img is None:
    print("image could not be read")

cv.imshow("display", img)
k = cv.waitKey(0)
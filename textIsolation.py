import cv2 as cv
import sys

img = cv.cvtColor(cv.imread(cv.samples.findFile("C:\\Users\\97152\\Source\\Repos\\bandi72006\\IICH\\Images\\testText2.png")), cv.COLOR_BGR2GRAY)

if img is None:
    print("image could not be read")

cv.imshow("display", img)
cv.waitKey(0)

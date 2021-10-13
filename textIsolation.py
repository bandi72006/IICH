import cv2 as cv
import sys
img = None

img = cv.cvtColor(cv.imread(cv.samples.findFile("C:\\Users\\97152\\Source\\Repos\\bandi72006\\IICH\\Images\\testText2.png")), cv.COLOR_BGR2GRAY)


if img is None:
    print("image could not be read")
    sys.exit("ERROR:NO IMAGE FOUND")

cv.imshow("display", img)
cv.waitKey(0)

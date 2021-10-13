import cv2 as cv
import numpy as np
import sys

cropy=np.array([])


#locate image and set to greyscale, store as img
img = cv.imread(cv.samples.findFile("Images\\testText.png"), 0)


def cropY(imgToCropY):
    cropy=np.array([])
    for ydim1 in range(len(imgToCropY)):
        if not (np.all(imgToCropY[ydim1] == img[ydim1][0])):
            cropy = np.append(cropy, ydim1).astype(int)
        else:
            print(False)
    return imgToCropY[np.min(cropy):np.max(cropy)+1]



cv.imshow("aa", cropY(img))
cv.waitKey(0)
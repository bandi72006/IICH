import cv2 as cv
import numpy as np

img = cv.imread(cv.samples.findFile("Images\\testText.png"), 0)

def cropY(imgToCropY):
    
    cropy=np.array([])
    
    for ydim1 in range(len(imgToCropY)):
        if not (np.all(imgToCropY[ydim1] == imgToCropY[ydim1][0])):
            cropy = np.append(cropy, ydim1).astype(int)
    
    return imgToCropY[np.min(cropy):np.max(cropy)+1]

def cropX(imgToCropX):

    cropx=np.array([])
    print(len(imgToCropX[0]))
    for xdim1 in range(len(imgToCropX[0])):
        if (np.all(imgToCropX == imgToCropX[xdim1][0], 0)):
            cropx = np.append(cropx, xdim1).astype(int)

    return imgToCropX[np.min(cropx):np.max(cropx)+1]


cv.imshow("og", img)
cv.imshow("cropy", cropY(img))
cv.imshow("cropy", cropX(img))
cv.waitKey(0)
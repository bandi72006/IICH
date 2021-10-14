import cv2 as cv
import numpy as np

img = cv.imread(cv.samples.findFile("Images\\testText.png"), 0)

def cropY(imgToCropY):
    
    cropy=np.array([])
    
    for ydim1 in range(len(imgToCropY)):
        if not (np.all(imgToCropY[ydim1] == imgToCropY[ydim1][0])):
            cropy = np.append(cropy, ydim1).astype(int)
    
    return imgToCropY[np.min(cropy):np.max(cropy)+1]

def cropX(imgTocropY):
    a = 0
    b = np.all(img == 255, 0)
    c = np.array([]).astype(int)  
    for obj in b:
        if not obj:
            c = np.append(c, a)
        a += 1
    
    print(a,b,c)
    return imgTocropY[np.min(c):np.max(c)+1]




cv.imshow("og", img)
cv.imshow("cropy", cropY(img))
cv.imshow("cropx", cropX(img))
cv.waitKey(0)
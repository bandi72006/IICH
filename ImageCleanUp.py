import cv2 as cv
import numpy as np
from writingRater import *


img = cv.imread(cv.samples.findFile("Images\\testText.png"), 0)

#def cropY(imgToCropY):
#    
#    cropy=np.array([])
#    
#    for ydim1 in range(len(imgToCropY)):
#        if not (np.all(imgToCropY[ydim1] == imgToCropY[ydim1][0])):
#            cropy = np.append(cropy, ydim1).astype(int)
#    
#    return imgToCropY[np.min(cropy):np.max(cropy)+1]

def cropX(X):
    a = 0
    b = np.all(img == 255, 0)   #returns an array with the evaluation of every item in dim0 == 255
    c = np.array([]).astype(int)  
    
    for obj in b:
        
        if not obj:
            
            c = np.append(c, a)
       
        a += 1
    
    return X[:, np.min(c):np.max(c)+1]

def cropY(Y):
    a = 0
    b = np.all(img == 255, 1)   #returns an array with the evaluation of every item in dim1 == 255
    c = np.array([]).astype(int)  
    
    for obj in b:
        
        if not obj:
            
            c = np.append(c, a)
       
        a += 1
        
    return Y[np.min(c):np.max(c)+1]

def cropXY(XY):
    
    return cropX(cropY(XY))

xHeight = getXHeight(img)
print(xHeight)

cv.imshow("og", img)
cv.imshow("cropped", cropXY(img))
cv.waitKey(0)
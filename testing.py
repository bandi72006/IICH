import cv2 as cv
import numpy as np

img = cv.imread(cv.samples.findFile("Images\\testText.png"), 0)

n=0
ydim = np.all(img == 255, 0)
for obj in ydim:
    
    if obj:
        ydim[n] = n
        print(ydim[n])
        print("pass")
    n +=1
print(ydim)

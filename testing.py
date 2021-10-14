import cv2 as cv
import numpy as np

img = cv.imread(cv.samples.findFile("Images\\testText.png"), 0)

ydim2 = np.array([]).astype(int)
ydim = np.all(img == 255, 0)
n = 0
for obj in ydim:
    
    if not obj:
        ydim2 = np.append(ydim2, n)


    n +=1
img = img[:, np.min(c):np.max(c)+1]
print(ydim2)

img = np.delete(img, ydim2, 1)
cv.imshow("test", img)
cv.waitKey(0)
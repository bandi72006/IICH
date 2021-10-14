import cv2 as cv
import numpy as np

def getXHeight(Y):
    best = [0,0]
    for i in range(len(Y)):
        count = 0
        print(len(Y[i]))
        for j in range(len(Y[i])):
            if Y[i][j] != 255:
                
                count += 1
            

        if count > best[0]:
            best = [count, i]
    
    return best[1]
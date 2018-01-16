import numpy as np
import cv2


def mse(imageA, imageB):
    err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    err /= float(imageA.shape[0] * imageA.shape[1])
    return err

def compare_images(imageA, imageB):
    m = mse(imageA, imageB)
    return m

z = 1
k = 1
n = 2
nf = 29168

for i in range(0, nf-1):
#while True:
    a = cv2.imread("frames\\"+ str(k) +".jpg",0)
    b = cv2.imread("frames\\"+ str(n) +".jpg",0)

    m = compare_images(a,b)
    if m >= 5 :
        cv2.imwrite("D:\\Minor2\\PROJECT\\final_output_mse_5\\"+ str(z) +".jpg" , a)
        z = z+1
        print(k,n,m)
        k = n
        n = k+1


    else :
        print(k,n,m)
        n = n+1
 

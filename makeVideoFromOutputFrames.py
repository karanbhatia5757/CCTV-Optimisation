import numpy as np
import cv2


# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('final_output.avi',fourcc, 25.0, (640,384))

i=1

nf = 10512

# while True:
for i in range (0,nf-1) :
        out.write("D:\\Minor2\\video to frames\\final_output\\" + str(i) + ".jpg")
        i = i+1
        

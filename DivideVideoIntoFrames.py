import cv2

vc = cv2.VideoCapture('D:\\Minor2\\PROJECT\\test.mp4')
c=1

if vc.isOpened():
    rval , frame = vc.read()
    
else:
    rval=False
    print("error")
    
while rval:
    rval, frame = vc.read()
    cv2.imwrite("D:\\Minor2\\PROJECT\\frames\\" + str(c) + '.jpg',frame)
    c = c + 1
    cv2.waitKey(1)

vc.release()

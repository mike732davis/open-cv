import cv2
cam = cv2.VideoCapture(0)
while True:
    check, frame = cam.read()
    cv2.imshow('video', frame)
    key = cv2.waitKey(1)
    for i in range(0,5):
        i=str(i)
        save=cv2.imwrite('Images'+'/'+i+'.jpeg',frame)
    if key == 27:
        break
cam.release()
cv2.destroyAllWindows()
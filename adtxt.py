import cv2
img=cv2.imread('LuffyGear5.jpeg')
imgrs=cv2.resize(img,(720, 720),interpolation=cv2.INTER_NEAREST)
adtxt=cv2.putText(
     imgrs, #numpy array on which text is written
     "Monkey D Luffy Gear 5", #text
     (100,30), #position at which writing has to start
     cv2.FONT_HERSHEY_SIMPLEX, #font family
     1, #font size
     (20, 20, 200, 255), #font color
     3) #font stroke
#cv2.imshow('image',imgrs)
save=cv2.imwrite('Images\adtxt.jpeg',adtxt)
print('image Written Success : ',save)
cv2.waitKey(0)
cv2.destroyAllWindows()
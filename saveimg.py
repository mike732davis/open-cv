import cv2
img=cv2.imread('LuffyGear5.jpeg')
img0=cv2.imread('LuffyGear5.jpeg',0)
imgrs=cv2.resize(img,(720, 720),interpolation=cv2.INTER_NEAREST)
imgrot=cv2.rotate(imgrs,cv2.ROTATE_90_COUNTERCLOCKWISE)
#cv2.imshow('image',imgrs)
#cv2.imshow('rotate',imgrot)
save=cv2.imwrite('Images\imgrs.jpg',imgrs)  
print("Image written sucess? : ", save)
savrot=cv2.imwrite('Images\imgrot.jpg',imgrot)
savbw=cv2.imwrite('Images\imgbw.jpg',img0)
cv2.waitKey(0)
cv2.destroyAllWindows()
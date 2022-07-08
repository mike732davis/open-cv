import cv2
img=cv2.imread('LuffyGear5.jpeg')
print(img.shape)
imgrs=cv2.resize(img,(720, 720),interpolation=cv2.INTER_NEAREST)
print(imgrs.shape)
cv2.imshow('image',imgrs)
cv2.waitKey(0)
cv2.destroyAllWindows()
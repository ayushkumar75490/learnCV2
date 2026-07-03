import cv2

img = cv2.imread('output.jpg') 

if img is None:
    print("img is loaded")
else:
    res = cv2.resize(img, (200, 200))
    cv2.imshow('cow', res)  
    cv2.waitKey(0)
    cv2.destroyAllWindows()

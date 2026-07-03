import cv2
img = cv2.imread('output.jpg') 
if img is None :
    print("Could not load image")
else:
    w,h = img.shape[:2]                #get width and height of image
    print(f"width: {w}, height: {h}")

    slice=img[50:200, 50:150]     #slice image/ crop image
    cv2.imshow('cow', slice)  
    cv2.waitKey(0)
    cv2.destroyAllWindows()

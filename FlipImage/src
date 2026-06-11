import cv2

img = cv2.imread("output.jpg")

if img is None:
    print("image is not loaded")
else:
    cv2.imshow("original image : ", img)
    cv2.imshow("horizontal flip image : ", cv2.flip(img, 1) )
    cv2.imshow("vertical flip image : ", cv2.flip(img, 0) )
    cv2.imshow("diagonal flip image : ", cv2.flip(img, -1) )

    cv2.waitKey(0)
    cv2.destroyAllWindows()


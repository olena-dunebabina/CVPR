import cv2 as cv

def webcam(image):
    gr_img = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    gray= cv.cvtColor(gr_img, cv.COLOR_GRAY2BGR)
    cv.rectangle(gray, (20,20), (80,80), (255,0,255), 3)
    cv.line(gray, (85,85), (120,85), (125,20,95) ,4)
    return gray

camera = cv.VideoCapture(0)   
res, img = camera.read()
if res:   
    cv.namedWindow("result", flags=cv.WINDOW_AUTOSIZE)
    cv.imshow("result", img)
    cv.waitKey(0)
    cv.imwrite("webphoto.jpg", img) 

image = cv.imread("webphoto.jpg")
cv.imshow("result-grey", webcam(image))
cv.imwrite("webphoto-grey.jpg", webcam(image))
cv.waitKey(0)
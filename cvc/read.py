import cv2 as cv
# img = cv.imread('./pic/cat.jpg')
# cv.imshow('cat', img)

capture = cv.VideoCapture('video/cat.mp4')

while True:
    isTrue , frame = capture.read()
    cv.imshow('video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()

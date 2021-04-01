import cv2 as cv

img  = cv.imread('pic/cat.jpg')
cv.imshow('cat', img)

def rescaleFrame (frame, scale = 0.75):
    width = int (frame.shape[1]*scale)
    length = int (frame.shape[0]*scale)
    dimensions = (width, length)
    return cv.resize(frmae, dimensions,interpolation = cv.INTER_AREA)

capture = cv.VideoCapture('video/cat.mp4')

while True:
    isTrue , frame = capture.read()
    cv.imshow('video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()

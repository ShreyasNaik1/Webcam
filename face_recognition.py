import cv2
import sys

cascPath = None
if sys.argv[1]:
    cascPath = sys.argv[1]
else: 
    cascPath = None



faceCascade = cv2.CascadeClassifier(cascPath)

video_capture = cv2.VideoCapture(0)

while True:
    ret, frame = video_capture.read()
    greyscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    feature = faceCascade.detectMultiScale(
        greyscale,
        scaleFactor=1.1,
        minNeighbors=10,
        minSize=(25, 25),
        flags=cv2.cv.CV_HAAR_SCALE_IMAGE
    )

    for (x, y, w, h) in feature:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
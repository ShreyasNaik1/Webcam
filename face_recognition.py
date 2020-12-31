import cv2
import sys
import feature_recognition_window as frw

def main():
    frw.func()
    casc = frw.get_ret()
    if not casc:
        return

    feature_cascade = cv2.CascadeClassifier(casc)
    vid = cv2.VideoCapture(0)

    while True:
        _, frame = vid.read()
        greyscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        feature = feature_cascade.detectMultiScale(
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

    vid.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
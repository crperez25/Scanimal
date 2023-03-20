#openCV has been installed allowing it to be imported for the camera.
import cv2
video=cv2.VideoCapture(0)

while (True):
    ret, frame=video.read()
    cv2.imshow("Scan", frame)
    if cv2.waitKey(1) & 0xFF==ord('a'):
        break
vid.release()
cv2.destroyAllWindows
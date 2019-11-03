import cv2,time
from datetime import datetime
video = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
smile_cascade = cv2.CascadeClassifier("haarcascade_smile.xml")
while True:
    check,frame = video.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.05,5)
    for x,y,w,h in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
        ros_gray = gray[y:y+h,x:x+w]
        ros_img= frame[y:y+h,x:x+w]
        smile = smile_cascade.detectMultiScale(ros_gray,1.8,20)
        for ex,ey,ew,eh in smile:
            cv2.rectangle(ros_img,(ex,ey),(ex+ew,ey+eh),(0,255,0),5)

    cv2.imshow("Capturing",frame)
    key = cv2.waitKey(1)
    if key == ord("q"):
        break
video.release()
cv2.destroyAllWindows()


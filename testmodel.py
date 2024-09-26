import cv2
video = cv2.VideoCapture(0)
facedetect = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

recognizer = cv2.face.LBPHFaceRecognizer_create(radius=2, neighbors=8, grid_x=8, grid_y=8)
recognizer.read("trainer.yml")
name_list = ["","zayed","Hamdan","Amni"]

while True:
    ret,frame = video.read()
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = facedetect.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=6)

    for (x,y,w,h) in faces :
        serial,conf=recognizer.predict(gray[y:y+h,x:x+w])
        if conf > 90:
            cv2.putText(frame,name_list[serial],(x,y-40),cv2.FONT_HERSHEY_SIMPLEX,1,(50,50,255),2)
            cv2.rectangle(frame , (x,y),(x+w , y+h),(50,50,255),1)
        else:   
            cv2.putText(frame,"unknown",(x,y-40),cv2.FONT_HERSHEY_SIMPLEX,1,(50,50,255),2)
            cv2.rectangle(frame , (x,y),(x+w , y+h),(50,50,255),1)

        
    cv2.imshow("Frame",frame)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
video.release()
cv2.destroyAllWindows()
print("Dataset collection completed")

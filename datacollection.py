import cv2
video = cv2.VideoCapture(0)
facedetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
id = input("Enter your ID")
count =0


while True:
    ret,frame = video.read()
    # Resize frame for faster processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
    gray = cv2.cvtColor(small_frame, cv2.COLOR_BGR2GRAY)
    faces = facedetect.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)


    for (x,y,w,h) in faces :
        count = count+1
        cv2.imwrite('datasets/User.' +str(id)+"."+str(count)+".jpg",gray[y:y+h,x:x+w])
        cv2.rectangle(frame,(x,y),(x+w ,y+h), (50,50,255),1)
    cv2.imshow("Frame",frame)
    k=cv2.waitKey(1)
    if count>500:
        break
video.release()
cv2.destroyAllWindows()
print("Dataset collection completed")

import cv2

cap = cv2.VideoCapture(0)

# Check if the webcam is opened correctly
if not cap.isOpened():
    raise IOError("Cannot open webcam")

while True:
    ret, frame = cap.read()
    #frame = cv2.resize(frame, None, fx=1, fy=1,
    #                  interpolation=cv2.INTER_AREA)
    #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    haar = cv2.CascadeClassifier('cascade.xml')
    #haar = cv2.CascadeClassifier('eye_detect.xml')
    haar_rect = haar.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=3)

    for(x,y,w,h) in haar_rect:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), thickness=2)
    
    cv2.imshow('My Camera', frame)

    c = cv2.waitKey(1)
    if c == 27:
        break

cap.release()
cv2.destroyAllWindows()

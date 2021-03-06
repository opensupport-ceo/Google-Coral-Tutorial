import cv2
import os

baseDir = os.getcwd()
sampleDir = os.path.join(baseDir, os.pardir, "sample")
haarDir = os.path.join(baseDir, os.pardir, "haar", "data", "haarcascades")

faceCascade = cv2.CascadeClassifier(os.path.join(haarDir, "haarcascade_frontalface_default.xml"))
eyeCascade = cv2.CascadeClassifier(os.path.join(haarDir, "haarcascade_eye.xml"))

frame = cv2.imread(os.path.join(sampleDir, "woman_face.jpg"))
frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(frame_gray, 1.7, 10)
print(faces)

for (x,y,w,h) in faces :
    cv2.rectangle(frame, (x,y), (x+w, y+h), (255, 0, 0), 2)
    roi = frame[y:y+h, x:x+w]
    roiGray = frame_gray[y:y+h, x:x+w]

    eyes = eyeCascade.detectMultiScale(roiGray, 1.5, 5, minSize=(100, 100), maxSize=(150, 150))
    print(eyes)
    for (ex, ey, ew, eh) in eyes :
        cv2.rectangle(roi, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)

cv2.imwrite("eyeRecognition.png", frame)
cv2.imwrite("roi.png", roi)

import imutils
import time
import cv2
import csv
import os

alg = 'haarcascade_frontalface_default.xml'
detector = cv2.CascadeClassifier(alg)

Name = str(input("Enter your Name : "))
Roll_Number = str(input("Enter your Roll_Number : "))
dataset = 'Dataset'
sub_data = Name
path = os.path.join(dataset, sub_data)

if not os.path.isdir(path):
    os.mkdir(path)
    print(sub_data)

info = [str(Name), str(Roll_Number)]
with open('student_data.csv','a') as csvFile:
    write = csv.writer(csvFile)
    write.writerow(info)
csvFile.close()

print("Starting video stream...")
cam = cv2.VideoCapture(0)
time.sleep(2.0)
total = 0

while total < 100:
    print(total)
    _, frame = cam.read()
    img = imutils.resize(frame, width=400)
    grayimg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    rects = detector.detectMultiScale(grayimg, scaleFactor=1.1, minNeighbors= 5, flags=cv2.CASCADE_SCALE_IMAGE, minSize=(30,30))

    for (x, y, w, h) in rects:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        p = os.path.sep.join([path, "{}.png".format(str(total).zfill(5))])
        cv2.imwrite(p, img)
        total += 1

    cv2.imshow("Frame", frame)
    if cv2.waitKey(1)==ord("q"): 
        break

cam.release()
cv2.destroyAllWindows()

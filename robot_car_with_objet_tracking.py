# import cv2

# imagePath = "input.jpg"

# img = cv2.imread(imagePath)
# img.shape
# gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# gray_image

# face_clasifier = cv2.CascadeClassifier(cv2.data.haarcascades +  'haarcascade_frontalface_alt.xml')
# face = face_clasifier.detectMultiScale(gray_image, scaleFactor = 1.1, minNeighbors = 5, minSize = (4, 40))
# for (x, y, w, h) in face:
#     bbox = (x, y, w, h)
#     cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    


import cv2
import serial
import Rpi.GPIO


face_classfier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_alt.xml")

video_capture = cv2.VideoCapture(0)
def detect_bounding_box(vid):
    
    gray_image = cv2.cvtColor(vid, cv2.COLOR_BGR2GRAY)
    faces = face_classfier.detectMultiScale(gray_image, 1.1, 5, minSize = (40, 40))
    width,height,ch = vid.shape
    center_frame = (width/2), (height/2)
    x,y,w,h = faces[0]
    cv2.rectangle(vid, (x,y), (x + w, y + h), (0, 255, 0), 4)

    center_object = ((x + w)/2), ((y + h)/2)
    area_object = ((x+w)*(y+h))
    area_desired = (width-1000)*(height-1000)


    a,b = center_frame
    c,d = center_object
    if (c < (a-20)):
        ser.write(str.encode("l"))
    elif (c > (a+20)):
        ser.write(str.encode("r"))
    if (area_object > 5000):
        ser.write(str.encode("b"))
    if (area_object < 5000):
        ser.write(str.encode("f"))
    
        

    return vid
while True:
    result, video_frame = video_capture.read() 
    if result is False:
        break
    faces = detect_bounding_box(video_frame)
    cv2.imshow("My Face Detection Project", faces)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows

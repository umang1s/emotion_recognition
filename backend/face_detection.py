
import numpy as np
import cv2
import model as mdl


def using_open_cv_haarcascade():
    frontal_xml="..\learn\open_cv_data\haarcascades\haarcascade_frontalface_default.xml"
    faceCascade=cv2.CascadeClassifier(frontal_xml)
    video=cv2.VideoCapture(0)

    while(True):
         
        ret , frame=video.read()
        #frame=cv2.flip(frame)
        frame = cv2.resize(frame, (600, 400))
 
        faces = faceCascade.detectMultiScale2(frame, scaleFactor=1.1, minNeighbors=5, flags=cv2.CASCADE_SCALE_IMAGE)
 
        for (x, y, w, h) in faces[0]:
            conf = faces[1][0][0]
            if conf > 5:
                text = f"{conf*10:.2f}%"
                cv2.putText(frame, text, (x, y-20), 
                            cv2.FONT_HERSHEY_SIMPLEX, 1,(170, 170, 170), 1)

                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 255, 255), 1)
        
        cv2.imshow("Frame", frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
 
    video.release()
    cv2.destroyAllWindows()



def getEmotionData(img):
    arr=[]
    for i in range(2):
        arr.append(mdl.EmotionData())
    cv2.imshow("Image",img)
    return mdl.ConvertEmotionDataToJsonFile(arr)

using_open_cv_haarcascade()

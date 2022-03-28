from keras.models import model_from_json
import mediapipe as mp
import os
import cv2
from keras.preprocessing import image
import numpy as np
import mediapipe.framework.formats.detection_pb2

class Emotion:

    def __init__(self, haarfile="null"):
        self.HaarFile=haarfile
        self.EMOTIONS=["angry","disgusted","fearful","happy","neutral","sad","surprised"] #don't update
        self.weights_file="weight.h5"
        self.json_file="weight_json.json"
        if haarfile != "null":
            self.haar_caascade=cv2.CascadeClassifier(self.HaarFile)
        else:
            self.mpResult=mp.solutions.face_detection
            self.faceDetection=self.mpResult.FaceDetection(model_selection=0, min_detection_confidence=0.5)
            self.faceDraw=mp.solutions.drawing_utils
            self.drawSpec=self.faceDraw.DrawingSpec(thickness=1,circle_radius=2)
        self.modelPresent=os.path.isfile("data/"+self.weights_file) and os.path.isfile("data/"+self.json_file)

        ### loading weights
        if not self.modelPresent:
            print("Model not availble Please train your model")
        else:
            self.trained_model = model_from_json(open("data/"+self.json_file, "r").read())
            self.trained_model.load_weights("data/"+self.weights_file)



    def recognizeEmotion(self,img):
        ret=[]
        if self.HaarFile!="null":
            gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            faces=self.haar_caascade.detectMultiScale(gray_img,1.20,4)
            for (x,y,w,h) in faces:
                emo_name=self.EMOTIONS[0]
                emo_value=-1
                if self.modelPresent:
                    crp_img=self.cropImage(img,x,y,w,h)
                    output=self.trained_model.predict(crp_img)
                    print(output)

                    max_index =np.argmax(output[0])
                    emo_value=output[0][max_index]*100
                    emo_name=self.EMOTIONS[max_index]
                ret.append((x,y,w,h,emo_value,emo_name))
        else:
            faceResult=self.faceDetection.process(img)
            if faceResult.detections is not None:
                for location in faceResult.detections:
                    box=location.location_data.relative_bounding_box
                    emo_name=self.EMOTIONS[0]
                    emo_value=-1
                    shape=img.shape
                    x,y,w,h=int(box.xmin*shape[1]),int(box.ymin*shape[0]),int(box.width*shape[1]),int(box.height*shape[0])
                    if self.modelPresent:
                        crp_img=self.cropImage(img,x,y,w,h)
                        output=self.trained_model.predict(crp_img)
                        print(output)

                        max_index =np.argmax(output[0])
                        emo_value=output[0][max_index]*100
                        emo_name=self.EMOTIONS[max_index]
                    ret.append((x,y,w,h,emo_value,emo_name))

        return  ret
    
    def cropImage(self,img,x,y,w,h):
        cropped=img[y:y+w,x:x+h]
        resized=cv2.resize(cropped,(48,48))
        gray_img=cv2.cvtColor(resized,cv2.COLOR_BGR2GRAY)
        img_pixels = image.img_to_array(gray_img)
        img_pixels = np.expand_dims(img_pixels, axis = 0)
        return img_pixels
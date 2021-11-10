import backend.model.constants as constants
from keras.models import model_from_json
import mediapipe as mp
import cv2
from keras.preprocessing import image
import numpy as np
class Emotion:

    def __init__(self,model_algorithm,haarfile="null"):
        self.HaarFile=haarfile
        self.ModelAlgo=model_algorithm
        print(haarfile)
        if model_algorithm==constants.CNN:
            self.haar_caascade=cv2.CascadeClassifier(self.HaarFile)

        else:
            self.mpResult=mp.solutions.face_mesh
            self.faceMesh=self.mpResult.FaceMesh(max_num_faces=2)
            self.faceDraw=mp.solutions.drawing_utils
            self.drawSpec=self.faceDraw.DrawingSpec(thickness=1,circle_radius=2)

    def load_model(self):
        print("Checking trained model")
        import os
        if self.ModelAlgo==constants.CNN:
            self.modelPresent=os.path.isfile(constants.CNN_WEIGHTS) and os.path.isfile(constants.CNN_JSON)
            if(self.modelPresent):
                self.trained_model = model_from_json(open(constants.CNN_JSON, "r").read())
                self.trained_model.load_weights(constants.CNN_WEIGHTS)
        else:
            self.modelPresent=os.path.isfile(constants.OUR_WEIGHTS)

        if not self.modelPresent:
            print("Model not availble Please train your model")
        return True


    def recognizeEmotion(self,img):
        ret=[]
        if self.ModelAlgo==constants.CNN:
            gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            faces=self.haar_caascade.detectMultiScale(gray_img,1.20,4)
            for(x,y,w,h) in faces:
                box=constants.Box(x,y,h,w)
                emotion=constants.Emotion(constants.EMOTIONS[1],0)
                if self.modelPresent:
                    crp_img=self.cropImage(img,x,y,w,h)
                    output=self.trained_model.predict(crp_img)
                    max_index =np.argmax(output[0])
                    emotion.Value=output[0][max_index]*100
                    emotion.Name=constants.EMOTIONS[max_index]
                ret.append((box,emotion))
        else:
            faceResult=self.faceMesh.process(img)
            if faceResult.multi_face_landmarks:
                for face in faceResult.multi_face_landmarks:
                    self.faceDraw.draw_landmarks(img,face,self.mpResult.FACEMESH_CONTOURS,self.drawSpec,self.drawSpec)


        return  ret
    
    def cropImage(self,img,x,y,w,h):
        cropped=img[y:y+w,x:x+h]
        resized=cv2.resize(cropped,(48,48))
        gray_img=cv2.cvtColor(resized,cv2.COLOR_BGR2GRAY)
        img_pixels = image.img_to_array(gray_img)
        img_pixels = np.expand_dims(img_pixels, axis = 0)
        return img_pixels


    def train_model(self,epoch=2):
        if self.ModelAlgo==constants.CNN:
            import backend.cnn_train as ct
            ct.start_training(epoch,constants.CURRENT_DIR)

        else:
            import backend.our_train as ot
            ot.start_training()
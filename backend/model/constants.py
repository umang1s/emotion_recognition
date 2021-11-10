EMOTIONS=["angry","disgusted","fearful","happy","neutral","sad","surprised"]

CNN=0
OUR=1

CURRENT_DIR="F:/Project/python/emotion_recognition/"
OUR_WEIGHTS="data/weights/OUR_Weights.h5"
CNN_WEIGHTS="data/weights/CNN_Weights.h5"
CNN_JSON="data/weights/Cnn.json"
OUR_JSON="data/weights/Our.json"
TEST_DATA="F:/Project/python/emotion_recognition/data/test/"
TRAIN_DATA="F:/Project/python/emotion_recognition/data/train/"
RED=(0,0,255)
BLUE=(255,0,0)
GREEN=(0,255,0)
WHITE=(255,255,255)


class Box:
    def __init__(self,x,y,h,w):
        self.X=x 
        self.Y=y
        self.H=h
        self.W=w

    def minxy(self):
        return (self.X,self.Y)

    def maxxy(self):
        return (self.X+self.W,self.Y+self.H)

    def text(self):
        return (self.X,self.Y-10)

class Emotion:
    def __init__(self,name,value):
        self.Name=name
        self.Value=value

class HaarFile:
    dir="F:/Project/python/emotion_recognition/data/haarcascades/"
    HFA=dir+"haarcascade_frontalface_alt.xml"
    HFA2=dir+"haarcascade_frontalface_alt2.xml"
    HFAC=dir+"haarcascade_frontalface_alt_cuda.xml"
    HFA2C=dir+"haarcascade_frontalface_alt2_cuda.xml"
    HFD=dir+"haarcascade_frontalface_default.xml"
    HFDC=dir+"haarcascade_frontalface_default_cuda.xml"
    LBP=dir+"lbpcascade_frontalface.xml" 
    LBPI=dir+"lbpcascade_frontalface_improved.xml" 
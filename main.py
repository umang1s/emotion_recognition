from emotion_recognition import Emotion
import cv2
import time

TIMEOUT=-1
URL="0"
EMOTIONS=["angry","disgusted","fearful","happy","neutral","sad","surprised"] #don't update
TEST_WITH={3,4,6}
RED=(0,0,255)
BLUE=(255,0,0)
GREEN=(0,255,0)
WHITE=(255,255,255)
CURRENT_DIR="F:/Project/python/emotion_recognition/"


class HaarFile:
    dir=CURRENT_DIR+"data/haarcascades/"
    HFA=dir+"haarcascade_frontalface_alt.xml"
    HFA2=dir+"haarcascade_frontalface_alt2.xml"
    HFAC=dir+"haarcascade_frontalface_alt_cuda.xml"
    HFA2C=dir+"haarcascade_frontalface_alt2_cuda.xml"
    HFD=dir+"haarcascade_frontalface_default.xml"
    HFDC=dir+"haarcascade_frontalface_default_cuda.xml"
    LBP=dir+"lbpcascade_frontalface.xml" 
    LBPI=dir+"lbpcascade_frontalface_improved.xml" 





if __name__=="__main__":
    print("Starting ....")

    emotion=Emotion(TEST_WITH,haarfile=HaarFile.HFA)
    print("Opening Camera")
    stream = cv2.VideoCapture(0)
    if len(URL)>10:
        stream=cv2.VideoCapture(URL)
    older_time=time.time()
    p_time=older_time
    if TIMEOUT<0: TIMEOUT=90
    c_time=p_time
    fps=0
    while c_time- older_time<TIMEOUT:
        ret, frame=stream.read()
        if not ret: continue
        frame=cv2.flip(frame,1)
        datas=emotion.recognizeEmotion(frame)
        c_time=time.time()
        fps=1/(c_time-p_time)
        p_time=c_time
        for (x,y,h,w,emo_value,emo_name) in datas:
            cv2.rectangle(frame,(x,y),(x+w,y+h),GREEN,thickness=2)
            if(emo_value>0):
                cv2.putText(frame,emo_name+": %0.1f%c"%(emo_value,chr(37)),(x,y-10),cv2.FONT_HERSHEY_PLAIN,3,RED,2)
            if emo_value==-1:
                cv2.putText(frame,"...",(x,y-10),cv2.FONT_HERSHEY_PLAIN,3,RED,2)
        cv2.putText(frame,str(int(fps)),(10,70),cv2.FONT_HERSHEY_PLAIN,3,RED,2)
        cv2.imshow('Emotion Recongition',frame)
        if cv2.waitKey(5) == ord('q'):#wait until 'q' key is pressed
            break
    stream.release()
    cv2.destroyAllWindows

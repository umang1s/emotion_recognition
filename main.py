"""Main runnable file.

    OPERATION:  
    1:  Train Model  
    2:  Test From Camera
    3:  Test from image
    4:  Start API Server.
    5:  Start Client server.
"""  
OPERATION=3
TIMEOUT=-1
URL="http://192.168.0.177:4747/video?640x480"
from backend.emotion_recognition import Emotion
import backend.model.constants as cns
import cv2
import time

if __name__=="__main__":
    emotion=Emotion(cns.CNN,cns.HaarFile().HFD)
    if OPERATION==1:    #training
        print("\tStart Training...\n")
        emotion.train_model(40)

    elif emotion.load_model(): 
        if OPERATION==2:
            print("Opening Camera")
            stream = cv2.VideoCapture(0)
            older_time=time.time()
            p_time=older_time
            if TIMEOUT<0: TIMEOUT=30
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
                for (box,emo) in datas:
                    cv2.rectangle(frame,box.minxy(),box.maxxy(),cns.GREEN,thickness=2)
                    if(emo.Value>0):
                        cv2.putText(frame,emo.Name+": %0.1f%c"%(emo.Value,chr(37)),box.text(),cv2.FONT_HERSHEY_PLAIN,3,cns.RED,2)
                    elif emo.Value==-1:
                        cv2.putText(frame,emo.Name,box.text(),cv2.FONT_HERSHEY_PLAIN,3,cns.RED,2)
                cv2.putText(frame,str(int(fps)),(10,70),cv2.FONT_HERSHEY_PLAIN,3,cns.RED,2)
                cv2.imshow('Emotion Recongition',frame)
                if cv2.waitKey(5) == ord('q'):#wait until 'q' key is pressed
                    break
            stream.release()
            cv2.destroyAllWindows

        elif OPERATION==3:
            import os
            print("Start Testing")
            total_image=14
            current=0
            while current< total_image:
                c_time=time.time()
                current+=1
                img=cv2.imread("data/sample/0%d.jpg"%current)
                datas=emotion.recognizeEmotion(img)
                for (box,emo) in datas:
                    cv2.rectangle(img,box.minxy(),box.maxxy(),cns.GREEN,thickness=2)
                    if(emo.Value>0):
                        cv2.putText(img,emo.Name+": %0.1f %c"%(emo.Value,chr(37)),box.text(),cv2.FONT_HERSHEY_PLAIN,3,cns.RED,2)
                        if(emo.Name==cns.EMOTIONS[(current-1)%7]):
                            cv2.putText(img,"Right",(10,100),cv2.FONT_HERSHEY_PLAIN,2,cns.GREEN,2)
                        else:
                            cv2.putText(img,"Wrong",(10,100),cv2.FONT_HERSHEY_PLAIN,2,cns.RED,2)
                    elif emo.Value==-1:
                            cv2.putText(img,emo.Name,box.text(),cv2.FONT_HERSHEY_PLAIN,3,cns.RED,2)
                cv2.putText(img,"%0.2fs"%(time.time()-c_time),(5,40),cv2.FONT_HERSHEY_PLAIN,2,cns.RED,2)
                cv2.imshow("Emotion from image %d"%current,img)
                if cv2.waitKey(3000)==ord('q'):
                    break
                cv2.destroyAllWindows()


        elif OPERATION==4:
            print('Starting Server API')
            IP=""
            PORT=2000
            import backend.api.server as server
            server.start()

        else:
            print("Starting Client Server")
            import backend.api.client as client
            IP="3232"
            PORT=3230

            client.start(IP,PORT)

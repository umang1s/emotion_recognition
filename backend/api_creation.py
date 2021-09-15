import socket
import cv2
import pickle
import struct
import method as mt
import face_detection as fd


def start():
    ip=mt.GetIp()
    HOST,PORT=ip[0],5500
    print("Activating API on %s:%d"%(HOST,PORT))
    server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print("Socket Created...")
    server.bind((HOST,PORT))
    server.listen(1000) #number of request to handles
    print("Socket bind and listening created")

    connection,client_add=server.accept()
    print("Client connected : {}".format(client_add))
    data=b""

    payload_size=struct.calcsize(">L")
    print("payload size : {}".format(payload_size))

    server_connected=True
    while server_connected:
        cnt=0
        while len(data)<payload_size:
            if(len(data)==0) :
                cnt+=1
            if cnt>10:
                server_connected=False
                connection.close()
                server.close()
                break
            data+=connection.recv(4096)

            packed_msg_size= data[:payload_size]
            data=data[payload_size:]
            msg_size=struct.unpack(">L",packed_msg_size)[0]

            while len(data) <msg_size:
                data+=connection.recv(4096)

            frame_data=data[:msg_size]
            data=data[msg_size:]

            frame=pickle.loads(frame_data,fix_imports=True,encoding="bytes")
            frame=cv2.imdecode(frame,cv2.IMREAD_COLOR)

            emo_data=fd.getEmotionData(frame)
            connection.sendall(emo_data.encode())
            cv2.waitKey(1)
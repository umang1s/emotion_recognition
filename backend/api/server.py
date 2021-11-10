import socket
import api.process_message as pm
import cv2

def start(emotion_recogniser,max_connection,HOST,PORT,isVisible=False):
    """It Creates API which accept image and call Processdata.
    
        ProcessData should return response in form of List(ResponseData)
    """
    chunk_size=4096
    print("Activating API on %s:%d"%(HOST,PORT))
    send_server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    recv_server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    recv_server.bind((HOST,PORT))
    send_server.bind((HOST,PORT+1))
    recv_server.listen(1000) #number of request to handles
    send_server.listen(1000)

    recv_conn,recv_addr=recv_server.accept()
    send_conn,send_addr=send_server.accept()
    print("Client connected : {}".format(recv_addr))
    send_data=b''
    client_connected=True
    client_count=0
    while client_count<max_connection:
        if not client_connected:
            client_count+=1
            if(client_count==max_connection):
                print("Quota completed")   
                break
            recv_conn,recv_addr=recv_server.accept()
            send_conn,send_addr=send_server.accept()
            client_connected=True
            print("New(%d) Client connected : %s"%(client_count+1,recv_addr[0]))
        recv_msg_len=b''
        recv_msg_len=recv_conn.recv(chunk_size)
        if len(recv_msg_len)==0:
            client_connected=False 
            print("Error 1: Client Disconnected")
            send_conn.close()
            recv_conn.close()
        else:
            img_height=recv_msg_len[6:9]
            img_width=recv_msg_len[9:12]
            recv_data=recv_msg_len[12:]
            recv_msg_len=recv_msg_len[:6]
            msg_len=int(recv_msg_len.decode("utf-8"),16)
            msg_len*=2
            data_received=False
            while len(recv_data)<msg_len:
                data_received=False
                recv_byte_len=chunk_size
                diff_len=msg_len-len(recv_data)
                if recv_byte_len >diff_len:
                    recv_byte_len=diff_len
                new_data=recv_conn.recv(recv_byte_len)
                if len(new_data)==0:
                    client_connected=False 
                    print("Error 2: Client Disconnected")
                    send_conn.close()
                    recv_conn.close()
                    break
                else: 
                    recv_data+=new_data 
                    data_received=True
            
            if data_received:
                img=pm.convertInImage(recv_data,img_height,img_width)
                if isVisible:
                    cv2.imshow("Video",img)
                    cv2.waitKey(1)
                result=emotion_recogniser(img)
                l=len(result)
                if client_connected and l>0:
                    try:
                        send_conn.sendall(bytes(pm.encodeEmotionsInBytes(result),'utf-8'))
                    except:
                        print("Error 3: Client disconnected")
                        client_connected=False
                        send_conn.close()
                        recv_conn.close()
    send_conn.close()
    recv_conn.close()
    if isVisible:
        cv2.destroyAllWindows()
    return False

# def convertInResponse(self):
#         """Convert Emotion data to bytes for sending to client"""
#         name,accuracy=self.calculateAccuracy()
#         ret="%0.1f,%0.1f,%0.1f,%0.1f,%s,%s,%0.3f"%(self.PosX,self.PosY,self.Height,self.Width,name,self.ID,accuracy)
#         return ret

import socket
import api.method as mt
import api.process_message as pm

def start(emotion_recogniser,max_connection):
    """It Creates API which accept image and call Processdata.
    
        ProcessData should return response in form of List(ResponseData)
    """
    chunk_size=8192
    ip=mt.GetIp()
    HOST,PORT=ip[0],5500
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
        recv_msg_len=recv_conn.recv(10)
        if len(recv_msg_len)==0:
            client_connected=False 
            print("Error 1: Client Disconnected")
            send_conn.close()
            recv_conn.close()
        else:
            msg_len=int(recv_msg_len.decode("utf-8"))
            msg_len*=2
            recv_data=b''
            data_received=False
            while len(recv_data)<msg_len:
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
                recv_data+=new_data 
                data_received=True
            
            if data_received:
                result=emotion_recogniser(pm.convertInImage(recv_data))
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

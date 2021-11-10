import json
import cv2
import socket

def start(IP,PORT):
    """start client server"""
    send_con= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    recv_con=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    recv_con.connect((IP,PORT+1))
    send_con.connect((IP,PORT))
    #send_con = send_con.makefile('wb')
    cam = cv2.VideoCapture(0)
    encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 60]
    while True:
        ret, frame = cam.read()
        cv2.imshow("Client Camera",cv2.flip(frame,1))
        result, frame = cv2.imencode('.jpg', frame, encode_param)
        # data = pickle.dumps(frame, 0)
        # size = len(data)
        # send_con.sendall(struct.pack(">L", size) + data)
        # response=send_con.recv(4096)
        if cv2.waitKey(1) == ord('q'):
            break
    cv2.destroyAllWindows()
    send_con.close()
    cam.release()

def scan_qr_code():
    """Return ip and port from the qr_code.json file"""

    file_name="qr_code.json"
    if __name__=="__main__":
        file_name="F:\Project\python\emotion_recognition\\"+file_name
    with open(file_name,'r') as f:
        scan_data=json.load(f)
    return (scan_data['IP'],scan_data['PORT'])

if __name__=="__main__":
    ip,port=scan_qr_code()
    print(ip)
    #start(ip,port)    
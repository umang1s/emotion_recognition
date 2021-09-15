import cv2
import io
import socket
import struct
import time
import pickle
import zlib

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('192.168.89.78', 5500))
connection = client_socket.makefile('wb')

cam = cv2.VideoCapture(0)


encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 60]
total_frame=200
cnt=0
while cnt<total_frame:#True:
    ret, frame = cam.read()
    result, frame = cv2.imencode('.jpg', frame, encode_param)
    data = pickle.dumps(frame, 0)
    size = len(data)
    client_socket.sendall(struct.pack(">L", size) + data)
    response=client_socket.recv(4096)
    print(cnt)
    cnt+=1

cam.release()
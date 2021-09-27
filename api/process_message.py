def encodeEmotionsInBytes(recv_emotions):
    """Convertes Emotion data in bytes"""
    if len(recv_emotions)==0:
        return ""
    seprator="&"
    response_data=recv_emotions[0].convertInResponse()
    for j in range(1,len(recv_emotions)):
        response_data+=seprator+recv_emotions[j].convertInResponse()
    return response_data
    
def convertInImage(data):
    return data

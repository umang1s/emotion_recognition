class EmotionData:
    def __init__(self):
        self.Angry=0.0
        self.Happy=0.0
        self.Disgust=0.0
        self.Fear=0.0
        self.Sad=0.0
        self.Surprise=0.0
        self.Neutral=0.0
        self.ID=0
        self.Height=50
        self.Width=50
        self.PosX=20
        self.PosY=50


def ConvertEmotionDataToJsonFile(list_of_emotion_data):
    """takes list of emotion data and return json file"""
    l=list_of_emotion_data
    total_face=len(list_of_emotion_data)
    data='{"Face":'+str(total_face)+'\n'
    for i in range(total_face):
        data+="""\t
            "Face_%d":[
                "ID":"%d",
                "PosX":"%d",
                "PosY":"%d",
                "Height":"%d",
                "Width":"%d",
                "Angry":"%0.2f",
                "Happy":"%0.2f",
                "Disgust":"%0.2f",
                "Fear":"%0.2f",
                "Sad":"%0.2f",
                "Surprise":"%0.2f",
                "Neutral":"%0.2f",
            ]\n
        """%(i,l[i].ID,l[i].PosX,l[i].PosY,l[i].Height,l[i].Width,l[i].Angry,l[i].Happy,l[i].Disgust,l[i].Fear,l[i].Sad,l[i].Surprise,l[i].Neutral)
    data+='}'
    return data    

temp=[]
for j in range(2):
    temp.append(EmotionData())

ConvertEmotionDataToJsonFile(temp)



class EmotionData:
    def __init__(self):
        self.Angry=0.0
        self.Happy=0.0
        self.Disgust=0.0
        self.Fear=0.0
        self.Sad=0.0
        self.Surprise=0.2
        self.Neutral=0.8
        self.ID=0
        self.Height=50
        self.Width=50
        self.PosX=20
        self.PosY=50

    def calculateAccuracy(self):
        """Calculate accuracy and name"""
        data=[(self.Angry,"Angry"),(self.Happy,"Happy"),(self.Disgust,"Disgust"),(self.Fear,"Fear"),
        (self.Sad,"Sad"),(self.Surprise,"Surprise"),(self.Neutral,"Neutral")]

        data.sort()
        return data[6][1],data[6][0]

    def convertInResponse(self):
        """Convert Emotion data to bytes for sending to client"""
        name,accuracy=self.calculateAccuracy()
        ret="%0.1f,%0.1f,%0.1f,%0.1f,%s,%s,%0.3f"%(self.PosX,self.PosY,self.Height,self.Width,name,self.ID,accuracy)
        return ret
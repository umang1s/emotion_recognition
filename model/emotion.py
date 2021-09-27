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

    def calculateAccuracy(self):
        """Calculate accuracy and name"""
        return "angry",0.5

    def convertInResponse(self):
        import random
        self.PosX=random.randint(1,10)*self.PosX
        self.PosY=random.randint(1,10)*self.PosY
        self.Height=random.randint(1,4)*self.Height
        self.Width=random.randint(1,4)*self.Width
        name,accuracy=self.calculateAccuracy()
        ret="%0.1f,%0.1f,%0.1f,%0.1f,%s,%s,%0.3f"%(self.PosX,self.PosY,self.Height,self.Width,name,self.ID,accuracy)
        return ret
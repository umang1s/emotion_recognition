import model.emotion as em

def recogniseEmotion(img):
    temp=em.EmotionData()
    import random
    temp.PosX=random.randint(1,10)*temp.PosX
    temp.PosY=random.randint(1,10)*temp.PosY
    temp.Height=random.randint(1,4)*temp.Height
    temp.Width=random.randint(1,4)*temp.Width
    temp2=em.EmotionData()
    temp2.PosX=random.randint(1,10)*temp2.PosX
    temp2.PosY=random.randint(1,10)*temp2.PosY
    temp2.Height=random.randint(1,4)*temp2.Height
    temp2.Width=random.randint(1,4)*temp2.Width
    temp3=em.EmotionData()
    temp3.PosX=random.randint(1,10)*temp3.PosX
    temp3.PosY=random.randint(1,10)*temp3.PosY
    temp3.Height=random.randint(1,4)*temp3.Height
    temp3.Width=random.randint(1,4)*temp3.Width

    return [temp,temp2,temp3]
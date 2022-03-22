"""Run This file for training model.
"""  
import os
from tensorflow.python.keras.callbacks import ModelCheckpoint, ReduceLROnPlateau
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import cnn as cnn

EPOCHES=1
LEARNING_RATE=0.001
BATCH_SIZE=128
DATASET_DIR="C:/Users/Public/dataset/"
EMOTIONS=["angry","disgusted","fearful","happy","neutral","sad","surprised"] #don't update
TRAIN_WITH={0,1,2,3,4,5,6}




def ImageBuffer(dirname,img_size,batch_size):
    print(dirname)
    """Returns Image Buffer"""
    stream=ImageDataGenerator(
        rotation_range=40,
        brightness_range=(0.0,2.0),
        horizontal_flip=True
    )
    image_buffer=stream.flow_from_directory(
        dirname,target_size=(img_size,img_size),
        color_mode='grayscale',
        batch_size=batch_size,
        class_mode='categorical',
        shuffle=True
    )
    image_buffer=stream.flow_from_directory(
        dirname,target_size=(img_size,img_size),
        color_mode='grayscale',
        batch_size=batch_size,
        class_mode='categorical',
        shuffle=True
    )

    return image_buffer



############################################## Driver Code ###########################################

if __name__=="__main__":
    print("Start Training ...\n")
    
    if len(TRAIN_WITH)>7 or len(TRAIN_WITH)<2:
        print("Please fill correct data")
    else:
        name="Model"
        for i in TRAIN_WITH:
            name=name+str(i)
        JSON_FILE=name+".json"
        WEIGHT_FILE=name+".h5"

        
        for folderName in EMOTIONS:
            print(folderName+" : ",str(len(os.listdir(DATASET_DIR+'train/'+folderName))))

        train_buffer=ImageBuffer(DATASET_DIR+"train/",48,BATCH_SIZE)
        test_buffer=ImageBuffer(DATASET_DIR+"test/",48,BATCH_SIZE)

        
        checkPoint=ModelCheckpoint("data/"+WEIGHT_FILE,monitor='val_accuracy',save_weights_only=True,model='max',verbose=1)
        
        learning_rate=ReduceLROnPlateau(monitor='val_loss',factor=0.1,patience=2,min_lr=0.001,model='auto')
        model=cnn.CNN(7)

        callbacks=[checkPoint,learning_rate]
        history=model.fit(steps_per_epoch=train_buffer.n//train_buffer.batch_size,
            epochs=EPOCHES,
            x=train_buffer,
            validation_data=test_buffer,
            callbacks=callbacks,
        )

        model_json = model.to_json()
        with open("data/"+JSON_FILE,"w") as json_file:
            json_file.write(model_json)


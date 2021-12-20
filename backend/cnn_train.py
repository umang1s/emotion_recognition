import numpy as np
import pandas as pd
import os
from tensorflow.python.keras.callbacks import ModelCheckpoint, ReduceLROnPlateau
import backend.model.cnn as cnn
import backend.model.constants as cns
import backend.image_buffer as buffer
from numba import jit

def start_training(epoches,dataset_location):
    print("starts training")

    for folderName in cns.EMOTIONS:
        print(folderName+" : ",str(len(os.listdir(dataset_location+'data/train/'+folderName))))

    train_buffer=buffer.getBuffer(dataset_location+"/data/train/",48,32)
    test_buffer=buffer.getBuffer(dataset_location+"/data/test/",48,32)

    
    checkPoint=ModelCheckpoint(cns.CNN_WEIGHTS,monitor='val_accuracy',
        save_weights_only=True,model='max',verbose=1)
    
    learning_rate=ReduceLROnPlateau(monitor='val_loss',factor=0.1,patience=2,min_lr=0.0001,model='auto')

    model=cnn.Cnn()

    callbacks=[checkPoint,learning_rate]
    history=model.fit(steps_per_epoch=train_buffer.n//train_buffer.batch_size,
        epochs=epoches,
        x=train_buffer,
        validation_data=test_buffer,
        callbacks=callbacks
    )

    model_json = model.to_json()
    with open(cns.CNN_JSON,"w") as json_file:
        json_file.write(model_json)
    
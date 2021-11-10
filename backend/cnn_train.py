import numpy as np
import pandas as pd
import os
from tensorflow.python.keras.callbacks import ModelCheckpoint, ReduceLROnPlateau
from livelossplot.keras import PlotLossesCallback

def start_training(epoches,dataset_location):
    print("starts training")
    import backend.model.cnn as cnn
    import backend.model.constants as cns
    import backend.image_buffer as buffer

    for folderName in cns.EMOTIONS:
        print(folderName+" : ",str(len(os.listdir(dataset_location+'data/train/'+folderName))))

    train_buffer=buffer.getBuffer(dataset_location+"/data/train/",48,32)
    test_buffer=buffer.getBuffer(dataset_location+"/data/test/",48,32)

    
    checkPoint=ModelCheckpoint(cns.CNN_WEIGHTS,monitor='val_accuracy',
        save_weights_only=True,model='max',verbose=1)
    
    lr=ReduceLROnPlateau(monitor='val_loss',factor=0.1,patience=2,min_lr=0.00001,model='auto')

    model=cnn.Cnn()

    callbacks=[PlotLossesCallback(),checkPoint,lr]
    history=model.fit(steps_per_epoch=train_buffer.n//train_buffer.batch_size,
        epochs=epoches,
        x=train_buffer,
        validation_data=test_buffer,
        callbacks=callbacks
    )

    model_json = model.to_json()
    with open(cns.CNN_JSON,"w") as json_file:
        json_file.write(model_json)
    
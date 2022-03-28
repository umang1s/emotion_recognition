from  tensorflow.keras.models import Sequential
import tensorflow.keras.layers as tkl
import tensorflow.keras.optimizers as otm

#########################################   CNN Model   ###################################################
def CNN(output_layer):
    """Return CNN Model"""
    model = Sequential()
    # 1-conv
    model.add(tkl.Conv2D(64,(5,5),padding='same',input_shape = (48,48,1)))
    model.add(tkl.BatchNormalization())
    model.add(tkl.Activation('relu'))

    # 2-conv
    model.add(tkl.Conv2D(64,(5,5),padding='same'))
    model.add(tkl.BatchNormalization())
    model.add(tkl.Activation('relu'))
    model.add(tkl.MaxPooling2D(pool_size=(3,3)))
    model.add(tkl.Dropout(0.10))

    # # 3-conv
    model.add(tkl.Conv2D(128,(3,3),padding='same'))
    model.add(tkl.BatchNormalization())
    model.add(tkl.Activation('relu'))
    model.add(tkl.Dropout(0.10))

    # # 4-conv
    model.add(tkl.Conv2D(128,(3,3),padding='same'))
    model.add(tkl.BatchNormalization())
    model.add(tkl.Activation('relu'))
    model.add(tkl.MaxPooling2D(pool_size=(2,2)))
    model.add(tkl.Dropout(0.10))

    # # 5-conv
    model.add(tkl.Conv2D(256,(3,3),padding='same'))
    model.add(tkl.BatchNormalization())
    model.add(tkl.Activation('relu'))
    model.add(tkl.Dropout(0.10))

    # # 6-conv
    model.add(tkl.Conv2D(256,(3,3),padding='same'))
    model.add(tkl.BatchNormalization())
    model.add(tkl.Activation('relu'))
    model.add(tkl.MaxPooling2D(pool_size=(2,2)))
    model.add(tkl.Dropout(0.10))


    #flatten
    model.add(tkl.Flatten())

    model.add(tkl.Dense(256))
    model.add(tkl.BatchNormalization())
    model.add(tkl.Activation('relu'))
    model.add(tkl.Dropout(0.25))

    model.add(tkl.Dense(128))
    model.add(tkl.BatchNormalization())
    model.add(tkl.Activation('relu'))
    model.add(tkl.Dropout(0.25))

    #output layer
    model.add(tkl.Dense(output_layer,activation='sigmoid'))

    opt = otm.Adam(lr=0.0005)

    model.compile(optimizer=opt,loss='categorical_crossentropy',metrics=['accuracy'])
    model.summary()

    return model

from tensorflow.keras.preprocessing.image import ImageDataGenerator

def getBuffer(dirname,img_size,batch_size):

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

    return image_buffer
    
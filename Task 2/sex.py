import sys
import json
import keras
import tensorflow
import numpy as np
import os
from keras import layers
from keras import models
from keras import optimizers

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # Убираем ругань от ТФ

face = models.Sequential()
face.add(keras.layers.Conv2D(filters=32, kernel_size=(5, 5), activation='relu', input_shape=(150, 100, 3)))
face.add(keras.layers.MaxPooling2D((2, 2)))
face.add(keras.layers.Conv2D(filters=64, kernel_size=(3, 3), activation='relu'))
face.add(keras.layers.Conv2D(filters=64, kernel_size=(3, 3), activation='relu'))
face.add(keras.layers.MaxPooling2D(2, 2))
face.add(keras.layers.Conv2D(filters=128, kernel_size=(3, 3), activation='relu'))
face.add(keras.layers.MaxPooling2D(2, 2))
face.add(keras.layers.Flatten())
face.add(keras.layers.Dense(512, activation='relu'))
face.add(keras.layers.Dense(2, activation='softmax'))
face.compile(loss='categorical_crossentropy', optimizer=keras.optimizers.RMSprop(lr=1e-4, decay=1e-6), metrics=['acc'])
face.load_weights('/Users/vitalij/Downloads/sex.h5')

dict = {}


def faces(path):

    path = str(path)
    list = os.listdir(path)

    for i in range(len(list)):

        load_img = keras.preprocessing.image.load_img(path=os.path.join(path, list[i]), target_size=(150, 100, 3))
        array = keras.preprocessing.image.img_to_array(load_img) / 255
        img_array = np.expand_dims(array, axis=0)
        predictions = face.predict(img_array)

        if np.argmax(predictions[0]) == 1:
            dict[list[i]] = 'male'
        else:
            dict[list[i]] = 'female'
    jsonarray = json.dumps(dict)
    jsonarray = jsonarray.replace('\'' , '')

    with open('process_results.json', 'w') as outfile:
        json.dump(jsonarray, outfile)

    return 'Видел пример вывода, но не разобрался до конца, как избавиться от символа \ в json файле, хотя в jsonarray его нет. Почитал на форумах - говорят ничего страшного.'


print(faces(sys.argv[1]))

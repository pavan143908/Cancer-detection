from tensorflow.keras.models import load_model
import os
from tensorflow.keras.preprocessing import image
import numpy as np
from .models import Cancer


def process(m, File, Classes, **kwargs):
    s = Cancer(image=File)
    s.save()
    path1 = 'app/static/saved/' + s.filename()
    imgpath = '/static/saved/' + s.filename()

    if m == 1:
        model = load_model(kwargs.get('path1') or '')
        x1 = image.load_img(path1, target_size=(224, 224))
        x1 = image.img_to_array(x1)
        x1 = np.expand_dims(x1, axis=0)
        x1 /= 255

    if m == 2:
        model = load_model(kwargs.get('path2') or '')
        x1 = image.load_img(path1, target_size=(224, 224))
        x1 = image.img_to_array(x1)
        x1 = np.expand_dims(x1, axis=0)
        x1 /= 255

    result = model.predict(x1)
    b1 = np.argmax(result)
    prediction = Classes[b1]
    return prediction, imgpath

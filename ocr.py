import tensorflow as tf
from keras.backend import set_session
config = tf.compat.v1.ConfigProto()
config.gpu_options.allow_growth=True
config.log_device_placement = True
#tf.debugging.set_log_device_placement(True)

sess = tf.compat.v1.Session(config=config)
set_session(sess)
from tensorflow.keras.models import load_model
import csv
import cv2
import numpy as np

def itemsList():
    file_handle = open(r"metaDataCSV.csv", "r", encoding="utf-8-sig")
    csv_reader = csv.DictReader(file_handle)
    items = {}
    for row in csv_reader:
        items[int(row['Label'])]=row['Char Name']
    file_handle.close()
    return items
labelList = itemsList()

model = load_model('model/model_digit.h5')
def pred(thresh_img):
    thresh = cv2.resize(thresh_img, (28, 28), interpolation=cv2.INTER_CUBIC)
    thresh = thresh.astype("float32") / 255.0
    thresh = np.expand_dims(thresh, axis=-1)
    thresh = thresh.reshape(1, 28, 28, 1)
    pred = model.predict(thresh)
    label = pred.argmax(axis=-1)
    char = labelList[label[0]]
    return char

# img = cv2.imread('0.jpeg',0)
# print(pred(img))

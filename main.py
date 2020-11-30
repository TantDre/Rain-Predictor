# ---------------- Import ----------------
# Files
from preprocessing import getData
from postprocessing import plotData, printStats

# Libraries 
import numpy as np
import tensorflow as tf
from tensorflow import keras

# ---------------- Main ----------------
# Pre-processing of data
x, y, x_norm, y_bool = getData()

# Test
def simpel_model(y_new):
    x = np.array([0, 1, 2, 4, 6, 8, 10])
    y = np.array([0.50, 1.00, 1.50, 2.50, 3.50, 4.50, 5.50])
    model = tf.keras.Sequential([keras.layers.Dense(units = 1, input_shape = [1])])
    model.compile(optimizer = 'sgd', loss = 'mean_squared_error')
    model.fit(x, y, epochs= 100)
    return model.predict(y_new)[0]

prediction =simpel_model([7.0])
print(prediction)
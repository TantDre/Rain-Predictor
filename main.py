# ---------------- Import ----------------
# Files
from preprocessing import getData

# Libraries
import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np
import pandas as pd
import sys


# ---------------- Main ----------------
# Pre-processing of data
x, y = getData()

# Model
model = tf.keras.models.Sequential()

# Layers
model.add(tf.keras.layers.Dense(3, input_dim=3, activation='relu'))
model.add(tf.keras.layers.Dense(1, activation='sigmoid'))

# Complie
model.compile(loss='mean_squared_error',
              optimizer='adam',
              metrics=['binary_accuracy'])

# Train
history = model.fit(x, y, epochs=300, verbose=1)

# Results
loss_data = hist.history["loss"]
plt.plot(loss_data)
plt.title("Training Loss")
plt.show()

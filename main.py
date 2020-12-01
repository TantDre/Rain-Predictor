# ---------------- Import ----------------
from preprocessing import getData
import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np
import pandas as pd
import sys

# ---------------- Main ----------------
print("---------------- Regn-Prediktor ----------------")
print("Train \t (1)\nTest\t (2)")
menu = int(input())

if menu == 1:
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
    fitModel = model.fit(x, y, epochs=300, verbose=1)

    # Results
    loss_data = fitModel.history["loss"]
    plt.plot(loss_data)
    plt.title("Training Loss")
    plt.show()

    # Save model
    model.save("SimpelRainModel.h5")

elif menu == 2:
    # Load model
    model = tf.keras.models.load_model("SimpelRainModel.h5")

    # Values
    x, y = getData()

    # Results
    print(model.predict(x))

else:
    print("Error")

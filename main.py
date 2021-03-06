# ---------------- Import ----------------
from preprocessing import getData, boolRain
import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np
import pandas as pd
import sys

# ---------------- Main ----------------
print("---------------- Rain-Predictor ----------------")
print("Train \t (1)\nTest\t (2)\nUse\t (3)")
menu = int(input())

if menu == 1:
    # Pre-processing of data
    x, y = getData()

    # Model
    model = tf.keras.models.Sequential()

    # Layers
    model.add(tf.keras.layers.Dense(3, input_dim=3, activation='relu'))
    model.add(tf.keras.layers.Dense(3, activation='relu'))
    model.add(tf.keras.layers.Dense(1, activation='sigmoid'))

    # Complie
    model.compile(loss='mean_squared_error',
                  optimizer='adam',
                  metrics=['binary_accuracy'])

    # Train
    fitModel = model.fit(x, y, epochs=600, verbose=1)

    # Results
    loss_data = fitModel.history["loss"]
    plt.plot(loss_data)
    plt.title("Training Loss")
    plt.show()

    acc_data = fitModel.history["binary_accuracy"]
    plt.plot(acc_data)
    plt.title("Accuracy")
    plt.show()

    # Save model
    model.save("RainModel.h5")

elif menu == 2:
    # Load model
    model = tf.keras.models.load_model("RainModel.h5")

    # Test data
    x, y = getData()

    # Results
    pred = model.predict(x)

    # Plot
    plt.plot(y)
    plt.plot(boolRain(pred))
    plt.title("Rain Plot")
    plt.show()

elif menu == 3:
    # Load model
    model = tf.keras.models.load_model("RainModel.h5")

    # Test data
    print("Enter temperature (C): ")
    x1 = float(input())

    print("Enter humidity (%): ")
    x2 = float(input())

    print("Enter pressure (mmhg): ")
    x3 = float(input())

    # Normalize
    x1n = (x1 - (-11)) / (22 - (-11))
    x2n = (x2 - 18) / (79 - 18)
    x3n = (x3 - 733) / (788 - 733)

    # Formate
    x_vec = np.array(([x1n], [x2n], [x3n])).T

    # Results
    print("The probability of rain today is: ")
    print(str(round(model.predict(x_vec)[0][0]*100)) + " %")

else:
    print("Error")

# ---------------- Import ----------------
import numpy as np

# ---------------- Activation function ----------------
# Sigmoid
def Sigmoid(x):
  y = np.inv(1 + np.exp(-x))
  return y

# Relu
def Relu(x):
  y = np.maximum(0, x)
  return y

# ---------------- Cost function ----------------
# Mean Square Error
def MSE(yp, yt):
  c = np.mean((yt-yp)^2)
  return c

# Cross Entropy
def CE(yp, yt):
  c = np.mean(-yt * np.log(yp) - (1 - yt) * np.log(1 - yp))
  return c

# ---------------- Import ----------------
from preprocessing import DataPreProcessing
import matplotlib.pyplot as plt
import numpy as np
#import tensorflow as tf

# ---------------- Main ----------------

# Data
x = DataPreProcessing()

# Print
print("The mean temperature is: ")
print(np.mean(x))

# Plot
plt.title('Temperature')
plt.plot(x)
plt.show()
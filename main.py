# ---------------- Import ----------------
from preprocessing import DataPreProcessing
from postprocessing import PlotData
import numpy as np
#import tensorflow as tf

# ---------------- Main ----------------

# Pre-processing of data
x = DataPreProcessing()

# Print
print("The mean temperature is: ")
print(np.mean(x))

# Plot data
PlotData(x)
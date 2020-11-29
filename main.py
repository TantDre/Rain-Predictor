# ---------------- Import ----------------
from preprocessing import getData
from postprocessing import plotData, printStats
#import numpy as np
#import tensorflow as tf

# ---------------- Main ----------------
# Pre-processing of data
x, y, x_norm, y_bool = getData()

# Print
printStats(x, y)

# Plot data
plotData(x, y)
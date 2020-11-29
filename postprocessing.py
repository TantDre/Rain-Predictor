# ---------------- Import ----------------
import matplotlib.pyplot as plt
import numpy as np

# ---------------- plotData(x, y) ----------------
# Plot data
def plotData(x, y):
  # Plot
  plt.title('Rain - Temperature')
  plt.plot(x, y, '.')
  plt.show()

# ---------------- printStats(x, y) ----------------
# Print stats 
def printStats(x, y):
  # Print
  print("The mean temperature is: " + str(round(np.mean(x))))
  print("The total amount of rain is: " + str(round(np.sum(x))))

  # Rain calc
  counter = 0
  for days in y:
    if days > 1:
      counter += 1
  print("It rains " + str(round((counter/np.size(y))*100)) + "% of the days.")
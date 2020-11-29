# ---------------- Import ----------------
import numpy as np
import csv

# ---------------- getData() ----------------
# Return the pre-processed data
def getData():
  # Get data
  x, y = DataPreProcessing()

  # Normalize data
  x_norm = normalizeData(x)
  
  # Return
  return x_norm, y

# ---------------- DataPreProcessing() ----------------
# Reads and reduces the raw data
def DataPreProcessing():
  # Variables
  TimeVec = []
  TempVec = []
  HumiVec = []
  PresVec = []
  WindSpeVec = []
  WindDirVec = []
  RainVec = []

  # Read csv
  with open('Data/Data_2017_2018.csv', newline='') as csvfile:
    dataFile = csv.DictReader(csvfile, delimiter='\t')

    # Loop file
    for row in dataFile:
      TimeVec.append(row['Time'])
      TempVec.append(float(row['Outdoor Temperature(°C)']))
      HumiVec.append(float(row['Outdoor Humidity(%)']))
      PresVec.append(float(row['Absolute Pressure(mmHg)']))
      WindSpeVec.append(float(row['Wind Speed(m/s)']))
      WindDirVec.append(row['Wind Direction'])
      RainVec.append(float(row['24 Hour Rainfall(mm)']))

  # Variables
  day = int(TimeVec[0][9:11])
  indexStart = 0
  indexStop = 0

  TimeVecRed = []
  TempVecRed = []
  HumiVecRed = []
  PresVecRed = []
  WindSpeVecRed = []
  RainVecRed = []

  # Reduce data to days
  for row in TimeVec:
    if day != int(row[9:11]):
      day = int(row[9:11])
      TimeVecRed.append(day)
      TempVecRed.append(np.mean(TempVec[indexStart:indexStop]))
      HumiVecRed.append(np.mean(HumiVec[indexStart:indexStop]))
      PresVecRed.append(np.mean(PresVec[indexStart:indexStop]))
      WindSpeVecRed.append(np.mean(WindSpeVec[indexStart:indexStop]))
      RainVecRed.append(np.sum(RainVec[indexStart:indexStop]))
      indexStart = indexStop 
    
    else:
      indexStop += 1

  # Return
  return TempVecRed, RainVecRed

# ---------------- normalizeData(X) ----------------
# Normalizes the data
def normalizeData(x):
  # Variables
  x_min = min(x)
  x_max = max(x)

  # Normalize
  x_norm = (x - x_min) / (x_max - x_min)

  # Return
  return x_norm
# ---------------- Import ----------------
import numpy as np
import csv

def DataPreProcessing():
  # ---------------- Variables ----------------
  TimeVec = []
  TempVec = []
  HumiVec = []
  PresVec = []
  WindSpeVec = []
  WindDirVec = []

  # ---------------- Read csv ----------------
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

  # ---------------- Operations ----------------

  # Test
  return(np.mean(TempVec))
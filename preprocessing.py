# ---------------- Import ----------------
import csv

# Return the pre-processed data
def getData():
  x, y = DataPreProcessing()
  return x, y

# Reads and collects the raw data
def DataPreProcessing():
  # ---------------- Variables ----------------
  TimeVec = []
  TempVec = []
  HumiVec = []
  PresVec = []
  WindSpeVec = []
  WindDirVec = []
  RainVec = []

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
      RainVec.append(float(row['24 Hour Rainfall(mm)']))

  # ---------------- Reduce data ----------------

  # Return
  return TempVec, RainVec
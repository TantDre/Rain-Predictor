# ---------------- Import ----------------
import numpy as np
import csv

# ---------------- getData() ----------------
# Return the pre-processed data


def getData():
    # Get data
    x1, x2, x3, y = DataPreProcessing()

    # Normalize data
    x1_norm = normalizeData(x1)
    x2_norm = normalizeData(x2)
    x3_norm = normalizeData(x3)

    # Convert true value
    y_bool = boolRain(y)

    # Format arrays
    y_vec = np.array(y_bool, "float32")
    x1_vec = np.array(x1_norm, "float32")
    x2_vec = np.array(x2_norm, "float32")
    x3_vec = np.array(x3_norm, "float32")
    x_vec = np.stack((x1_vec, x2_vec, x3_vec), axis=0).T

    # Return
    return x_vec, y_vec

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
            TempVec.append(float(row['Outdoor Temperature(C)']))
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
    RainVecRed = []

    # Reduce data to days
    for row in TimeVec:
        if day != int(row[9:11]):
            day = int(row[9:11])
            TimeVecRed.append(day)
            TempVecRed.append(np.mean(TempVec[indexStart:indexStop]))
            HumiVecRed.append(np.mean(HumiVec[indexStart:indexStop]))
            PresVecRed.append(np.mean(PresVec[indexStart:indexStop]))
            RainVecRed.append(np.sum(RainVec[indexStart:indexStop]))
            indexStart = indexStop

        else:
            indexStop += 1

    # Return
    return TempVecRed, HumiVecRed, PresVecRed, RainVecRed

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

# ---------------- boolRain(x) ----------------
# Converts mm rain to true or false


def boolRain(y):
    # Variables
    rainLimit = 2
    y_bool = []

    # Convert
    for days in y:
        if days > rainLimit:
            y_bool.append(1)
        else:
            y_bool.append(0)

    # Return
    return y_bool

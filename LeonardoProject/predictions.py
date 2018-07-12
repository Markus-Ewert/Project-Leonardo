import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas import Series
import seaborn as sns
import datetime as dt
import time
from sklearn.svm import SVC
import math
from sklearn import preprocessing
from sklearn.externals import joblib


def prepareData(path):
    # Insert to into a data frame
    df_june_raw = pd.read_csv(path, index_col=False,
                              names=["id", "machineID", "measureTime", "voltage", "current", "activePower",
                                     "apparentPower", "reactivePower", "powerFactor"])
    df_june_raw = df_june_raw.iloc[1:]

    # Format to correct data types
    df_june_raw["machineID"] = pd.to_numeric(df_june_raw["machineID"])
    df_june_raw["measureTime"] = pd.to_datetime(df_june_raw["measureTime"])
    df_june_raw["voltage"] = pd.to_numeric(df_june_raw["voltage"])
    df_june_raw["current"] = pd.to_numeric(df_june_raw["current"])
    df_june_raw["activePower"] = pd.to_numeric(df_june_raw["activePower"])
    df_june_raw["apparentPower"] = pd.to_numeric(df_june_raw["apparentPower"])
    df_june_raw["reactivePower"] = pd.to_numeric(df_june_raw["reactivePower"])
    df_june_raw["powerFactor"] = pd.to_numeric(df_june_raw["powerFactor"])

    june_test = df_june_raw.copy()

    june_test.drop("measureTime", axis=1, inplace=True)
    june_test.drop("id", axis=1, inplace=True)

    return june_test


def predict_svm():
    # load model
    clf = joblib.load('/Users/markus/PycharmProjects/LeonardoProject/media/LeonardoProject/files/svm.pkl')

    # data preparation
    test_df = prepareData("/Users/markus/PycharmProjects/LeonardoProject/media/LeonardoProject/files/svm.csv")

    # create new data set for actual prediction
    test = test_df.copy()
    test.drop("machineID", axis=1, inplace=True)

    # prediction
    prediction = clf.predict(test)

    labels = np.unique(prediction)

    machines = test_df.machineID.unique()

    machinePredicitons = []

    for _ in machines:
        machinePredicitons.append([])

    # estimate machines
    for i, el in enumerate(prediction):
        for j in range(0, len(machinePredicitons)):

            if machines[j] == test_df.machineID.values[i]:
                machinePredicitons[j].append(el)

    maxCounter = 0

    finalpredictions = []
    for _ in machines:
        finalpredictions.append([])

    for i, el in enumerate(machinePredicitons):
        for label in labels:

            mCounter = machinePredicitons[i].count(label)

            if maxCounter < mCounter:
                maxCounter = mCounter
                finalpredictions[i] = label

    result = {
        'machines': machines,
        'classes': finalpredictions,
        'range': range(0, len(machines))
    }

    return result


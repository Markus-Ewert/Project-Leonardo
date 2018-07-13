from __future__ import print_function, division
from sklearn.svm import SVC
from sklearn import preprocessing
import pandas as pd
from sklearn.externals import joblib
import os
from LeonardoProject.settings import BASE_DIR


def prepareData(path):
    # Insert to into a data frame
    df_raw = pd.read_csv(path, index_col=False,
                              names=["id", "machineID", "measureTime", "voltage", "current", "activePower",
                                     "apparentPower", "reactivePower", "powerFactor"])

    df_raw = df_raw.iloc[1:]

    # Format to correct data types
    df_raw["measureTime"] = pd.to_datetime(df_raw["measureTime"])
    df_raw["voltage"] = pd.to_numeric(df_raw["voltage"])
    df_raw["current"] = pd.to_numeric(df_raw["current"])
    df_raw["activePower"] = pd.to_numeric(df_raw["activePower"])
    df_raw["apparentPower"] = pd.to_numeric(df_raw["apparentPower"])
    df_raw["reactivePower"] = pd.to_numeric(df_raw["reactivePower"])
    df_raw["powerFactor"] = pd.to_numeric(df_raw["powerFactor"])

    X = df_raw.copy()

    X.drop("measureTime", axis=1, inplace=True)
    X.drop("id", axis=1, inplace=True)

    return X


def train_svm():
    file_path = os.path.join(BASE_DIR, 'media/LeonardoProject/files/svm_train.csv')

    df = prepareData(file_path)

    # get sample of training data to randomize input -> will lead to better results
    df_training = df

    # Set labels
    y = df_training['machineID']
    # Set training data
    X = df_training.drop('machineID', axis=1)

    X_scaled = preprocessing.scale(X)

    # Train model
    svclassifier = SVC(kernel='rbf', verbose=True)
    svclassifier.fit(X, y)

    # Save model
    model_path = os.path.join(BASE_DIR, 'media/LeonardoProject/files/svm.pkl')
    joblib.dump(svclassifier, model_path)

    return True


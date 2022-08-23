import random
import pandas as pd
import pylab as pl
import numpy as np
import scipy.optimize as opt
from sklearn import preprocessing
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.svm import SVC
import matplotlib.pyplot as plt
from module.dataset import dataset

class dataclean:
    def dataclean():
        df = dataset.dataset()
        print(df['BPM'].value_counts())
        print(df['RHR'].value_counts())
        print(df['steps'].value_counts())
        print(df['Target'].value_counts())
        print(df['RMSSD'].value_counts())
        print(df.isnull().sum())
        print(df.duplicated().sum())
        df['steps'].fillna((0), inplace=True)
        df['RMSSD'].fillna((df['RMSSD'].mean()), inplace=True)
        df['RHR'].fillna((df['RHR'].mean()), inplace=True)
        df['BPM'].fillna((df['RMSSD'].mean()), inplace=True)
        df['Target'].fillna((0), inplace=True)
        print(df.isnull().sum())
        print(df.duplicated().sum())
        print(df.dtypes)
        df = df.astype({
            'BPM': int,
            'steps': int,
            'Target': int
        })
        fig = plt.figure(figsize =(10, 7))
        plt.pie(df['Target'].value_counts(), labels = ["sehat","sakit"])
        plt.show()
        print(df['Target'].value_counts())
        df.to_csv('hasil.csv')
        return df
        
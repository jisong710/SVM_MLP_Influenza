import pandas as pd
import pylab as pl
import numpy as np
import scipy.optimize as opt
from sklearn import preprocessing
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.svm import SVC
import matplotlib.pyplot as plt

class dataclean:
    def dataclean():
        df = pd.read_csv('hasil.csv')
        print(df['BPM'].value_counts())
        print(df['RHR'].value_counts())
        print(df['steps'].value_counts())
        print(df['Target'].value_counts())
        print(df['RMSSD'].value_counts())
        
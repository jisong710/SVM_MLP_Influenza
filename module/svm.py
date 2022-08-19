import pandas as pd
import pylab as pl
import numpy as np
import scipy.optimize as opt
from sklearn import preprocessing
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.svm import SVC
import matplotlib.pyplot as plt

class svm:
    def svm():
        df1 = pd.read_csv("HR PASIEN 1.csv", sep=';')
        df2 = pd.read_csv("HRV PASIEN 1.csv", sep=';')
        df3 = pd.read_csv("RHR PASIEN 1.csv", sep=';')
        df4 = pd.read_csv("STEPS PASIEN 1.csv", sep=';')
        print(df1.head())
        df1.dtypes
        df1['DateTime'] = pd.to_datetime(df1['DateTime'])
        df1

        df1.head(40)
        df1.set_index('DateTime', inplace=True)
        df1

        df2['DateTime'] = pd.to_datetime(df2['DateTime'])
        df2

        df2.dtypes
        df2.head(40)
        df2.set_index('DateTime', inplace=True)
        df2
        
        df3.dtypes
        df3['DateTime'] = pd.to_datetime(df3['DateTime'])
        df3

        df3.head(40)

        df3.set_index('DateTime', inplace=True)
        df3

        df4.dtypes
        df4['DateTime'] = pd.to_datetime(df4['DateTime'])
        df4

        df4.head(40)

        df4.set_index('DateTime', inplace=True)
        df4
        df1['steps'] = df4['Value']
        df1['RMSSD'] = df2['RMSSD']
        df1['RHR'] = df3['RHR']
        print(df1.head())
        df1 = df1.astype({
            'BPM': int,
            'steps': int,
            'Target': int
        })
        feature_df = df1[['bpm', 'steps']]
        x = np.asarray(feature_df)
        x[0:50]

        df1['target'] = df1['target'].astype('int')
        y = np.asarray(df1['target'])
        y[:50] , y[len(y)-50:]

        x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2, random_state=2)
        print('Train set:', x_train.shape, y_train.shape)
        print('Test set:', x_test.shape, y_test.shape)

        df1.bpm.value_counts()

svm1 = svm
svm1.svm()
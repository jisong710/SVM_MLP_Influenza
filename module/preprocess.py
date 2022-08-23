import pandas as pd
import pylab as pl
import numpy as np
import scipy.optimize as opt
from sklearn import preprocessing
import seaborn as sn
import matplotlib.pyplot as plt
from module.dataclean import dataclean

class preproces:
    def preproces():
        df = dataclean.dataclean()
        normalize = preprocessing.MinMaxScaler()
        df= pd.DataFrame(normalize.fit_transform(df.values), columns=df.columns, index=df.index)
        print(df.skew(axis=0))
        sn.boxplot(data = df['BPM'])
        sn.boxplot(data = df['RHR'])
        sn.boxplot(data = df['RMSSD'])
        sn.boxplot(data = df['steps'])
        plt.hist(df['BPM'])
        plt.hist(df['RHR'])
        plt.hist(df['RMSSD'])
        plt.hist(df['steps'])
        df['steps']= np.where(df['steps']<df['steps'].quantile(0.10),df['steps'].quantile(0.10),df['steps'])
        df['RMSSD']= np.where(df['RMSSD']>df['RMSSD'].quantile(0.90),df['RMSSD'].quantile(0.90),df['RMSSD'])
        df['RMSSD']= np.where(df['RMSSD']<df['RMSSD'].quantile(0.10),df['RMSSD'].quantile(0.10),df['RMSSD'])
        df['steps']= np.where(df['steps']>df['steps'].quantile(0.90),df['steps'].quantile(0.90),df['steps'])
        print(df.skew(axis=0))
        return df
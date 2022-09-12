from random import randint
import matplotlib.pyplot as plt
from module.dataset2 import dataset
import pandas as pd

class dataclean:
    def dataclean(self):
        df = pd.read_csv('subjek2.csv', sep = ';')
        print(df['BPM'].value_counts())
        print(df['RHR'].value_counts())
        print(df['steps'].value_counts())
        print(df['Target'].value_counts())
        print(df.isnull().sum())
        print(df.duplicated().sum())
        df['steps'].fillna((df['steps'].median()), inplace=True)
        df['RHR'].fillna((df['RHR'].median()), inplace=True)
        df['BPM'].fillna((df['BPM'].median()), inplace=True)
        df['Target'].fillna(1, inplace=True)
        print(df.isnull().sum())
        print(df.duplicated().sum())
        df.drop_duplicates(inplace=True)
        print(df.dtypes)
        df = df.astype({
            'BPM': int,
            'steps': int,
            'RHR': int,
            'Target': int
        })
        print(df['Target'].value_counts())
        df.to_csv('hasil2.csv')
        return df
        

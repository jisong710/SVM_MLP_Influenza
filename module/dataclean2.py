from random import randint
import matplotlib.pyplot as plt
from module.dataset2 import dataset

class dataclean:
    def dataclean(self):
        df = dataset().dataset()
        print(df['BPM'].value_counts())
        print(df['RHR'].value_counts())
        print(df['steps'].value_counts())
        print(df['Target'].value_counts())
        print(df.isnull().sum())
        print(df.duplicated().sum())
        df['steps'].fillna((df['steps'].mean()), inplace=True)
        df['RHR'].fillna((df['RHR'].mean()), inplace=True)
        df['BPM'].fillna((df['BPM'].mean()), inplace=True)
        df.dropna(subset=['Target'],inplace=True)
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
        
import matplotlib.pyplot as plt
from module.dataset import dataset

class dataclean:
    def dataclean(self):
        df = dataset().dataset()
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
        df['BPM'].fillna((df['BPM'].mean()), inplace=True)
        df['Target'].fillna((0), inplace=True)
        print(df.isnull().sum())
        print(df.duplicated().sum())
        print(df.dtypes)
        df = df.astype({
            'BPM': int,
            'steps': int,
            'RHR': int,
            'Target': int
        })
        plt.figure(figsize =(10, 7))
        plt.pie(df['Target'].value_counts(), labels = ["sehat","sakit"])
        print(df['Target'].value_counts())
        df.to_csv('hasil1.csv')
        return df
        
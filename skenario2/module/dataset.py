import pandas as pd

class dataset:
    def dataset(self,):

        df1 = pd.read_csv("HR PASIEN 1.csv", sep=';')
        df2 = pd.read_csv("HRV PASIEN 1.csv", sep=';')
        df3 = pd.read_csv("RHR PASIEN 1.csv", sep=';')
        df4 = pd.read_csv("STEPS PASIEN 1.csv", sep=';')
        print(df1.head())
        df1.dtypes
        df1['DateTime'] = pd.to_datetime(df1['DateTime'])
        df1

        df1.head(40)
        df1

        df2['DateTime'] = pd.to_datetime(df2['DateTime'])
        df2

        df2.dtypes
        df2.head(40)
        df2
        
        df3.dtypes
        df3['DateTime'] = pd.to_datetime(df3['DateTime'])
        df3

        df3.head(40)
        df3
        print(df4.dtypes)
        df4['DateTime'] = pd.to_datetime(df4['DateTime'])
        df4
        df4.head(40)
        df4
        df1['RMSSD'] = df2['RMSSD']
        df1['RHR'] = df3['RHR']
        df1['steps'] = df4['steps']
        df1.set_index('DateTime', inplace=True)
        print(df1.head())
        return df1
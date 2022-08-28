import pandas as pd
import pylab as pl
import numpy as np
import scipy.optimize as opt
from sklearn import preprocessing
import seaborn as sn
import matplotlib.pyplot as plt
from module.dataclean import dataclean

class preproces:
    def preproces(self):
        df = dataclean().dataclean()
        normalize = preprocessing.MinMaxScaler()
        df= pd.DataFrame(normalize.fit_transform(df.values), columns=df.columns, index=df.index)
        return df
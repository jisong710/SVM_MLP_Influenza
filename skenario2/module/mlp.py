# -*- coding: utf-8 -*-
"""TA_MULTILAYERPERCEPTRON_PASIEN_1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Ge27vPx2Lqap0GNJVNj-vVSuAH0oCqT8
"""

from io import StringIO
from random import randint
import random
import matplotlib
matplotlib.use('Agg')
from sklearn.datasets import load_iris
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pandas as pd
from sklearn.metrics import plot_confusion_matrix
import matplotlib.pyplot as plt
import numpy as np
from module.preprocess import preproces
class mlp:
  def mlp(self, inputDetakJantung):
    dfdetak = pd.read_csv(StringIO(inputDetakJantung), sep=',',header=None)
    seriesDetakJantung = dfdetak.transpose()
    seriesDetakJantung = seriesDetakJantung.mean()
    print(seriesDetakJantung)
    DetakJantung =  seriesDetakJantung.loc[0]
    kumpulandata = pd.read_csv("hasil1.csv")
    hasildata = kumpulandata.loc[kumpulandata['BPM'] == DetakJantung]
    kumpulandata['Target'].value_counts().plot(kind='bar',figsize=(14,8),title="deteksi detak jantung dengan penderita")
    plt.show()
    print(hasildata.head())
    dss = preproces().preproces()
    dss

    X = dss[['BPM','RHR','steps']]
    X = np.asarray(X)
    X

    y = dss['Target']
    y = np.asarray(y)
    y

    X_train, X_test, y_train, y_test = train_test_split(X, y,random_state=123, test_size=0.3)
    print('Train set:', X_train.shape, y_train.shape)
    print('Test set:', X_test.shape, y_test.shape)

    y[:100]

    """#MULTI LAYER-PERCEPTRON#"""

    clf = MLPClassifier(hidden_layer_sizes=(256,128,64,32),activation="relu",random_state=1, verbose=1).fit(X_train, y_train)
    y_pred=clf.predict(X_test)
    print(clf.score(X_test, y_test))

    from sklearn.metrics import classification_report, confusion_matrix
    import itertools

    def plot_confusion_matrix(cm, classes,
                              normalize=True,
                              title='Confusion matrix',
                              cmap=plt.cm.Blues):
        """
        This function prints and plots the confusion matrix.
        Normalization can be applied by setting `normalize=True`.
        """
        if normalize:
            cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
            print("Normalized confusion matrix")
        else:
            print('Confusion matrix, without normalization')

        print(cm)

        plt.imshow(cm, interpolation='nearest', cmap=cmap)
        plt.title(title)
        plt.colorbar()
        tick_marks = np.arange(len(classes))
        plt.xticks(tick_marks, classes, rotation=45)
        plt.yticks(tick_marks, classes)

        fmt = '.2f' if normalize else 'd'
        thresh = cm.max() / 2.
        for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
            plt.text(j, i, format(cm[i, j], fmt),
                    horizontalalignment="center",
                    color="white" if cm[i, j] > thresh else "black")

        plt.tight_layout()
        plt.ylabel('True label')
        plt.xlabel('Predicted label')

    # Compute confusion matrix
    cnf_matrix = confusion_matrix(y_test, y_pred)
    pred_from_train = clf.predict(X_train)
    cnf_matrix_training_data = confusion_matrix(y_train, pred_from_train)

    np.set_printoptions(precision=2)

    print (classification_report(y_test, y_pred))

    # Plot non-normalized confusion matrix
    plt.figure()
    plot_confusion_matrix(cnf_matrix, classes=['Sehat','Influenza'],normalize= True,  title='Confusion matrix')
    plt.savefig("static/img/mlp.png", format='png')
    # plot_confusion_matrix(cnf_matrix_training_data, classes=['Sehat','Influenza'],normalize= False,  title='Confusion matrix')

    print('jumlah Target testing yang influenza',len(list(filter(lambda x : x == 1, y_test))))
    print('jumlah hasil pred. data testing yang influenza',len(list(filter(lambda x : x == 1, y_pred))))

    print('jumlah hasil pred. semua dataset yang influenza',len(list(filter(lambda x : clf.predict([x]) == 1, X))))
    print('jumlah hasil pred. semua dataset yang sehat',len(list(filter(lambda x : clf.predict([x]) == 0, X))))
    print('kombinasi BPM steps yang influenza', list(filter(lambda x : clf.predict([x]) == 1, X_test)))
    return classification_report(y_test, y_pred,output_dict=True),clf.predict([[int(DetakJantung)/100,random.random(),random.random()]])
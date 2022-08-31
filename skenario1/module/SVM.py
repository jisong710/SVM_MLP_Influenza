# -*- coding: utf-8 -*-
"""SVM_FIKS.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1P3nTfARzZ5cHAKHpZQDSQDOUzmojNKCm
"""

# Commented out IPython magic to ensure Python compatibility.
from random import randint
import random
import pandas as pd
import pylab as pl
import numpy as np
import scipy.optimize as opt
from sklearn import preprocessing
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.svm import SVC
from module.preprocess import preproces
import matplotlib
matplotlib.use('Agg')
# %matplotlib inline 
import matplotlib.pyplot as plt
from module.dataclean import dataclean
#panjang array
class svm:
    def svm(self, inputDetakJantung):
        dfdetak = pd.read_csv(inputDetakJantung, sep=',')
        seriesDetakJantung = dfdetak.mean()
        print(seriesDetakJantung)
        DetakJantung =  seriesDetakJantung.loc['BPM']
        kumpulandata = pd.read_csv("hasil1.csv")
        hasildata = kumpulandata.loc[kumpulandata['BPM'] == DetakJantung] 
        print(kumpulandata.head())
        kumpulandata['Target'].value_counts().plot(kind='bar',figsize=(10,5),title="deteksi detak jantung dengan penderita")
        plt.show()  
        df = dataclean().dataclean()
        feature_df = df[['BPM','RHR','steps']]
        x = np.asarray(feature_df)
        x[0:50]

        df['Target'] = df['Target'].astype('int')
        y = np.asarray(df['Target'])
        y[:50] , y[len(y)-50:]

        x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.3, random_state=123)
        print('Train set:', x_train.shape, y_train.shape)
        print('Test set:', x_test.shape, y_test.shape)

        df.BPM.value_counts()

        """SVM"""

        from sklearn import svm
        #GridSearch
        tuned_parameters = [
            {"kernel": ["rbf"], "gamma": [1e-3, 1e-4, 1e-5], "C": [1, 10, 100, 1000]}
        ]

        clf = GridSearchCV(svm.SVC(), tuned_parameters, refit = True, verbose = 3)
        # clf = svm.SVC(kernel='poly', gamma='auto')
        clf.fit(x_train, y_train) 
        #PENGARUH KERNEL JUGA BISA dan parameter svm yang mempengaruhi

        clf.best_params_
        #cari  tau arti kernel,gamaa, c

        yhat = clf.predict(x_test)
        yhat[0:5]

        from sklearn.metrics import classification_report, confusion_matrix
        import itertools

        def plot_confusion_matrix(cm, classes,
                                normalize=False,
                                title='Confusion matrix',
                                cmap=plt.cm.Blues):
            """
            This function prints and plots the confusion matrix.
            Normalization can be applied by setting `normalize=True`.
            """
            if normalize:
                cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
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
        cnf_matrix = confusion_matrix(y, yhat)
        pred_from_train = clf.predict(x_train)
        cnf_matrix_training_data = confusion_matrix(y_train, pred_from_train)

        np.set_printoptions(precision=2)
        report = classification_report(y_test, yhat)
        print (report)

        # Plot non-normalized confusion matrix
        plt.figure()
        plot_confusion_matrix(cnf_matrix, classes=['Sehat','Influenza'],normalize= False,  title='Confusion matrix')
        # plot_confusion_matrix(cnf_matrix_training_data, classes=['Sehat','Influenza'],normalize= False,  title='Confusion matrix')
        plt.savefig("static/img/svm.png", format='png')
        from sklearn.metrics import f1_score
        f1_score(y_test, yhat, average='weighted')

        # clf.predict([[59,0],[61,0]])
        y_pred = clf.predict(x_train)
        max(y_pred)
        list(filter(lambda x : clf.predict([x]) == 1,x_train))
        # clf.predict([[89, 45]])
        # df1[df1['steps']>40]

        import seaborn as sns
        plt.figure(figsize=(10, 8))
        # Plotting our two-features-space
        sns.scatterplot(x=x_train[:, 0], 
                        y=x_train[:, 1], 
                        hue=y_train, 
                        s=8);
        # Constructing a hyperplane using a formula.
        best_model = clf.best_estimator_
        w = best_model.coef0           # w consists of 2 elements
        b = best_model.intercept_      # b consists of 1 element
        x_points = np.linspace(-1, 1)    # generating x-points from -1 to 1
        y_points = np.linspace(-1, 1)  # getting corresponding y-points
        # Plotting a red hyperplane
        plt.plot(x_points, y_points, c='r');
        # Encircle support vectors
        plt.scatter(best_model.support_vectors_[:, 0],
                    best_model.support_vectors_[:, 1], 
                    s=50, 
                    facecolors='none', 
                    edgecolors='k', 
                    alpha=.5);
        # Step 2 (unit-vector):
        w_hat = best_model.coef0 / (np.sqrt(np.sum(best_model.coef0 ** 2)))
        # Step 3 (margin):
        margin = 1 / np.sqrt(np.sum(best_model.coef0 ** 2))
        # Step 4 (calculate points of the margin lines):
        decision_boundary_points = np.array(list(zip(x_points, y_points)))
        points_of_line_above = decision_boundary_points + w_hat * margin
        points_of_line_below = decision_boundary_points - w_hat * margin
        # Plot margin lines
        # Blue margin line above
        plt.plot(points_of_line_above[:, 0], 
                points_of_line_above[:, 1], 
                'b--', 
                linewidth=2)
        # Green margin line below
        plt.plot(points_of_line_below[:, 0], 
                points_of_line_below[:, 1], 
                'g--',
                linewidth=2)
        hasildeteksi =[]
        jumlahdetak = dfdetak.shape
        for i in range(jumlahdetak[0]):
            hasildeteksi.append(clf.predict([[int(dfdetak['BPM'][i])/100,random.random(),random.random()]]))
        meandeteksi = pd.Series(hasildeteksi).mean()
        hasilsehasilhasilnya = meandeteksi[0]
        return classification_report(y_test, yhat,output_dict=True),hasilsehasilhasilnya
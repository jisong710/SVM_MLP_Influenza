from flask import Flask, render_template, request
import pandas as pd
from module.mlp import mlp
from module.MLP2 import mlp2
from module.SVM import svm
from module.SVM2 import svm2


app = Flask(__name__)
algoritmasvm = svm()
algoritmasvm2 = svm2()
algoritmamlp = mlp()
algoritmamlp2 = mlp2()
@app.route('/',methods = ['POST', 'GET'])
def index():
    return render_template('index.html')

@app.route('/akun',methods = ['POST', 'GET'])
def akun():
    return render_template('akun.html')

@app.route('/Pasien1',methods = ['POST', 'GET'])
def pasien1():
    df = pd.read_csv('hasil1.csv', nrows=1000)
    return render_template('pasien1.html', tables=[df.to_html(classes='data')], titles=df.columns.values)

@app.route('/Pasien2',methods = ['POST', 'GET'])
def pasien2():
    df = pd.read_csv('hasil2.csv', nrows=1000)
    return render_template('pasien2.html', tables=[df.to_html(classes='data')], titles=df.columns.values)

@app.route('/MLP',methods = ['POST', 'GET'])
def hMLP():
    data = []
    report = []
    if(request.method == "POST"):
        if(request.form['pasien'] == "1"):
            data,report = algoritmamlp.mlp(request.form['BPM'])
        else:
            data,report = algoritmamlp2.mlp2(request.form['BPM'])
        length = len(data)
        return render_template('halamanFullMLP.html',data=data ,length = length, report = report)
    length = len(data)
    return render_template('MLP.html',data=data ,length = length, report = report)

@app.route('/SVM',methods = ['POST', 'GET'])
def hsvm():
    data = []
    report = []
    if(request.method == "POST"):
        if(request.form['pasien'] == "1"):
            data,report = algoritmasvm.svm(request.form['BPM'])
        else:
            data,report = algoritmasvm2.svm2(request.form['BPM'])
        length = len(data)
        return render_template('halamanFullSVM.html',data=data ,length = length, report = report)
    length = len(data)
    return render_template('SVM.html',data=data ,length = length, report = report)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
 

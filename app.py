from flask import Flask, render_template, request
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
    return render_template('halamanUtama.html')
@app.route('/mlp',methods = ['POST', 'GET'])
def hmlp():
    if(request.method == "POST"):
        if(request.form['pasien'] == "1"):
            report,data = algoritmamlp.mlp()
        else:
            report,data = algoritmamlp2.mlp2()
    else:
        data = []
        report = []
    length = len(data)
    return render_template('MLP.html',data = data ,length = length, report = report)
@app.route('/svm',methods = ['POST', 'GET'])
def hsvm():
    if(request.method == "POST"):
        if(request.form['pasien'] == "1"):
            report,data = algoritmasvm.svm()
        else:
            report,data = algoritmasvm2.svm2()
    else:
        data = []
        report = []
    length = len(data)
    return render_template('SVM.html',data = data ,length = length, report = report)
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
 

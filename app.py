from flask import Flask, render_template, request
from module.MLP1 import mlp1
from module.MLP2 import mlp2
from module.SVM import svm

app = Flask(__name__)
algoritmalstm = svm()
algoritmasvr = mlp1()
algoritmasvr = mlp2()
@app.route('/',methods = ['POST', 'GET'])
def index():
    return render_template('halamanUtama.html')
@app.route('/mlp',methods = ['POST', 'GET'])
def hmlp():
    return render_template('MLP.html')
@app.route('/svm',methods = ['POST', 'GET'])
def hsvm():
    return render_template('SVM.html')
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
 

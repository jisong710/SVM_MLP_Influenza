from crypt import methods
from flask import Flask, render_template, request
from module.mlp import mlp
from module.MLP2 import mlp2
from module.SVM import svm

app = Flask(__name__)
algoritmalstm = svm()
algoritmasvr = mlp()
algoritmasvr = mlp2()
@app.route('/',methods = ['POST', 'GET'])
def index():
    return render_template('halamanUtama.html')
@app.route('/mlp',methods = ['POST', 'GET'])
def hmlp():
    if(request.method == "POST"):

    else:
        
    return render_template('MLP.html')
@app.route('/svm',methods = ['POST', 'GET'])
def hsvm():
    if(request.method == "POST"):
        
    else:

    return render_template('SVM.html')
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
 

from flask import Flask, render_template, request
from module.MLP1
from module.MLP2
from module.SVM

app = Flask(__name__)
algoritmalstm = SVM()
algoritmasvr = MLP1()
algoritmasvr = MLP2()
@app.route('/',methods = ['POST', 'GET'])
def index():
    return render_template('halamanUtama.html')

@app.route('/information',methods = ['POST', 'GET'])
def information():
    return render_template('informasialgoritma.html')
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
 
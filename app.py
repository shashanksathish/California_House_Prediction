import numpy as np
from flask import Flask, request, render_template
from gevent.pywsgi import WSGIServer
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def index():
    return render_template('info.html')

@app.route('/index')
def page():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [float(x) for x in request.form.values()]
    final_features = np.array([np.array(int_features)])
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)

    return render_template('end.html', prediction_text='The Cost of your House is $ {}'.format(output))


if __name__ == "__main__":
  http_server = WSGIServer(('', 5000), app)
  http_server.serve_forever()
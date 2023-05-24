from flask import Flask, request, render_template
import pickle
import numpy as np
import webbrowser as wb
from threading import Timer

app = Flask(__name__)

model1 = pickle.load(open('model.pkl','rb'))

model = ''

@app.route('/')
def init():
    return render_template('car_predict.html')

@app.route('/select_model', methods=['POST','GET'])
def select_model():
    global model 
    model = request.form.get('model', '')

    # DEBUG
    print(model)
    # DEBUG

    return render_template('car_predict.html', model = model)

@app.route('/predict1', methods=['POST','GET'])
def predict1():
    global model

    try:
        int_features=[int(x) for x in request.form.values()]
    except:
        return render_template('car_predict.html', pred = 'Invalid Input.', model = model)

    final=[np.array(int_features)]
    
    # DEBUG
    print(model)
    print(int_features)
    print(final)
    # DEBUG

    prediction=model1.predict_proba(final)
    output = '{0:.{1}f}'.format(prediction[0][1], 2)

    if output > str(0.5):
        return render_template('car_predict.html', pred = 'You are getting scammed. Predicted price is {}.'.format(output), model = model)
    else:
        return render_template('car_predict.html', pred = 'Your are not getting scammed. Predicted is {}.'.format(output), model = model)
    
@app.route('/predict2', methods=['POST','GET'])
def predict2():
    global model

    try:
        int_features=[int(x) for x in request.form.values()]
    except:
        return render_template('car_predict.html', pred = 'Invalid Input.', model = model)

    final=[np.array(int_features)]
    
    # DEBUG
    print(model)
    print(int_features)
    print(final)
    # DEBUG

    prediction=model1.predict_proba(final)
    output = '{0:.{1}f}'.format(prediction[0][1], 2)

    if output > str(0.5):
        return render_template('car_predict.html', pred = 'You are getting scammed. Predicted price is {}.'.format(output), model = model)
    else:
        return render_template('car_predict.html', pred = 'Your are not getting scammed. Predicted is {}.'.format(output), model = model)

if __name__ == '__main__':
    Timer(1, wb.open_new("http:localhost:5000/")).start()
    app.run(debug=False)
    # app.run(debug=True)

from flask import Flask, request, url_for, redirect, render_template
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open('model.pkl','rb'))

@app.route('/')
def start():
    return render_template("car_price.html")

@app.route('/predict', methods=['POST','GET'])
def predict():
    try:
        int_features=[int(x) for x in request.form.values()]
    except:
        return render_template('car_price.html', pred = 'Invalid Input.')

    final=[np.array(int_features)]
    
    # DEBUG
    print(int_features)
    print(final)
    # DEBUG

    prediction=model.predict_proba(final)
    output = '{0:.{1}f}'.format(prediction[0][1], 2)

    if output > str(0.5):
        return render_template('car_price.html', pred = 'You are getting scammed. Predicted price is {}.'.format(output))
    else:
        return render_template('car_price.html', pred = 'Your are not getting scammed. Predicted is {}.'.format(output))

if __name__ == '__main__':
    app.run(debug=True)

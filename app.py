from flask import Flask, request, render_template
import pickle
import numpy as np
import webbrowser as wb
from threading import Timer

app = Flask(__name__)

model4 = pickle.load(open('models/Classification_MLP.pkl','rb'))

model = ''

@app.route('/')
def init():
    return render_template('car_predict.html')

@app.route('/select_model', methods=['POST','GET'])
def select_model():
    global model 
    model = request.form.get('model', '')
    print(model)

    return render_template('car_predict.html', model = model)

@app.route('/predict1', methods=['POST','GET'])
def predict1():
    global model
    print(model)

    
    
@app.route('/predict2', methods=['POST','GET'])
def predict2():
    global model
    print(model)

    age = request.form.get("Age")
    sell_price = request.form.get("Selling Price")
    kms = request.form.get("Kms Driven")
    fuel = request.form.get("Fuel Type")
    seller_type = request.form.get("Seller Type")
    transmission = request.form.get("Transmission Type")

    if model == "4":
        age = (int(age) - 3) / 31
        sell_price = (int(sell_price) - 20000) / 8900000
        kms = (int(kms) - 1) / 806599
        fuel_Diesel = 1 if fuel.lower() == "diesel" else 0
        fuel_Other = 1 if fuel.lower() == "other" else 0
        fuel_Petrol = 1 if fuel.lower() == "petrol" else 0
        seller_type_Dealer = 1 if seller_type.lower() == "dealer" else 0
        seller_type_Individual = 1 if seller_type.lower() == "individual" else 0
        seller_type_Trustmark_Dealer = 1 if seller_type.lower() == "trustmark dealer" else 0
        transmission_Automatic = 1 if transmission.lower() == "automatic" else 0
        transmission_Manual = 1 if transmission.lower() == "manual" else 0

        input_to_model4 = np.array([[age, sell_price, kms, fuel_Diesel, fuel_Other, fuel_Petrol, seller_type_Dealer, seller_type_Individual, seller_type_Trustmark_Dealer, transmission_Automatic, transmission_Manual]])

        prediction_probs = model4.predict_proba(input_to_model4)

        print(prediction_probs)
        
        return render_template('car_predict.html', pred = 'Predicted Number of Previous Owners is {0}.\n Prediction Probabilities are {1}.'.format(prediction_probs.argmax() + 1, prediction_probs), model = model)

if __name__ == '__main__':
    Timer(1, wb.open_new("http:localhost:5000/")).start()
    app.run(debug=False)
    # app.run(debug=True)

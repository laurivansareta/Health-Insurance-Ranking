import datetime
import pickle
import pandas as pd
import os
from flask import Flask, request, Response
from healthinsurance import HealthInsurance as hi

print(os.getcwd())

# Carragando modelo
model = pickle.load(open('models/model_linear_regression.pkl', 'rb'))

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/status', methods=['GET'])
def status():
    return Response('Api HealthInsurance - Status Online {}'.format(datetime.datetime.today()), status=200, mimetype='application/json')

@app.route('/predict', methods=['POST'])
def health_insurance_predict():   
    test_json = request.get_json()

    if not test_json:
        return Response('{}', status=200, mimetype='application/json')

    if isinstance(test_json, dict):
        teste_raw = pd.DataFrame(test_json, index=[0])
    else:
        teste_raw = pd.DataFrame(test_json, columns=test_json[0].keys())

    pipeline = hi.HealthInsurance()
    df = pipeline.data_cleaning(teste_raw)
    df = pipeline.feature_engineering(df)
    df = pipeline.data_preparation(df)

    return pipeline.get_prediction(model, teste_raw, df)

if __name__ == '__main__':
    # Heroku
    # port = os.environ.get('PORT', 5000)
    # app.run('0.0.0.0', port=port)
    # Local
    app.run('0.0.0.0', debug=True)
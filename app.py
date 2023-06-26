from flask import Flask, request, Response
from model import Model

app = Flask(__name__)

model = Model('ml/randomForest.pkl')


@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    arr = []
    try:
        data.keys()
        arr.append(data['EDA_mean'])
        arr.append(data['EDA_std'])
        arr.append(data['EDA_min'])
        arr.append(data['EDA_max'])

        arr.append(data['EDA_phasic_mean'])
        arr.append(data['EDA_phasic_std'])
        arr.append(data['EDA_phasic_min'])
        arr.append(data['EDA_phasic_max'])

        arr.append(data['EDA_tonic_mean'])
        arr.append(data['EDA_tonic_std'])
        arr.append(data['EDA_tonic_min'])
        arr.append(data['EDA_tonic_max'])

        arr.append(data['TEMP_mean'])
        arr.append(data['TEMP_std'])
        arr.append(data['TEMP_min'])
        arr.append(data['TEMP_max'])
        arr.append(data['TEMP_slope'])

        arr.append(data['age'])
        arr.append(data['height'])
        arr.append(data['weight'])
        arr.append(data['coffee_today_YES'])
        arr.append(data['sport_today_YES'])
        arr.append(data['feel_ill_today_YES'])
        arr.append(data['gender'])
        arr.append(data['smoker'])

    except:
        return Response("Invalid Data!!")

    return model.predict(data)


if __name__ == '__main__':
    app.run(debug=True)

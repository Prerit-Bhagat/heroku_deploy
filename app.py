from flask import Flask,request,jsonify # type: ignore
import pickle
import numpy as np # type: ignore

with open('clf5.pkl','rb') as file:
    model=pickle.load(file)

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'


@app.route('/predict',methods=['GET','POST'])
def predict():
    snoring_range=request.form.get('snoring_range')
    respiration_rate=request.form.get('respiration_range')
    temprature=request.form.get('temprature')
    blood_oxygen=request.form.get('blood_oxygen')
    sleep=request.form.get('sleep')
    heart_rate=request.form.get('heart_rate')
    # result={'snoring_range':snoring_range,'respiration_rate':respiration_rate,'temp=':temprature,'sleep':sleep,'heart_rate':heart_rate}
    input_query=np.array([[snoring_range,respiration_rate,temprature,blood_oxygen,sleep,heart_rate]])
    # print(input_query)
    result=model.predict(input_query)
    
    # return "HElo"
    return jsonify({'Stress level :':str(result)})
    # return jsonify({'Result':str(result)})
'''
snoring range
respiration rate
body temperature
limb movement
blood oxygen
eye movement
hours of sleep
heart rate
Stress Levels
'''
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
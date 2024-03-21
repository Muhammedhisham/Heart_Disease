from flask import Flask, request, render_template
import pickle

# Load the trained model
with open(r'C:\Users\hisha\Desktop\Python\Heart\model.pkl', 'rb') as f:
    model = pickle.load(f)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        Age=float(request.form['Age'])
        Sex=float(request.form['Sex'])
        ChestPainType=float(request.form['ChestPainType'])
        RestingBP=float(request.form['RestingBP'])
        Cholesterol=float(request.form['Cholesterol'])
        FastingBS=float(request.form['FastingBS'])
        RestingECG=float(request.form['RestingECG'])
        MaxHR=float(request.form['MaxHR'])
        ExerciseAngina=float(request.form['ExerciseAngina'])
        Oldpeak=float(request.form['Oldpeak'])
        ST_Slope=float(request.form['ST_Slope'])
        k=[Age, Sex, ChestPainType, RestingBP, Cholesterol, FastingBS,RestingECG,MaxHR,ExerciseAngina,Oldpeak,ST_Slope]
        # Make prediction
        prediction=model.predict([[Age, Sex, ChestPainType, RestingBP, Cholesterol, FastingBS,RestingECG,MaxHR,ExerciseAngina,Oldpeak,ST_Slope]])
        print('prediction###################', k)
        
        prediction=int(prediction[0])
        print('prediction=', prediction)
        output=''
        if prediction==0:
            output='Y'
        else:
            output='N'
        return render_template('index.html', prediction=output)

if __name__ == '__main__':
    app.run(debug=True, port=5002)

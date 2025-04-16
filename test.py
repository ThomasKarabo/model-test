from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

# Load your model
with open(r'C:\Users\Thomas.Mohlapo\OneDrive - 9475042 - Tshela Health Care\Documents\ML Model Deploy Code\Credit Modelling\model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    
    if request.method == 'POST':
        # Get all form data
        data = {
            'person_age': int(request.form['person_age']),
            'person_income': int(request.form['person_income']),
            'person_home_ownership': request.form['person_home_ownership'],
            'person_emp_length': float(request.form['person_emp_length']),
            'loan_intent': request.form['loan_intent'],
            'loan_grade': request.form['loan_grade'],
            'loan_amnt': int(request.form['loan_amnt']),
            'loan_int_rate': float(request.form['loan_int_rate']),
            'loan_percent_income': float(request.form['loan_percent_income']),
            'cb_person_default_on_file': request.form['cb_person_default_on_file'],
            'cb_person_cred_hist_length': int(request.form['cb_person_cred_hist_length'])
        }
        
        # Convert to DataFrame
        input_df = pd.DataFrame([data])
        
        # Make prediction
        prediction = model.predict(input_df)
    
    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

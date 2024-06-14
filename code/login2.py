from flask import Blueprint, render_template, request
import pandas as pd
login2 = Blueprint('login2', __name__)

def login(name, og_password):
    csv_file = 'data.csv'
    df = pd.read_csv(csv_file)
    result = df[df['firstname'] == name]

    if not result.empty:
        password2 = result['password'].values[0]
        if password2 == og_password:
            print('Login successful') 
        else:
            print('Login failed')                                              
    else:
        print(f"No record found for {name}.")

@login2.route('/login2', methods=['GET', 'POST'])
def index():
    name = request.form.get('name')
    passw = request.form.get('pass')
    # Call the function with the ID you want to fetch
    login(name,passw)
    
    return render_template('login2.html')
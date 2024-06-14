from flask import Blueprint, render_template, request
import pandas as pd

signup2 = Blueprint('signup2', __name__)

def store_data(firstname,lastname,number,email,password):
    data = [{'firstname': firstname, 'lastname': lastname, 'number': number, 'email' : email, 'password': password}]
    new_df = pd.DataFrame(data)
    csv_file = 'data.csv'
    new_df.to_csv(csv_file, mode='a', header=False, index=False)

@signup2.route('/signup2', methods=['GET', 'POST'])
def index():
    firstname = request.form.get('first_name')
    lastname = request.form.get('last_name')
    number = request.form.get('number')
    email = request.form.get('email')
    password = str(request.form.get('UserPassword'))
    re_password = request.form.get('confirm_password')
    print('password is',password)
    if password != re_password:
        print("password dosen't match")
    elif len(password) <= 7:
        print('ERROR: PAsswrod should be grater than or equal to 8 letters')
    else:
        store_data(firstname,lastname,number,email,password)
    return render_template('signup2.html')

from flask import Flask, request, render_template
import mysql.connector

app = Flask(__name__)

# Database configuration
db_config = {
    'user': 'root',
    'password': 'password',
    'host': 'localhost',
    'database': 'donor_managment_2'
}

# Route for serving the donor registration form
@app.route('/')
def donor_registration_form():
    return render_template('donor_registration_form.html')

# Route for handling individual donor registration
@app.route('/register/donor', methods=['POST'])
def register_donor():
    full_name = request.form.get('full_name')
    phone_number = request.form.get('phone_number')
    email = request.form.get('email')
    address = request.form.get('address')
    pan_card_number = request.form.get('pan_card_number')
    password_hash = 'default_hash'  # Set a default or generate a hash for the password

    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO users (full_name, phone_number, email, address, pan_card_number, password_hash) VALUES (%s, %s, %s, %s, %s, %s)",
        (full_name, phone_number, email, address, pan_card_number, password_hash)
    )
    connection.commit()
    cursor.close()
    connection.close()

    return 'Individual donor registered successfully!'

# Route for handling company donor registration
@app.route('/register/company', methods=['POST'])
def register_company():
    company_name = request.form.get('company_name')
    contact_person = request.form.get('contact_person')
    phone_number = request.form.get('phone_number_company')
    email = request.form.get('email_company')
    address = request.form.get('address_company')
    company_pan_card = request.form.get('pan_card_number_company')
    password_hash = 'default_hash'  # Set a default or generate a hash for the password

    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO users (company_name, contact_person, phone_number, email, address, company_pan_card, password_hash) VALUES (%s, %s, %s, %s, %s, %s, %s)",
        (company_name, contact_person, phone_number, email, address, company_pan_card, password_hash)
    )
    connection.commit()
    cursor.close()
    connection.close()

    return 'Company donor registered successfully!'

if __name__ == '__main__':
    app.run(debug=True)

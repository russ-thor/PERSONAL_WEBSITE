from flask import Flask
from flask import render_template
from flask import request
from flask import url_for
import sqlite3
import datetime
from email.message import EmailMessage
import os
import smtplib

app = Flask(__name__)


# f(x) to add a new contact-us record to an SQLite3 table in our database
def add_one(date_sent, name, email, company, user_msg):
    conn = sqlite3.connect('contact_page_messages.db')  # create a db connection
    c = conn.cursor()  # create a cursor

    c.execute("INSERT INTO form_response VALUES (?,?,?,?,?)", (date_sent, name, email, company, user_msg))

    conn.commit()  # Commit the command
    conn.close()  # Close our connection

# Webpage routing
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/services')
def about():
    return render_template('services.html', title='services')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html', title='portfolio')

@app.route('/publications')
def publications():
    return render_template('publications.html', title='publications')

@app.route('/contact')
def contact():
    return render_template('contact.html', title='contact')

# Contact-us form routing
@app.route('/form', methods=['POST'])
def form():
    with open('security.txt') as f:
    # with open('/home/russthor/security_texts/security.txt') as f:  # direct link for servers
        lines = f.readlines()
        personal_email = lines[0]
        personal_password = lines[1]

    # variables taken from form submission
    name = request.form.get('name')
    email = request.form.get('email')
    company = request.form.get('company')
    message = request.form.get('message')

    # if form not completed, alert user with an error statement (keep partially completed data)
    if not name or not email or not company or not message:
        error_statement = '***  All Form Fields Required  ***'
        return render_template('contact.html',
                               error_statement=error_statement,
                               name=name,
                               email=email,
                               company=company,
                               message=message)

    # compose email with contact form details - send to my email
    msg=EmailMessage()
    msg.set_content('from: ' + email + '\n'*3 + message)
    msg['Subject'] = 'Website Form Msg from: ' + company
    msg['From'] = email
    msg['To'] = personal_email

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(personal_email, personal_password)
    server.send_message(msg)
    server.quit()

    # also insert the contact form details into an SQLite3 table in a database
    today = datetime.date.today()
    add_one(today, name, email, company, message)

    # return a thank you for submission page
    return render_template('form.html',
                           title='Thank you!',
                           name=name,
                           email=email,
                           company=company,
                           message=message)


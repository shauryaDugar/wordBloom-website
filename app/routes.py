from flask import render_template, request, flash
from flask_mail import Message
from app import app, mail
from dotenv import load_dotenv
import os
from threading import Thread

load_dotenv()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

# @app.route('/contact', methods=['GET', 'POST'])
# def contact():
#     if(request.method=='POST'):
#         name=request.form['name']
#         email=request.form['email']
#         phone=request.form['phone']
#         subject=request.form['subject']
#         message=request.form['message']
#         msg = Message('New enquiry from ' + name + ' - ' + subject,
#                       sender='wordbloomjpr@gmail.com',
#                         recipients=['wordbloomjpr@gmail.com'])
#         msg.body = f'{email} \n {phone} \n {message}' 
#         mail.send(msg)
#         send_email_confirmation(name, email, subject, message)
#         flash("Thank you for your enquiry. We will get back to you as soon as possible. Please check your email for a copy of your enquiry.")
#     return render_template('contact.html', title='Contact')
    

def send_email_confirmation(name, email, subject, message):
    msg = Message('Thank you for your enquiry',
                  sender='kashconails@gmail.com',
                  recipients=[email])
    msg.body = f'Hi {name}, \n\nThank you for your enquiry with Word Bloom. \n\nHere is a copy of your query: {subject}\n{message}\n\nWe will get back to you as soon as possible. \n\nKind regards, \nWord Bloom'
    mail.send(msg)


if __name__ == '__main__':
    app.run(debug=True)
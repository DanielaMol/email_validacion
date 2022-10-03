from dataclasses import dataclass
from email_app.models.email import Email
from email_app import app
from flask import render_template, redirect, request, session 


@app.route('/')
def raiz():
    return render_template("index.html")
    #*! En lugar de devolver una cadena, 
    #*! devolveremos el resultado del método render_template
    #*!pasando el nombre de nuestro archivo HTML


@app.route('/process', methods=['POST'])
def enviar():
    print(request.form)
    if not Email.validate_email(request.form):
        return redirect ('/')
    data = {
        "email": request.form['email'],
    }
    Email.save(data)
    return redirect('/success')

@app.route('/success')
def resultado():
    emails = Email.get_all()
    return render_template("success.html", todos_emails=emails)

@app.route('/clearsession')
def limpiar_session():
    session.clear()
    return redirect('/')
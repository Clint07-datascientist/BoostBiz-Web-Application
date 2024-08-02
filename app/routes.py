from flask import render_template, redirect, url_for, request
from app import app
from app.forms import LoginForm, RegisterForm

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Handle login logic here
        return redirect(url_for('index'))
    return render_template('loginregister.html', form=form, form_type='login')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        # Handle registration logic here
        return redirect(url_for('index'))
    return render_template('loginregister.html', form=form, form_type='register')

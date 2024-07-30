from flask import Flask, render_template, request, redirect, url_for, flash
from app import app, db
from app.models import User, Business

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    # Example data to pass to the template
    data = {
        'financial_health': 'Good',
        'recommendations': ['Reduce expenses', 'Increase marketing efforts']
    }
    return render_template('dashboard.html', data=data)

@app.route('/assessments', methods=['GET', 'POST'])
def assessments():
    if request.method == 'POST':
        # Handle form submission
        business_name = request.form['business_name']
        # Process the assessment data
        flash(f'Assessment for {business_name} submitted successfully!', 'success')
        return redirect(url_for('dashboard'))
    return render_template('assessments.html')

@app.route('/mentorship')
def mentorship():
    mentors = [
        {'name': 'John Doe', 'expertise': 'Financial Planning'},
        {'name': 'Jane Smith', 'expertise': 'Investment Strategies'}
    ]
    return render_template('mentorship.html', mentors=mentors)

@app.route('/partners')
def partners():
    partners = [
        {'name': 'Bank A', 'services': 'Loans, Credit'},
        {'name': 'Gov Agency B', 'services': 'Grants, Subsidies'}
    ]
    return render_template('partners.html', partners=partners)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Authenticate user
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password', 'danger')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Register new user
        new_user = User(username=username)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        flash('Registration successful!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)


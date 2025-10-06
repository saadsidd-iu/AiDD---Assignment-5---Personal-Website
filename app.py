from flask import Flask, render_template, request, redirect, url_for, flash
import re

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Change this to a random secret key

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/resume')
def resume():
    return render_template('resume.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Get form data
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        # Basic validation
        errors = []
        
        if not first_name:
            errors.append('First name is required')
        elif len(first_name) < 2:
            errors.append('First name must be at least 2 characters long')
            
        if not last_name:
            errors.append('Last name is required')
        elif len(last_name) < 2:
            errors.append('Last name must be at least 2 characters long')
            
        if not email:
            errors.append('Email is required')
        elif not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
            errors.append('Please enter a valid email address')
            
        if not message:
            errors.append('Message is required')
        elif len(message) < 10:
            errors.append('Message must be at least 10 characters long')
        elif len(message) > 1000:
            errors.append('Message must be less than 1000 characters')
        
        if errors:
            for error in errors:
                flash(error, 'error')
            return render_template('contact.html')
        else:
            # Form is valid, redirect to thank you page
            return redirect(url_for('thank_you'))
    
    return render_template('contact.html')

@app.route('/thankyou')
def thank_you():
    return render_template('thankyou.html')

if __name__ == '__main__':
    app.run(debug=True)

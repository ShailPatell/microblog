from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'username':
            'Shail'}
    posts = [

        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!!!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts = posts)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    #Call the Login Form class from the forms.py file.
    form = LoginForm()

    #form.validate_on_submit will run if u have a csfr token in the html file
    #validate_on_submit() will process the form.
    #When the browser sends a GET request to page with the form, the method is going to return False
    #So in that case it skips the if statement and just renders the template.
    if form.validate_on_submit():
        #If form.validate_on_submit returns true, it calls the flash function.
        #The flash function is a useful way to show messages to the user.
        #It is used as a technique to let the user know if an action has been successful or not.

        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        #Redirect() instructs the web browser to automatically redirect the user to the index page of the application.
        return redirect(url_for('index'))
    #If the forms are empty it will just return the Login page again.
    return render_template('login.html', title = 'Sign In', form = form)



from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy
import sqlite3



app = Flask(__name__)

@app.route('/')
def base():
    return render_template('baseTemplateFlask.html')

@app.route('/home')
def home():
    return render_template('homePageFlask.html')

@app.route('/gallery')
def gallery():
    return render_template('galleryPageFlask.html')

@app.route('/rates')
def rates():
    return render_template('ratesPageFlask.html')

@app.route('/contact')
def contact():
    return render_template('contactPageFlask.html')

'''@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash('Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('registerPageFlask.html', title='Register', form=form)
'''
@app.route('/register', methods=["GET","POST"])
def register():

    if request.method == "POST":
        name = request.form.get("name")
        username = request.form.get("username")
        password = request.form.get("password")
        conn = sqlite3.connect('database.db')
        c = conn.cursor()


        c.execute('INSERT into users VALUES (?,?,?)', (name, username, password))

        conn.commit()
        conn.close()



    return render_template('register.html')
'''@app.route('/login'  ,methods=['GET','POST'])
     def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('loginPageFlask.html', title='Login',form=form)
'''
@app.route('/login')
def login():

        return  render_template('login.html')
@app.route('/welcome', methods=['POST'])
def welcome():
    if request.method == "POST":
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        user = request.form.get('name')
        password = request.form.get('password')
        c.execute("SELECT pass FROM users WHERE username=?", (user,))
        passwordValue = c.fetchone()
        print(passwordValue)
        if(passwordValue==None):
            return render_template('login.html')
        elif (passwordValue[0] == password):
            return render_template('welcome.html')
        else:
            flash('Incorrect Password/Username')
            return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)

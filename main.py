from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', home_href='/', about_href='/', join_href='/', projects_href='/', emails='zceboys@gmail.com', emails_href='/')
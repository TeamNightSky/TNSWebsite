from flask import Flask, render_template, redirect


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', home_href='/', about_href='/', join_href='/', projects_href='/', emails='zceboys@gmail.com', emails_href='/')

@app.route('/github')
def github():
    return redirect('https://github.com/TeamNightSky')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
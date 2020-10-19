from flask import Flask, render_template, redirect

app = Flask(__name__)


@app.route('/')
def home():
    return render_template(
        'home.html',
        nav1_href='/',
        nav2_href='/',
        nav3_href='https://github.com/TeamNightSky',
        nav4_href='/',
        emails='zceboys@gmail.com',
        emails_href='/',
        navlink1='Home',
        navlink2='About',
        navlink3='Github',
        navlink4='',
    )


@app.route('/github')
def github():
    return redirect('https://github.com/TeamNightSky')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

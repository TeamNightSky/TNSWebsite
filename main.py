from flask import Flask, render_template, redirect

app = Flask(__name__)


@app.route('/')
def home():
    return render_template(
        'home.html',
        icon_href='https://www.pngrepo.com/png/296672/180/planet-galaxy.png',
        nav1_href='/',
        nav2_href='/about',
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


@app.route('/about')
def about():
    return 'about'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

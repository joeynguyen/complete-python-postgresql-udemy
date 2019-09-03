from flask import Flask, render_template, session, redirect, request

from database import Database
from user import User
from twitter_utils import get_request_token, get_oauth_verifier_url, get_access_token

app = Flask(__name__)
app.secret_key = '1234'

Database.initialise(user='joeynguyen', password='password', host='localhost', database='joeynguyen')


@app.route('/')
def homepage():
    return render_template('home.html')


@app.route('/login/twitter')
def twitter_login():
    request_token = get_request_token()
    session['request_token'] = request_token
    print('request_token', request_token)
    print('session', session)

    # redirect the user
    return redirect(get_oauth_verifier_url(request_token))


@app.route('/auth/twitter')  # http://127.0.0.1:4995/auth/twitter?oauth_token=xwA_bBPdHZ0&oauth_verifier=MdRcq5y
def twitter_auth():
    oauth_verifier = request.args.get('oauth_verifier')
    access_token = get_access_token(session['request_token'], oauth_verifier)
    print('access_token', access_token)

    user = User.load_from_db(access_token['screen_name'])
    if not user:
        user = User(access_token['screen_name'], access_token['oauth_token'],
                    access_token['oauth_token_secret'], None)
        user.save_to_db()

    session['screen_name'] = user.screen_name
    print('session', session)
    print('user', user)

    return user.screen_name


app.run(port=4995, debug=True)

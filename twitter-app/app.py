from flask import Flask, render_template, session, redirect, request, url_for, g
import requests

from database import Database
from user import User
from twitter_utils import get_request_token, get_oauth_verifier_url, get_access_token
import constants

app = Flask(__name__)
app.secret_key = '1234'

Database.initialise(user='joeynguyen', password='password', host='localhost', database='joeynguyen')


@app.before_request
def load_user():
    if 'screen_name' in session:
        g.user = User.load_from_db(session['screen_name'])


@app.route('/')
def homepage():
    return render_template('home.html')


@app.route('/login/twitter')
def twitter_login():
    if 'screen_name' in session:
        return redirect(url_for('profile'))

    request_token = get_request_token()
    session['request_token'] = request_token

    # redirect the user
    return redirect(get_oauth_verifier_url(request_token))


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('homepage'))


@app.route('/auth/twitter')  # http://127.0.0.1:4995/auth/twitter?oauth_token=xwA_bBPdHZ0&oauth_verifier=MdRcq5y
def twitter_auth():
    oauth_verifier = request.args.get('oauth_verifier')
    access_token = get_access_token(session['request_token'], oauth_verifier)

    user = User.load_from_db(access_token['screen_name'])
    if not user:
        user = User(access_token['screen_name'], access_token['oauth_token'],
                    access_token['oauth_token_secret'], None)
        user.save_to_db()

    session['screen_name'] = user.screen_name
    print('session', session)
    print('user', user)

    return redirect(url_for('profile'))


@app.route('/profile')
def profile():
    return render_template('profile.html', user=g.user)


@app.route('/search')
def search():
    query = request.args.get('q')
    url = "{}?q={}+filter:images".format(constants.TWEETS_SEARCH_URL, query)
    tweets = g.user.twitter_request(url)

    tweet_texts = [{'tweet': s['text'], 'label': ''} for s in tweets['statuses']]

    for tweet in tweet_texts:
        r = requests.post('http://text-processing.com/api/sentiment/', data={'text': tweet['tweet']})
        json_reponse = r.json()
        label = json_reponse['label']
        tweet['label'] = label

    return render_template('search.html', content=tweet_texts)


app.run(port=4995, debug=True)

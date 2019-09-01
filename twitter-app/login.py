import constants
from user import User
from database import Database
from twitter_utils import get_request_token, get_oauth_verifier, get_access_token

Database.initialise(user='joeynguyen', password='password', host='localhost', database='joeynguyen')

email = input("Enter your email: ")
user = User.load_from_db(email)

if user:
    print("This email is already in the database")
else:
    request_token = get_request_token()

    oauth_verifier = get_oauth_verifier(request_token)

    access_token = get_access_token(request_token, oauth_verifier)

    first_name = input("Enter your first_name: ")
    last_name = input("Enter your last_name: ")

    user = User(email, first_name, last_name, access_token['oauth_token'], access_token['oauth_token_secret'], None)
    user.save_to_db()

tweets = user.twitter_request("{}?q=computers+filter:images".format(constants.TWEETS_SEARCH_URL))

if tweets:
    for s in tweets['statuses']:
        print(s['text'])

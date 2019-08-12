import secrets
import constants
import oauth2
import json
import urllib.parse as urlparse

consumer = oauth2.Consumer(secrets.CONSUMER_KEY, secrets.CONSUMER_SECRET)
client = oauth2.Client(consumer)

# Use the client to perform a request for the request token
response, content = client.request(constants.REQUEST_TOKEN_URL, 'POST')
if response.status != 200:
    print("An error occurred getting the request token from Twitter")

# Get the request token parsing the query string returned
request_token = dict(urlparse.parse_qsl(content.decode('utf-8')))

# Ask the user to authorize our app and give us the PIN code
print("Go to the following site in your browser:")
print("{}?oauth_token={}".format(constants.AUTHORIZATION_URL, request_token['oauth_token']))
oauth_verifier = input("What is the PIN? ")

# Create a Token object which contains the request token and the verifier
token = oauth2.Token(request_token['oauth_token'], request_token['oauth_token_secret'])
token.set_verifier(oauth_verifier)

# Create a client with our consumer (our app) and the newly created (and verified) token
client = oauth2.Client(consumer, token)

# Ask Twitter for an access token, and Twitter knows it should give it to us because we've verified the request token
response, content = client.request(constants.ACCESS_TOKEN_URL, 'POST')
access_token = dict(urlparse.parse_qsl(content.decode('utf-8')))

print('access_token', access_token)

# Create an 'authorized_token' Token object and use that to perform Twitter API calls on behalf of the user
authorized_token = oauth2.Token(access_token['oauth_token'], access_token['oauth_token_secret'])
authorized_client = oauth2.Client(consumer, authorized_token)

# Make Twitter API calls
response, content = authorized_client.request("{}?q=computers+filter:images".format(constants.TWEETS_SEARCH_URL), 'GET')

if response.status != 200:
    print("An error occurred while searching!")

# convert response string into Python dict
tweets = json.loads(content.decode('utf-8'))

for s in tweets['statuses']:
    print(s['text'])

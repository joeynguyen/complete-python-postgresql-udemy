import secrets
import constants
import oauth2
import urllib.parse as urlparse

consumer = oauth2.Consumer(secrets.CONSUMER_KEY, secrets.CONSUMER_SECRET)
client = oauth2.Client(consumer)

response, content = client.request(constants.REQUEST_TOKEN_URL, 'POST')
if response.status != 200:
    print('An error occurred getting the request token from Twitter')

request_token = dict(urlparse.parse_qsl(content.decode('utf-8')))

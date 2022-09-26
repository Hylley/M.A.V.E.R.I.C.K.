import tweepy
from json import load, dump

class Auth:
    def __init__(self, api_key, api_key_secret, access_token, access_token_secret):
        auth = tweepy.OAuthHandler(
            api_key,
            api_key_secret
        )

        auth.set_access_token(
            access_token,
            access_token_secret
        )

        self.api = tweepy.API(auth)
        self.load_data()
    
    def new_replies(self):
        self.load_data()

        replies = self.api.mentions_timeline(
            since_id = self.data['last_registered_reply_id'],
            tweet_mode = 'extended'
        )

        if not replies: return None

        self.data['last_registered_reply_id'] = replies[0].id

        self.update_data()

        return replies

    def preivous_reply(self, id):
        status = self.api.get_status(id)
        
        if not status: return None

        previous = self.api.get_status(status.in_reply_to_status_id, tweet_mode='extended')

        if not previous: return None

        return previous

    def load_data(self):
        with open('Twitter\data.json', 'r') as data_file:
            self.data = load(data_file)
        
            return self.data

    def update_data(self):
        with open('Twitter\data.json', 'w') as data_file:
            dump(self.data, data_file, indent=4)



# def twitterAuthenticate():
#     # Autenticação.
#     auth = tweepy.OAuthHandler(load_dotenv('API_KEY'), load_dotenv('API_KEY_SECRET'))
#     auth.set_access_token(load_dotenv('ACCESS_TOKEN'), load_dotenv('ACCESS_TOKEN_SECRET'))

#     # Criação do objeito de API do Twitter.
#     twt = tweepy.API(auth)
#     return twt
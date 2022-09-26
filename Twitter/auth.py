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
        self.LoadData()
    
    def LoadData(self):
        with open('Twitter\data.json', 'r') as data_file:
            self.data = load(data_file)
        
            return self.data

    def UpdateData(self):
        with open('Twitter\data.json', 'w') as data_file:
            dump(self.data, data_file, indent=4)
    
    def MentionsTimeline(self):
        self.LoadData()

        replies = self.api.mentions_timeline(
            since_id = self.data['last_registered_reply_id'],
            tweet_mode = 'extended'
        )

        if not replies: return None

        self.data['last_registered_reply_id'] = replies[0].id

        self.UpdateData()

        return replies

    def SearchForPreviousTweet(self, id):
        status = self.api.get_status(id)
        
        if not status: return None

        previous = self.api.get_status(status.in_reply_to_status_id, tweet_mode='extended')

        if not previous: return None

        return previous

    def Reply(self, text, tweet_id):
        self.api.update_status(
            status = text,
            in_reply_to_status_id = tweet_id,
            auto_populate_reply_metadata = True
        )

        print(f'MAV: {text}')


# def twitterAuthenticate():
#     # Autenticação.
#     auth = tweepy.OAuthHandler(load_dotenv('API_KEY'), load_dotenv('API_KEY_SECRET'))
#     auth.set_access_token(load_dotenv('ACCESS_TOKEN'), load_dotenv('ACCESS_TOKEN_SECRET'))

#     # Criação do objeito de API do Twitter.
#     twt = tweepy.API(auth)
#     return twt
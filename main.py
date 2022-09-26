from AI import AI
from os import getenv
from time import sleep
from Twitter import Auth
from dotenv import load_dotenv

TWEET_RESPONSE_DELAY = 1
TWEET_RESEARCH_DELAY = 10

load_dotenv()

Maverick = AI('MAVERICK', '~$', False)
Twitter = Auth(
    getenv('API_KEY'),
    getenv('API_KEY_SECRET'),
    getenv('ACCESS_TOKEN'),
    getenv('ACCESS_TOKEN_SECRET')
)

last_statement = None

while True:
    timeline = Twitter.new_replies()

    if timeline:
        Maverick.open_session()

        for tweet in timeline:
            plast_statement = Twitter.preivous_reply(tweet.id).full_text

            print(Maverick.talk(tweet.full_text, last_statement))

            sleep(TWEET_RESPONSE_DELAY)
        
        Maverick.close_session()
    
    sleep(TWEET_RESEARCH_DELAY)

    # text = input('>')

    # if text == '~$q':
    #     Maverick.close_session()
    #     break

    # response = Maverick.talk(text, last_statement)

    # if not response == 110:
    #     print(response)
    #     last_statement = response
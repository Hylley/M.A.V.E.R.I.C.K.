from os import getenv
from time import sleep
from dotenv import load_dotenv

from AI import AI
from Twitter import Auth, MentionLinkFilter

TWEET_RESPONSE_DELAY = 2
TWEET_RESEARCH_DELAY = 60

load_dotenv()

Maverick = AI('MAVERICK', '~$', True)
Twitter = Auth(
    getenv('API_KEY'),
    getenv('API_KEY_SECRET'),
    getenv('ACCESS_TOKEN'),
    getenv('ACCESS_TOKEN_SECRET')
)

last_statement = None

while True:
    mentions = Twitter.MentionsTimeline()

    if mentions:
        Maverick.OpenSession()

        for tweet in mentions:
            previous_tweet = Twitter.SearchForPreviousTweet(tweet.id)

            response = Maverick.Talk(
                MentionLinkFilter(tweet.full_text),
                MentionLinkFilter(previous_tweet.full_text)
            )

            if response and not response == 110:
                try:
                    Twitter.Reply(
                        response,
                        tweet.id
                    )
                except Exception as error:
                    print(error)

                sleep(TWEET_RESPONSE_DELAY)
        
        Maverick.CloseSession()
    
    sleep(TWEET_RESEARCH_DELAY)

    # text = input('>')

    # if text == '~$q':
    #     Maverick.close_session()
    #     break

    # response = Maverick.talk(text, last_statement)

    # if not response == 110:
    #     print(response)
    #     last_statement = response
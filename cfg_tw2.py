import tweepy


consumer_key = 'u49TM32o5fGz6BBVBvdX1D5lA'
consumer_secret = 'ggq8FLJb75ZwzFI8Nk5Nr2PIp8t5rFm5svoyvbSn2nESv8E8wc'
access_token = '20428729-EYECo8G9JQjFmdFtmRLs7k50cZBAQ7Bai3ewWVJHK'
access_token_secret = 'pOSOEtzL0EhzwPIf3SqEZtPdxLg9iguMHgowtKRO3WnQF'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

twitter_api = tweepy.API(auth)

cfg_tweets = twitter_api.search(
    q="CodeFirstGirls"
)

for tweet in cfg_tweets:
    print tweet.user.name + ": " + tweet.text
import tweepy

auth = tweepy.OAuthHandler('u49TM32o5fGz6BBVBvdX1D5lA',  'ggq8FLJb75ZwzFI8Nk5Nr2PIp8t5rFm5svoyvbSn2nESv8E8wc')
auth.set_access_token('20428729-EYECo8G9JQjFmdFtmRLs7k50cZBAQ7Bai3ewWVJHK', 'pOSOEtzL0EhzwPIf3SqEZtPdxLg9iguMHgowtKRO3WnQF')

twitter_api = tweepy.API(auth)

cfg_tweets = twitter_api.search(
    q="CodeFirstGirls"
)

for tweet in cfg_tweets:
    print tweet.user.name + ": " + tweet.text
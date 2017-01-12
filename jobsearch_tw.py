# -*- coding: utf-8 -*-
import tweepy
import pdb

consumer_key = 'u49TM32o5fGz6BBVBvdX1D5lA'
consumer_secret = 'ggq8FLJb75ZwzFI8Nk5Nr2PIp8t5rFm5svoyvbSn2nESv8E8wc'
access_token = '20428729-EYECo8G9JQjFmdFtmRLs7k50cZBAQ7Bai3ewWVJHK'
access_token_secret = 'pOSOEtzL0EhzwPIf3SqEZtPdxLg9iguMHgowtKRO3WnQF'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

twitter_api = tweepy.API(auth)

results = twitter_api.search(
    q="content manager London",
    lang="en"
)

with open("hello.txt", "wb") as f:
	for tweet in results:
	#print tweet.user.name + ":" + tweet.text
		line = tweet.user.name + ":" + tweet.text
		f.write(line.encode("UTF-8") + "\r\n")

results = twitter_api.search(
    q="content manager London",
    lang="en",
	since_id = tweet.id)

for tweet in results:
	line = tweet.user.name + ":" + tweet.text
	print line.encode("UTF-8")

#print len(results) 
#pdb.set_trace()



	#assert isinstance(SearchResults, object)
	#print result
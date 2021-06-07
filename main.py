import os
import tweepy as tw
import pandas as pd
from os import system
import datetime as dt
from textblob import TextBlob
system('cls')
consumer_key= ''
consumer_secret= ''
access_token= ''
access_token_secret= ''
auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)
date_since = dt.datetime.now().date()
tweet_amount = 1000
search_words = input('Input word for analysis: ')
new_search = search_words + "-filter:retweets"
tweets = tw.Cursor(api.search,
              q=new_search,
              lang="en",
              since=date_since).items(tweet_amount)
i=0
total=0
print('Starting analysis...')
for tweet in tweets:
	new_tweet = tweet.text
	analysis = TextBlob(new_tweet)
	if analysis.polarity == 0.0:
		sum = total
	else:
		sum = analysis.polarity + total
	total = sum
	i+=1
	percentage = round(i / tweet_amount * 100, 1)
	system('cls')
	print('Processing:',percentage,'%') 
overall = sum / tweet_amount
if overall > 0.1:
	world_mood = 'very positive'
elif overall > 0.05:
	world_mood = 'positive'
elif overall < 0.05:
	world_mood = 'negative'
elif overall < 0.0:
	world_mood = 'very negative'
elif overall > 0.01 and overall < 0.01:
	world_mood = 'neutral'
system('cls')
print('Analysed:', i, 'Tweets')
print('Total:', overall)
print('World Mood:', world_mood)
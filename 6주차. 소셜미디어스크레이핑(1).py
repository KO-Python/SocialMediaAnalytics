"""
트위터는 대표적인 데이터 분석 대상 플랫폼임
트위터 내용 수집을 위해서 다양한 모듈이 존재하지만 API기반 수집이 안정적인 수집방법임
Tweepy는 API 기반 데이터 수집 모듈임
개인 액세스 토큰 확인 방법: https://developer.twitter.com/en/docs/authentication/oauth-1-0a/api-key-and-secret
"""

import tweepy
import pandas as pd

consumer_key = "drk0gtFoFdTCc41SwQNMCReX5"
consumer_secret = "Fd9Zrd2cuZHmaKo3jhnO2q01mqH47h4cqQF5XRnuExh38zKoWg"
access_token = "3432925246-jq6QJzaSsN2ftVO5NQwLxfQanhXFWcbaAwenK4K"
access_token_secret = "dbfpHpXhwwz2rPcuDVESVCur60swqkcjCnfvzUcFqL7sw"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

keyword =  '윤석열'
# search for tweets containing keyword
keyword = "data science"
tweets = api.search_tweets(keyword, lang="en")
# extract the text of each tweet
texts = [tweet.text for tweet in tweets]
# print the text of each tweet
for text in texts:
    print(text)







# search for tweets containing keyword
keyword = "윤석열"
tweets = api.search_tweets(keyword)
# extract the date, username, and text of each tweet
data = [(tweet.created_at, tweet.user.screen_name, tweet.text) for tweet in tweets]
# print the date, username, and text of each tweet
for d in data:
    print(d[0], d[1], d[2])









"""
To scrape tweets, date, username, 
number of followers, and save the information to a CSV file using the tweepy library, 
you can extract the created_at, user.screen_name, user.followers_count, and 
text attributes of each tweet object and write them to a CSV file using the csv module. 
"""
# set up tweepy API client
import csv
# search for tweets containing keyword
keyword = "윤석열"
tweets = api.search_tweets(keyword)

# extract the date, username, followers count, and text of each tweet
data = [(tweet.created_at, tweet.user.screen_name, tweet.user.followers_count, tweet.text) for tweet in tweets]

# write the data to a CSV file
with open("tweets.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Date", "Username", "Followers Count", "Text"])
    writer.writerows(data)








"""
To scrape past tweets using the tweepy library, 
you can use the Cursor object in the API. 
The Cursor provides a convenient way to paginate through results and retrieve a large number of tweets. 
"""
# search for tweets containing keyword
keyword = "윤석열"

# use tweepy cursor to paginate through results and retrieve up to 100 tweets
tweets = tweepy.Cursor(api.search_tweets, q=keyword).items(100)

# extract the date, username, followers count, and text of each tweet
data = [(tweet.created_at, tweet.user.screen_name, tweet.user.followers_count, tweet.text) for tweet in tweets]

# write the data to a CSV file
with open("tweets.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Date", "Username", "Followers Count", "Text"])
    writer.writerows(data)










# Create an API object
import json

# Create an API object
api = tweepy.API(auth)

# Define the stream listener
class MyStreamListener(tweepy.Stream):
    def on_data(self, data):
        # Print the text of the tweet
        tweet = json.loads(data)
        print(tweet['text'])

# Start the stream
myStreamListener = MyStreamListener(auth=api.auth)
myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)
myStream.filter(track=['keyword1', 'keyword2'])


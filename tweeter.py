# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 11:40:45 2018

@author: Vijay
"""

#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

consumer_key = 'zLQbhnx4Rm0zQrtBMv5KNr7u6'
consumer_secret = 'ByfhCH9zrC5Fh0erNAPRNfpSAjAxNqgH5hkdjlKqaM784bSFRT'
access_token = '323803298-SeIKcBy3jfXrW1AuR9Ec8M5yrnnIFrqBYc5wSGch'
access_secret = 'eFRMQ7CbR5iFUilWA9P3AjoEnkCZExEdqffzbn7XBdxcb'

#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print (data)
        return True

    def on_error(self, status):
        print (status)


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['python', 'javascript', 'ruby'])
   
    def on_data(self, data):
        with open('data/twitter_data.txt','a',encoding='utf8') as f:
            all_data = json.loads(data)
            tweet = all_data["text"]
            print(all_data)
            f.write(tweet)
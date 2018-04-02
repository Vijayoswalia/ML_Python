# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 10:11:18 2018

@author: Vijay
"""

#%% sentiment analysis
import tweepy          # To consume Twitter's API
import pandas as pd     # To handle data
import numpy as np      # For number computing

# For plotting and visualization:
from IPython.display import display
import matplotlib.pyplot as plt
import seaborn as sns
from tweepy import OAuthHandler
# Twitter App access keys for @user

# Consume:
CONSUMER_KEY    = 'zLQbhnx4Rm0zQrtBMv5KNr7u6'
CONSUMER_SECRET = 'ByfhCH9zrC5Fh0erNAPRNfpSAjAxNqgH5hkdjlKqaM784bSFRT'

# Access:
ACCESS_TOKEN  = '323803298-SeIKcBy3jfXrW1AuR9Ec8M5yrnnIFrqBYc5wSGch'
ACCESS_SECRET = '	eFRMQ7CbR5iFUilWA9P3AjoEnkCZExEdqffzbn7XBdxcb'

# API's setup:
def twitter_setup():
    """
    Utility function to setup the Twitter's API
    with our access keys provided.
    """
    # Authentication and access using keys:
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

    # Return API with authentication:
    api = tweepy.API(auth)
    return api

# We create an extractor object:
extractor = twitter_setup()

# We create a tweet list as follows:
tweets = extractor.user_timeline(screen_name="ivy", count=200)
print("Number of tweets extracted: {}.\n".format(len(tweets)))

# We print the most recent 5 tweets:
print("5 recent tweets:\n")
for tweet in tweets[:5]:
    print(tweet.text)
    print()

# We create a pandas dataframe as follows:
data = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['Tweets'])

# We display the first 10 elements of the dataframe:
display(data.head(10))

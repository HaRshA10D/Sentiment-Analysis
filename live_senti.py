# -*- coding: utf-8 -*-
"""
Created on Fri May 26 19:59:01 2017

@author: Harsha SlimShady
"""

import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener

import json

from textblob import TextBlob
import re

import matplotlib.pyplot as plt

consumer_key = 'C5AuTRgdv5NNtRtIcvlsbiUT3'
consumer_secret = 'WI1ePKnfXNPcX6FoBhWUoqkT4rJn55oA5eIHVSCxJWhYphd1MI'
acess_token = '3022120112-WfskTNLDV2RZSKyvimx4DFX0reOWcDRFGADakYr'
acess_secret = 'ICW6OPMkirNur8m9x1zhdwpx8uBCMW0SouL5aLxKxnVCK'

auth = OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(acess_token,acess_secret)

api = tweepy.API(auth)

def getOwnTimeline():
    for tweet in api.home_timeline():
        blob = TextBlob(clean_tweet(tweet.text))
        if blob.sentiment.polarity > 0:
            print('positive one by ' + tweet.user.name)
        else:
            print('Negetive one by ' + tweet.user.name)
            
def getUser(name):
    user = api.get_user(name)
    print(user.screen_name)
    print(user.followers_count)
    for user in user.friends():
        print(user.screen_name)
            
def clean_tweet(tweet):
    tweet=" ".join(re.findall("[a-zA-Z]+", tweet))
    return tweet

def myProfileSenti():
    i = 1

    for tweet in tweepy.Cursor(api.user_timeline).items():
        cleanTweet = clean_tweet(tweet.text)
        blob = TextBlob(cleanTweet)
        polarity = blob.sentiment.polarity
        print(polarity)
        plt.plot([i],[polarity],'ro')
        i += 1
        
        
    plt.axis([0,30,-1,+1])
    plt.show()




        
        
        
        
        
        
        
        
        
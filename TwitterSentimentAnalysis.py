# -*- coding: utf-8 -*-
"""
Created on Wed May  9 11:55:35 2018

@author: e1077611
"""
import json
import os
from textblob import TextBlob

class TwitterClient(object):
    '''
    Generic Twitter Class for sentiment analysis.
    '''
    def __init__(self):
        '''
        Class constructor or initialization method.
        '''
        # keys and tokens from the Twitter Dev Console
# =============================================================================
#         consumer_key = 'XXXXXXXXXXXXXXXXXXXXXXXX'
#         consumer_secret = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXX'
#         access_token = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXX'
#         access_token_secret = 'XXXXXXXXXXXXXXXXXXXXXXXXX'
# =============================================================================

    def get_tweet_sentiment(self, tweet):
        analysis = TextBlob(tweet)
        if analysis.sentiment.polarity > 0:
            return 'positive'
        elif analysis.sentiment.polarity == 0:
            return 'neutral'
        else:
            return 'negative'

    def get_tweets(self, hashTag):
        tweets = []
        fetched_tweets = self.mine_tweets(hashTag);
        for tweet in fetched_tweets:
                parsed_tweet = {}
                parsed_tweet['text'] = tweet
                parsed_tweet['sentiment'] = self.get_tweet_sentiment(tweet)
                tweets.append(parsed_tweet)
        return tweets
    
    def get_tweets_prod(self, hashTag, prodHashTag):
        tweets = []
        fetched_tweets = self.mine_tweets_prod(hashTag, prodHashTag);
        for tweet in fetched_tweets:
                parsed_tweet = {}
                parsed_tweet['text'] = tweet
                parsed_tweet['sentiment'] = self.get_tweet_sentiment(tweet)

                tweets.append(parsed_tweet)

        return tweets
    
    def mine_tweets_prod(self, compHashTag, prodHashTag):
        THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
        twitter_dump = os.path.join(THIS_FOLDER,'twitterDummyExample.txt')

        tweets_data = []
        tweets_file = open(twitter_dump, "r")
        found = False
        for line in tweets_file:
            found = False
            tweet = json.loads(line)
            for key, value in tweet.items():
                    if found == True:
                        break
                    foundCompHashTag =False
                    foundProdHashTag =False
                    if key=='entities':
                        for key, value in value.items():
                            if found == True:
                                break
                            if key=='hashtags':
                                for x in value:
                                    if x["text"] == compHashTag:
                                        foundCompHashTag =True
                                    if x["text"] == prodHashTag:
                                        foundProdHashTag =True
                    if foundCompHashTag == True and  foundProdHashTag == True:
                            tweets_data.append(tweet["text"])
                            found = True
                            break
        return tweets_data

    def mine_tweets(self, hashTag):
        THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
        twitter_dump = os.path.join(THIS_FOLDER,'twitterDummyExample.txt')

        tweets_data = []
        tweets_file = open(twitter_dump, "r")
        found = False
        for line in tweets_file:
            found = False
            try:
                tweet = json.loads(line)
                for key, value in tweet.items():
                    if found == True:
                        break
                    if key=='entities':
                     for key, value in value.items():
                         if found == True:
                             break
                         if key=='hashtags':
                          for x in value:
                           if x["text"] == hashTag:
                            print(tweet["text"])
                            tweets_data.append(tweet["text"])
                            found = True
                            break

            except:
                continue
        return tweets_data
    def analyseTweetData(self, hashTag, prodHashTag):
        if prodHashTag:
            tweets = self.get_tweets_prod(hashTag, prodHashTag)
        else:
            tweets = self.get_tweets(hashTag)
        
        ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
        if(len(tweets) != 0):
            pSentiment=100*len(ptweets)/len(tweets)
        else:
            pSentiment=0
        
        ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']
        if(len(tweets) != 0):
            nSentiment=100*len(ntweets)/len(tweets)
        else:
            nSentiment=0
        sentimentArray= []
        sentimentArray.append(pSentiment)
        sentimentArray.append(nSentiment)
        return sentimentArray

def main():
    # creating object of TwitterClient Class
    api = TwitterClient()
    sentimentArray = api.analyseTweetData('FIS','IO')
    print("Positive sentiment-->{} %".format(sentimentArray[0]))
    print("Negative sentiment-->{} %".format(sentimentArray[1]))
    # calling function to get tweets
    #tweets = api.get_tweets(query = 'FIS', count = 200)

    # picking positive tweets from tweets
   # ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
   # if(len(tweets) != 0):
      #  pSentiment=100*len(ptweets)/len(tweets)
   # else:
     #   pSentiment=0
    # percentage of positive tweets
   # print("Positive tweets percentage: {} %".format(pSentiment))
    # picking negative tweets from tweets
  #  ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']
   # if(len(tweets) != 0):
    #    nSentiment=100*len(ntweets)/len(tweets)
   # else:
   #    nSentiment=0
    # percentage of negative tweets
   # print("Negative tweets percentage: {} %".format(nSentiment))

   # print("Sentiment analysis for Infosys------>")
   # tweets = api.get_tweets(query = 'Infosys', count = 200)

    # picking positive tweets from tweets
  #  ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
    # percentage of positive tweets
  #  print("Positive tweets percentage: {} %".format(100*len(ptweets)/len(tweets)))
    # picking negative tweets from tweets
   # ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']
    # percentage of negative tweets
   # print("Negative tweets percentage: {} %".format(100*len(ntweets)/len(tweets)))
    # percentage of neutral tweets
if __name__ == "__main__":
    # calling main function
    main()

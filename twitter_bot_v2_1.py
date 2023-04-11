#!/usr/bin/python3
import os
import tweepy
import openai


api_key = "<API_KEY>"
api_secret = "<API_SECRET_KEY>"
bearer_token = "<BEARER_TOKEN>"
access_token = "<ACCESS_TOKEN>"
access_token_secret = "<ACCESS_TOKEN_SECRET>"

client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)
    
auth = tweepy.OAuthHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)

openai.api_key = '<OPENAI_API_KEY>'


def read_tweets_from_file(file_path):
    with open(file_path, "r") as file:
        tweets = file.read().splitlines()
    return tweets

def generate_tweet(prompt, max_tokens=280, temperature=0.8, max_length=280):
    while True:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=max_tokens,
            n=1,
            stop=None,
            temperature=temperature,
        )

        tweet = response.choices[0].text.strip()
    
        if len(tweet) <= max_length:
    	    break
    	
    return tweet

if __name__ == "__main__":
    
    tweets_file_path = "/your/path/to/user_tweets.txt"
    tweets = read_tweets_from_file(tweets_file_path)

    
    prompt = f"Write a tweet in the style of the user based on these tweets and do not put hashtag and quotation mark and make all letters lower case. : {tweets}"
    
    
    generated_tweet = generate_tweet(prompt)
    
    client.create_tweet(text=generated_tweet)
    

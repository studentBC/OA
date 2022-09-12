"""
Please use Python version 3.7+
"""

import csv
import sys
from typing import List, Tuple

class TweetIndex:
    # Starter code--please override
    def __init__(self):
        self.list_of_tweets = []

    # Starter code--please override
    def process_tweets(self, list_of_timestamps_and_tweets: List[Tuple[str, int]]) -> None:
        """
        process_tweets processes a list of tweets and initializes any data structures needed for
        searching over them.

        :param list_of_timestamps_and_tweets: A list of tuples consisting of a timestamp and a tweet.
        """
        for row in list_of_timestamps_and_tweets:
            timestamp = int(row[0])
            tweet = str(row[1])
            uniq = set(tweet.split(" "))
            self.list_of_tweets.append((tweet, timestamp, uniq))

    # Starter code--please override
    def search(self, query: str) -> List[Tuple[str, int]]:
        """
        NOTE: Please update this docstring to reflect the updated specification of your search function

        search looks for the most recent tweet (highest timestamp) that contains all words in query.

        :param query: the given query string
        :return: a list of tuples of the form (tweet text, tweet timestamp), ordered by highest timestamp tweets first. 
        If no such tweet exists, returns empty list.
        """
        list_of_words = query.split(" ")
        result_tweet, result_timestamp = "", -1
        for tweet, timestamp in self.list_of_tweets:
            words_in_tweet = tweet.split(" ")
            tweet_contains_query = True
            for word in list_of_words:
                if word not in words_in_tweet:
                    tweet_contains_query = False
                    break
            if tweet_contains_query and timestamp > result_timestamp:
                result_tweet, result_timestamp = tweet, timestamp
        return [(result_tweet, result_timestamp)] if result_timestamp != -1 else []

if __name__ == "__main__":
    # A full list of tweets is available in data/tweets.csv for your use.
    tweet_csv_filename = "../data/small.csv"
    list_of_tweets = []
    with open(tweet_csv_filename, "r") as f:
        csv_reader = csv.reader(f, delimiter=",")
        for i, row in enumerate(csv_reader):
            if i == 0:
                # header
                continue
            timestamp = int(row[0])
            tweet = str(row[1])
            list_of_tweets.append((timestamp, tweet))

    #read command line argument
    n = len(sys.argv)
    for i in range(1, n):
        print(sys.argv[i], end = " ")
    
    ti = TweetIndex()
    ti.process_tweets(list_of_tweets)
    assert ti.search("hello") == ('hello this is also neeva', 15)
    assert ti.search("hello me") == ('hello not me', 14)
    assert ti.search("hello bye") == ('hello bye', 3)
    assert ti.search("hello this bob") == ('hello neeva this is bob', 11)
    assert ti.search("notinanytweets") == ('', -1)
    print("Success!")

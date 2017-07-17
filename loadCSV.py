import pandas as pd
import numpy as np
import re


class loadCSV(object):
    def __init__(self):
        dataSet = [i.strip().split(",") for i in open('smileannotationsfinal.csv', 'r', encoding="utf8").readlines()]

        for index, val in enumerate(dataSet):
            if len(val) > 3:
                dataSet[index] = [val[0], ','.join(val[1:len(val) - 1]), val[-1]]
            dataSet[index][1] = cleanTweet(dataSet[index][1])

        self.tweetDataFrame = pd.DataFrame(dataSet, columns=['ID', 'Tweet', 'Classifiation'])



def cleanTweet(tweet):
    tweet = tweet.lower()
    #Convert www.* or https?://* to URL
    tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))','URL',tweet)
    #Convert @username to AT_USER
    tweet = re.sub('@[^\s]+','AT_USER',tweet)
    #Remove additional white spaces
    tweet = re.sub('[\s]+', ' ', tweet)
    #Replace #word with word
    tweet = re.sub(r'#([^\s]+)', r'\1', tweet)
    #trim
    tweet = tweet.strip('\'"')
    return tweet

def main():
    csvData = loadCSV()
    print(csvData.tweetDataFrame.head())
    csvData.tweetDataFrame.to_csv('export.csv', sep=',', encoding='utf-8')



if __name__ == "__main__":
    # calling main function
    main()
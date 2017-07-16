import pandas as pd
import numpy as np
import re

dataSet = [i.strip().split(",") for i in open('smileannotationsfinal.csv', 'r', encoding="utf8").readlines()]

for index, val in enumerate(dataSet):
    if len(val)>3:
        dataSet[index] = [val[0], ','.join(val[1:len(val) - 1]), val[-1]]


tweetDataFrame = pd.DataFrame(dataSet, columns = ['ID', 'Tweet', 'Classifiation'])
print(tweetDataFrame.head())


def cutMention(self, tweet):
    mentionList = re.findall('(@\w+)', tweet)
    resultTweet = [word for word in tweet.split() if word not in mentionList]
    return ' '.join(resultTweet)
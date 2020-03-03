# Imports
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer 

def custom_score(sentence):
    # Create a SentimentIntensityAnalyzer object. 
    sid_obj = SentimentIntensityAnalyzer() 

    # polarity_scores method of SentimentIntensityAnalyzer 
    # oject gives a sentiment dictionary. 
    # which contains pos, neg, neu, and compound scores. 
    sentiment_dict = sid_obj.polarity_scores(sentence)

    return sentiment_dict['compound'] 


def compound_sum_score(sentence_list):

    troll_lst = []


    for sentence in sentence_list:
        troll_lst.append(custom_score(sentence))

    troll_score = sum(troll_lst) / len(troll_lst)


    return troll_score 
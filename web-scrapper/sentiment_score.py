import streamlit as st
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer


def review_score(reviews):
    review_score_list = []
    neg, neu, pos = [], [], []
    sid = SentimentIntensityAnalyzer()
    for sentence in reviews:
        ss = sid.polarity_scores(sentence)
        for k in ss:
            if k == "neg":
                neg.append(ss[k])
            elif k == "pos":
                pos.append(ss[k])
            elif k == "neu":
                neu.append(ss[k])

    neg_score = sum(neg) / len(neg)
    pos_score = sum(pos) / len(pos)
    neu_score = sum(neu) / len(neu)

    review_score_list.append(neg_score)
    review_score_list.append(pos_score)
    review_score_list.append(neu_score)
    return review_score_list


def display_scores(scores):
    st.success(f"Positive Score: {round(scores[1] * 100, 3)}")
    st.warning(f"Neutral Score: {round(scores[2] * 100, 3)}")
    st.error(f"Negative Score: {round(scores[0] * 100, 3)}")

from nltk.sentiment.vader import SentimentIntensityAnalyzer
import streamlit as st
from bs4 import BeautifulSoup
import requests

st.markdown("<h1 style='text-align: center'> Movie Review Generator</h1>",
            unsafe_allow_html=True)
movie_name = st.text_input("Enter a movie name")
movie_name = movie_name.lower()
movie_name = movie_name.replace(' ', '_')

critic_reviews, audience_reviews = [], []

# scrapper
critic_rt = requests.get(
    f"https://www.rottentomatoes.com/m/{movie_name}/reviews?type=top_critics").text
audience_rt = requests.get(
    f"https://www.rottentomatoes.com/m/{movie_name}/reviews?type=user").text

critic_soup = BeautifulSoup(critic_rt, 'lxml')
audience_soup = BeautifulSoup(audience_rt, 'lxml')

cr_row = critic_soup.find_all('div', class_='review-row')
for cr in cr_row:
    review_text = cr.find('div', class_='review-text-container')
    quote = review_text.find('p', class_='review-text').text.strip()
    critic_reviews.append(quote)

ar_row = audience_soup.find_all('div', class_='review-text-container')
for ar in ar_row:
    audience_quote = ar.find(
        'p', class_='audience-reviews__review js-review-text clamp clamp-8 js-clamp').text.strip()
    audience_reviews.append(audience_quote)


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


if critic_reviews and audience_reviews:
    st.subheader("Top 5 Critic Reviews")
    for idx, val in enumerate(critic_reviews):
        if idx == 5:
            break
        st.write(val)

    cr_score = review_score(critic_reviews)
    st.success(f"Positive Score: {round(cr_score[1] * 100, 3)}")
    st.warning(f"Neutral Score: {round(cr_score[2] * 100, 3)}")
    st.error(f"Negative Score: {round(cr_score[0] * 100, 3)}")

    st.subheader("Top 5 Audience Reviews")
    for idx, val in enumerate(audience_reviews):
        if idx == 5:
            break
        st.write(val)

    aud_score = review_score(audience_reviews)
    st.success(f"Positive Score: {round(aud_score[1] * 100, 3)}")
    st.warning(f"Neutral Score: {round(aud_score[2] * 100, 3)}")
    st.error(f"Negative Score: {round(aud_score[0] * 100, 3)}")

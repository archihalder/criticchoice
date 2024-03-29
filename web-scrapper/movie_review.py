import streamlit as st
from bs4 import BeautifulSoup
import requests
import sentiment_score as ss


def intro():
    st.markdown("<h1 style='text-align: center'> CinemaSense </h1>", unsafe_allow_html=True)
    movie_name = st.text_input("Enter a movie name")
    movie_name = movie_name.lower()
    movie_name = movie_name.replace(' ', '_')
    return movie_name


def movie_info(movie_name):
    html = requests.get(f"https://www.rottentomatoes.com/m/{movie_name}").text
    soup = BeautifulSoup(html, 'lxml')

    all_info = soup.find_all('li', class_='info-item')
    labels = ['Rating', 'Genre', 'Director', 'Producer', 'Runtime']
    di = {}
    for info_data in all_info:
        category = info_data.find('b').text[:-1]
        if category in labels:
            category_data = info_data.find('span', class_="info-item-value").text.split()
            di[category] = category_data

    if di:
        st.subheader("Movie Info")
        for key, val in di.items():
            st.write(f"{key}: {' '.join(val)}")


def movie_review_generator(movie_name):
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
            'p', class_='audience-reviews__review js-review-text').text.strip()
        audience_reviews.append(audience_quote)

    if critic_reviews and audience_reviews:
        st.subheader("Top 5 Critic Reviews")
        for idx, val in enumerate(critic_reviews):
            if idx == 5:
                break
            st.write(val)

        cr_score = ss.review_score(critic_reviews)
        ss.display_scores(cr_score)

        st.subheader("Top 5 Audience Reviews")
        for idx, val in enumerate(audience_reviews):
            if idx == 5:
                break
            st.write(val)

        aud_score = ss.review_score(audience_reviews)
        ss.display_scores(aud_score)

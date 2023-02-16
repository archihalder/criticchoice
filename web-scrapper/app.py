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
for i, cr in enumerate(cr_row):
    if i == 5:
        break
    review_text = cr.find('div', class_='review-text-container')
    quote = review_text.find('p', class_='review-text').text.strip()
    critic_reviews.append(quote)

ar_row = audience_soup.find_all('div', class_='review-text-container')
for j, ar in enumerate(ar_row):
    if j == 5:
        break
    audience_quote = ar.find(
        'p', class_='audience-reviews__review js-review-text clamp clamp-8 js-clamp').text.strip()
    audience_reviews.append(audience_quote)

# streamlit display
if critic_reviews and audience_reviews:
    st.subheader("Top Critic Reviews")
    for i in critic_reviews:
        st.write(i)

    st.subheader("Top Audience Reviews")
    for j in audience_reviews:
        st.write(j)

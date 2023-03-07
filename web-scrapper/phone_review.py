import streamlit as st
from bs4 import BeautifulSoup
import requests
import sentiment_score as ss
import url

st.markdown("<h1 style='text-align: center'> Phone Review Generator</h1>",
            unsafe_allow_html=True)
phone_brand = st.selectbox("Select the brand", ["Apple", "Samsung"])

model_name, model_id = [], []
for key, val in url.brands[phone_brand].items():
    if phone_brand == "Apple":
        model_name.append("iphone " + key)
    elif phone_brand == "Samsung":
        model_name.append("galaxy " + key)
    model_id.append(val)

model = st.selectbox("Select the model", model_name)

idx = 0
for i, v in enumerate(model_name):
    if v == model:
        idx = i

url_name = f"{phone_brand.lower()}-{'-'.join(model)}-price-in-india-{model_id[idx]}"

phone_review = requests.get(f"https://www.gadgets360.com/{url_name}/user-reviews").text
soup = BeautifulSoup(phone_review, 'lxml')

quote = []
all_reviews = soup.find_all('div', class_="_cmttxt _wwrap")
for review in all_reviews:
    quote.append(review.text.strip())

st.subheader("Top 5 reviews")
for idx, val in enumerate(quote):
    if idx == 5:
        break
    st.write(val)

phone_rating = ss.review_score(quote)
ss.display_scores(phone_rating)


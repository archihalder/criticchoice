import streamlit as st
from bs4 import BeautifulSoup
import requests
import sentiment_score as ss
import url


def phone_review_generator():
    st.markdown("<h1 style='text-align: center'> Phone Review Generator</h1>",
                unsafe_allow_html=True)
    phone_brand = st.selectbox("Brand Name: ", ["Select a brand", "Apple", "Samsung", "OnePlus", "Xiaomi", "Motorola"])

    if phone_brand == "Select a brand":
        pass
    else:
        model_name, model_id = [], []
        for key, val in url.brands[phone_brand].items():
            if phone_brand == "Apple":
                model_name.append("iphone " + key)
            elif phone_brand == "Samsung":
                model_name.append("galaxy " + key)
            elif phone_brand == "OnePlus":
                model_name.append("oneplus " + key)
            elif phone_brand == "Xiaomi":
                model_name.append(key)
            elif phone_brand == "Motorola":
                model_name.append("motorola " + key)
            model_id.append(val)

        model_name.insert(0, "Select a model")
        model = st.selectbox("Model Name: ", model_name)

        if model == "Select a model":
            pass
        else:
            idx = 0
            for i, v in enumerate(model_name):
                if v == model:
                    idx = i-1

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


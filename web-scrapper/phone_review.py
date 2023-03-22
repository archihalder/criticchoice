import streamlit as st
from bs4 import BeautifulSoup
import requests
import sentiment_score as ss
import url


def intro():
    res = []
    st.markdown("<h1 style='text-align: center'> Phone Review Generator</h1>", unsafe_allow_html=True)
    phone_brand = st.selectbox("Brand Name: ", ["Select a brand", "Apple", "Samsung", "OnePlus", "Xiaomi", "Motorola"])

    if phone_brand == "Select a brand":
        pass
    else:
        res.append(phone_brand)
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
            res.append(model)
            res.append(model_id)
            idx = 0
            for i, v in enumerate(model_name):
                if v == model:
                    idx = i - 1
            res.append(idx)

    if len(res) == 4:
        url_name = f"{res[0].lower()}-{'-'.join(res[1])}-price-in-india-{res[2][res[3]]}"
        return url_name


def phone_info(url_name):
    if url_name:
        st.subheader("Phone Info")
    html = requests.get(f"https://www.gadgets360.com/{url_name}#specs").text
    soup = BeautifulSoup(html, 'lxml')
    all_info = soup.find_all('div', class_='_pdsd')
    for info_data in all_info:
        title = info_data.find('span', class_='_ttl').text
        value = info_data.find('span', class_='_vltxt').text
        st.write(title, ':', value)


def phone_review_generator(url_name):
    phone_review = requests.get(f"https://www.gadgets360.com/{url_name}/user-reviews").text
    soup = BeautifulSoup(phone_review, 'lxml')

    quote = []
    all_reviews = soup.find_all('div', class_="_cmttxt _wwrap")
    for review in all_reviews:
        quote.append(review.text.strip())

    st.subheader("Top 5 reviews")
    for i, val in enumerate(quote):
        if i == 5:
            break
        st.write(val)

    phone_rating = ss.review_score(quote)
    ss.display_scores(phone_rating)

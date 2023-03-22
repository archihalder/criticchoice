import movie_review as mr
import phone_review as pr
import streamlit as st


st.sidebar.title("Choose the product")
product = st.sidebar.selectbox("Product Type", ["Select a product", "Movies", "Phones"])

if product == "Movies":
    mr.intro()
    mr.movie_info()
    mr.movie_review_generator()
elif product == "Phones":
    data = pr.intro()
    if data:
        pr.phone_info(data)
        pr.phone_review_generator(data)
else:
    st.markdown("<h1 style='text-align: center'> Product Buying Assistant </h1>", unsafe_allow_html=True)

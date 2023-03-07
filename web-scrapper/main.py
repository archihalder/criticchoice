import movie_review as mr
import phone_review as pr
import streamlit as st


st.sidebar.title("Choose the product")
product = st.sidebar.selectbox("Product Type", ["Select a product", "Movies", "Phones"])

if product == "Movies":
    mr.movie_review_generator()
elif product == "Phones":
    pr.phone_review_generator()
else:
    st.markdown("<h1 style='text-align: center'> Product Buying Assistant </h1>", unsafe_allow_html=True)
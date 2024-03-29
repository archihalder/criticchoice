import movie_review as mr
import phone_review as pr
import streamlit as st


st.sidebar.title("Choose the product")
product = st.sidebar.selectbox("Product Type", ["Select a product", "Movies", "Phones"])

if product == "Movies":
    name = mr.intro()
    if name:
        mr.movie_info(name)
        mr.movie_review_generator(name)
elif product == "Phones":
    data = pr.intro()
    if data:
        pr.phone_info(data)
        pr.phone_review_generator(data)
else:
    st.markdown("<h1 style='text-align: center'> CriticChoice </h1>", unsafe_allow_html=True)
    subheading = "A web-app which helps customers to buy products"
    st.write(f'<p style="text-align: center">{subheading}</p>', unsafe_allow_html=True)

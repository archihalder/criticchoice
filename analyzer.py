import streamlit as st
import pandas as pd
from collections import OrderedDict

data = [
    [0.863184, 0.863555, 0.863184, 0.863156, 0.227],
    [0.890749, 0.891775, 0.890749, 0.890685, 0.164],
    [0.497042, 0.497025, 0.497042, 0.497009, 3.093],
    [0.753807, 0.754090, 0.753807, 0.753753, 0.639],
    [0.836501, 0.845098, 0.836501, 0.835438, 1.191],
    [0.477281, 0.466603, 0.477281, 0.428799, 1.475],
    [0.882568, 0.886573, 0.882568, 0.882279, 1.590],
    [0.926875, 0.927327, 0.926875, 0.926852, 23.274]
]

row_names = ["Naive Bayes", "Fast Forward NN", "Simple RNN", "Single LSTM",
             "Stacked LSTM", "USE", "USE Refined", 
             "Hugging Face"]

def create_df(data:dict, col_idx:int):
    new_dict = OrderedDict()
    for i in range(len(data)):
        new_dict[row_names[i]] = data[i][col_idx]
    return new_dict

accuracy_data = create_df(data, 0)
precision_data = create_df(data, 1)
recall_data = create_df(data, 2)
f1_score = create_df(data, 3)
time_taken = create_df(data, 4)

st.title("Comparitive Analysis of Algorithms")

st.header("Accuracy")
st.bar_chart(accuracy_data)

st.header("Precision")
st.bar_chart(precision_data)

st.header("Recall")
st.bar_chart(recall_data)

st.header("F1 Score")
st.bar_chart(f1_score)

st.header("Time Taken (in milliseconds)")
st.bar_chart(time_taken)

st.header("Overall Observation")
st.write("If time is not a factor, Hugging Face model is best. Otherwise, Fast Forward Neural Network or the Refined USE can be used for fast results")
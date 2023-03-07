import streamlit as st
import pandas as pd
import plotly.express as px

data = {
    "Metrics": ["Accuracy", "Precision", "Recall", "F1 Score", "Time Taken"],
    "Naive Bayes": [0.863184, 0.863555, 0.863184, 0.863156, 0.227],
    "Fast Forward NN": [0.890749, 0.891775, 0.890749, 0.890685, 0.164],
    "Simple RNN": [0.497042, 0.497025, 0.497042, 0.497009, 3.093],
    "Single LSTM": [0.753807, 0.754090, 0.753807, 0.753753, 0.639],
    "Stacked LSTM": [0.836501, 0.845098, 0.836501, 0.835438, 1.191],
    "USE": [0.477281, 0.466603, 0.477281, 0.428799, 1.475],
    "USE Refined": [0.882568, 0.886573, 0.882568, 0.882279, 1.590],
    "Hugging Face": [0.926875, 0.927327, 0.926875, 0.926852, 23.274]
}

st.sidebar.title("Comparative Analysis of Algorithms")
metric = st.sidebar.radio("Metrics", ("All", "Accuracy", "Precision", "Recall", "F1 Score", "Time Taken"))

df = pd.DataFrame(data)
df = df.set_axis(df["Metrics"])
df = df.iloc[:, 1:]

if metric == "All":
    fig = px.line(df.iloc[:-1, :])
    st.plotly_chart(fig)
else:
    metric_col = data["Metrics"]
    for idx, val in enumerate(metric_col):
        if metric == val:
            fig = px.line(df.iloc[idx])
            st.plotly_chart(fig)
            break

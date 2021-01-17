import streamlit as st
import pickle
import pandas as pd

FILENAME = "best_classifier.pickle"

with open(FILENAME, "rb") as file:
    model = pickle.load(file)


def calc_progress(data):
    progress = 0
    columns = ["variance", "skewness", "curtosis", "entropy"]

    for column in columns:
        if data[column] != 0:
            progress = progress + 25

    return progress


def progress_bar(progress):
    st.write(f"Progress: {progress}")
    st.progress(progress)

@st.cache
def predict(data):
    input_data = pd.DataFrame([data], columns=['variance', 'skewness', 'curtosis', 'entropy'])
    return model.predict(input_data)[0]
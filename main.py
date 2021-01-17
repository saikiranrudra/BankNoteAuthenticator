import streamlit as st
from utils import calc_progress, progress_bar, predict
import sys

"""
    # 🌟 Bank Note Authenticator

    Authenticate bank note by filling the form Below

    ## Fill the detail about Note 💶
"""

variance = st.number_input("Enter Variance", -9999.0, 9999.9, 0.0)
skewness = st.number_input("Enter Skewbess", -9999.0, 9999.9, 0.0)
curtosis = st.number_input("Enter curtosis", -9999.0, 9999.9, 0.0)
entropy = st.number_input("Enter Entropy", -9999.0, 9999.9, 0.0)

progress = calc_progress({
    'variance': variance,
    'skewness': skewness,
    'curtosis': curtosis,
    'entropy': entropy
})

progress_bar(progress)

if progress == 100:
    st.success("👌 Now Click on PREDICT NOTE AUTHENTICITY")

if st.button("PREDICT NOTE AUTHENTICITY"):
    if variance == 0 or skewness == 0 or curtosis == 0 or entropy == 0:
        st.warning("Complete the Form First")
    else:
        output = predict([variance, skewness, curtosis, entropy])
        result = "Fake" if output == 0 else "Not Fake"

        if output == 1:
            st.success(f"## **Prediction** {result}")
        else:
            st.error(f"## Prediction **{result}**")

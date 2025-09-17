import streamlit as st
import joblib
import re

# Load model and vectorizer only once when app starts
model = joblib.load("../models/xgboost_phishing_model.pkl")
vectorizer = joblib.load("../models/tfidf_vectorizer.pkl")

def clean_url(url):
    url = url.lower()
    url = re.sub(r'https?://', '', url)
    url = re.sub(r'www\d*\.', '', url)
    url = re.sub(r'[^a-z0-9\-\.\/]', ' ', url)
    url = re.sub(r'\s+', ' ', url)
    return url.strip()

st.title("Phishing URL Detector")

url_input = st.text_input("Enter URL to check for phishing:")

if st.button("Check URL"):
    if url_input:
        cleaned_url = clean_url(url_input)
        features = vectorizer.transform([cleaned_url])
        prediction = model.predict(features)[0]
        if prediction == 0:
            label = "This is a Phishing URL"
            st.markdown(
                f'<div style="padding:10px; background-color:#ff4c4c; color:white; border-radius:5px;">Prediction: {label}</div>',
                unsafe_allow_html=True,
            )
        else:
            label = "This is a Legitimate URL"
            st.markdown(
                f'<div style="padding:10px; background-color:#4CAF50; color:white; border-radius:5px;">Prediction: {label}</div>',
                unsafe_allow_html=True,
            )
    else:
        st.warning("Please enter a valid URL.")

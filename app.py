
import streamlit as st
import openai
import pandas as pd
import yfinance as yf

# Set OpenAI API key using Streamlit secrets
openai.api_key = st.secrets["openai_api_key"]

def get_chatgpt_response(prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

st.title('Beast Trader - AI + Telegram Breakout Screener')

# User input for trade suggestions
trade_query = st.text_input("Enter your trade query:")
if st.button("Get Response"):
    response = get_chatgpt_response(trade_query)
    st.write(response)

# Example for stock analysis
if st.button("Get Stock Data for Nifty50"):
    nifty50_data = yf.download("^NSEI", start="2021-01-01", end="2021-12-31")
    st.write(nifty50_data.tail())


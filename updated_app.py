
import streamlit as st
import openai
import pandas as pd

# Set the OpenAI API key using Streamlit secrets
openai.api_key = st.secrets["openai_api_key"]

# Function to get response from ChatGPT
def get_chatgpt_response(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Use the latest available model
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"Error: {str(e)}"

# Streamlit UI
st.title("AI-Powered Trading Assistant")
st.write("Get analysis and suggestions for your trades.")

# Input for user trade query
trade_query = st.text_input("Enter your trade query:")
if st.button("Get Response"):
    if trade_query:
        result = get_chatgpt_response(trade_query)
        st.write(result)
    else:
        st.write("Please enter a query to get a response.")

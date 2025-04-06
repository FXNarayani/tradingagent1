
import openai
import streamlit as st

# Access the OpenAI API key securely from Streamlit secrets
openai.api_key = st.secrets["openai_api_key"]

# Example usage of OpenAI API
def get_chatgpt_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100
    )
    return response.choices[0].text.strip()

# Streamlit app layout
st.title("AI-Powered Trading Assistant")
st.write("Get analysis and suggestions for your trades.")
prompt = st.text_area("Enter your trade query:")

if st.button("Get Response"):
    if prompt:
        response = get_chatgpt_response(prompt)
        st.write(response)
    else:
        st.write("Please enter a query.")

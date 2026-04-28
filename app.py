import streamlit as st
import os
from openai import OpenAI

st.set_page_config(page_title="GenAI App", layout="centered") 

st.title("GenAI Assistant 🚀")

query = st.text_input("Ask anything:")

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY")) 

if query:
    with st.spinner("Thinking..."):
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": query}] 
        )
        st.success(response.choices[0].message.content)
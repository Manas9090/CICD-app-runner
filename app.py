import streamlit as st
import os
from openai import OpenAI

st.set_page_config(page_title="GenAI App", layout="centered")

st.title("GenAI Assistant 🚀")

# Load API Key
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    st.error("❌ OPENAI_API_KEY is not set. Please configure environment variable.")
    st.stop()

# Cache OpenAI client (important for performance)
@st.cache_resource
def get_client():
    return OpenAI(api_key=api_key)

client = get_client()

# Input box
query = st.text_input("Ask anything:")

if query and query.strip():
    try:
        with st.spinner("Thinking..."):
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": query}]
            )

        answer = response.choices[0].message.content

        st.markdown("### 🤖 Response")
        st.write(answer)

    except Exception as e:
        st.error(f"⚠️ Error: {str(e)}")
import streamlit as st
import os
import requests
from exa_py import Exa
from langchain_groq import ChatGroq

# Initialize API keys
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
EXA_API_KEY = os.getenv("EXA_API_KEY")

st.set_page_config(page_title="LLM Crypto Analysis Tool", page_icon="💰", layout="centered")

st.title("💰 LLM-Powered Crypto Analysis Tool")
st.write("Analyze cryptocurrency trends and sentiment using LLaMA 3 + Groq API.")

query = st.text_input("Enter your crypto-related query:", "Summarize Bitcoin market news this week")

if st.button("Analyze"):
    if not (GROQ_API_KEY and EXA_API_KEY):
        st.error("Please set your GROQ_API_KEY and EXA_API_KEY environment variables.")
    else:
        exa = Exa(api_key=EXA_API_KEY)
        result = exa.search_and_contents(query, summary=True)
        if result.results:
            st.subheader("📰 Latest News Headlines:")
            for item in result.results[:5]:
                st.markdown(f"**{item.title}** - [{item.url}]({item.url})")

        st.subheader("🧠 LLM Analysis:")
        llm = ChatGroq(model="llama3-70b-8192", api_key=GROQ_API_KEY)
        summary = llm.invoke(f"Provide a summary and market insight on: {query}")
        st.write(summary)

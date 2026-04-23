from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

st.header("Research Tool")

user_input = st.text_input("Enter your research question here")

if st.button("Search"):
    if user_input:
        llm = ChatOpenAI(model="gpt-3.5-turbo")
        result = llm.invoke(user_input)

        st.write(result.content)
    else:
        st.warning("Please enter a question first")
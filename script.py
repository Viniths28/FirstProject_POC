import streamlit as st
st.set_page_config(page_title="Ask a Question about disasterWise Website", page_icon= ":-)")
st.title("Ask Question")

with st.sidebar:
    st.header("Settings")
    website_url = st.text_input("Enter the URL")

def get_response(user_input):
    return "I don't know"


user_query = st.chat_input("Type Yor Questions here...")
if user_query is not None and user_query !="":
    response = get_response(user_query)
    with st.chat_message("Human"):
        st.write(user_query)
    with st.chat_message("AI"):
        st.write(response)

         
  
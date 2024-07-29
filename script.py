import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage
from langchain_community.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from dotenv import load_dotenv


def get_vectorstore_from_url(url):
    loader = WebBaseLoader(url)         
    document = loader.load()
    text_splitter = RecursiveCharacterTextSplitter()
    document_chunks = text_splitter.split_documents(document)

    vector_store = chroma.from_documents(document_chunks,OpenAIEmbeddings())


    return document_chunks





    return document

st.set_page_config(page_title="Ask a Question about disasterWise Website", page_icon= ":-)")
st.title("Ask Question")
    
def get_response(user_input):
    return "I don't know"

if "chat_history" not in st.session_state:
    st.session_state.chat_history=[
            AIMessage(content="Hello, I am a bot. How can I help you?"),
        ]



with st.sidebar:
    st.header("Settings")
    website_url = st.text_input("Enter the URL")

if website_url is None or website_url == "":
    st.info("Please enter a website URL")

else:
    chunks = get_vectorstore_from_url(website_url)
    with st.sidebar:
        st.write(chunks)


    user_query = st.chat_input("Type Yor Questions here...")
    if user_query is not None and user_query !="":
        response = get_response(user_query)
        st.session_state.chat_history.append(HumanMessage(content=user_query))
        st.session_state.chat_history.append(AIMessage(content= response))
    
    
    for message in st.session_state.chat_history:
        if isinstance(message, AIMessage):
            with st.chat_message("AI"):
                st.write(message.content)
        elif isinstance(message, HumanMessage):
            with st.chat_message("Human"):
                st.write(message.content)




          

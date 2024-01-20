import streamlit as st
import os
import google.generativeai as genai

st.title('Intern-Bot')

os.environ['GOOGLE_API_KEY']='AIzaSyDlXJiqbFWXpM2Y2rimIbqGrykfIxzFtpQ'
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])


model=genai.GenerativeModel('gemini-pro')


if "messages" not in st.session_state:
    st.session_state.messages=[
        {
            "role":"Internship-Bot",
            "content":"Ask me anything related to Internships."
        }
    ]


# Displaying chat messages
for message in st.session_state.messages:
    with st.chat_message(message['role']):
        st.markdown(message['content'])


def process(query):
    flag=0
    
    response=model.generate_content(f"As an Internship Bot, {query} ")
    rel_response=response.text


    if model.generate_content(f"Is {rel_response} query related to Internships? State answer in one word, yes or no?").text.lower() == "yes": 
        with st.chat_message("Internship-Bot"):
            st.markdown(response.text)
    else:
        flag=1
        with st.chat_message("Internship-Bot"):
            st.markdown("Sorry, your query is not related to internships.")
            

    st.session_state.messages.append({
        "role":"user",
        "content":query
    })
    
    if(flag == 0):
        st.session_state.messages.append(
            {
                "role":"Internship-Bot",
                "content": response.text
            }
        )
    else:
        st.session_state.messages.append(
            {
                "role":"Internship-Bot",
                "content": "Sorry, your query is not related to internships."
            }
        )
        

query=st.chat_input("Ask me anything related to Internships.")

if query:
    with st.chat_message("user"):
        st.markdown(query)
    process(query)
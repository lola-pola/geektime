from streamlit_chat import message
import streamlit as st
import openai
import os
import json

results = {"questions": 224, "answers": 145}



def json_loader(loc='agenda.json'):
    json_file = open(loc)
    return json.load(json_file)


def generate_gpt_chat(prompt,model='dev03',max_tokens=4000):
    bot_context = f"you are geektime event agent ,event date is 12.6.23 in pavilion 10 expo tel aviv,this is event json agenda:{json_loader()}. \
        you are friendly and concise. \
        you only provide factual answers to queries, and do not provide answers that are not related to geekime event ."

    response = openai.ChatCompletion.create(
        engine="dev03",
        messages=[{"role":"system","content":bot_context},{"role":"user","content":prompt}],
        temperature=1,
        max_tokens=max_tokens,
        top_p=0.95,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None
    )
    return str(response['choices'][0]['message']['content'])




# Set up OpenAI API key
openai.api_type = "azure"
openai.api_base = "https://aks-production.openai.azure.com/"
# openai.api_base=  "https://biotest123.openai.azure.com/"
openai.api_version = "2023-03-15-preview"
openai.api_key = os.getenv("KEY_AZURE_AI")
data = {"questions": 0, "answers": 0}


st.set_page_config(page_title="Geektime Event Chatbot", page_icon=":robot_face:")
st.title("Geektime Event Chatbot Test !")
# with st.sidebar.title("Geektime Event Chatbot"):
#     if st.checkbox("Show Agenda"):
#         st.table(json_loader(loc='agenda.json'))
#     if st.checkbox("Show Results"):
#         st.bar_chart(results)

st.markdown("This is a chatbot that can answer questions about the event agenda")






results["questions"] += 1
results["answers"] += 2


st.session_state['generated'] = []
st.session_state['past'] = []

if 'generated' not in st.session_state:
    st.session_state['generated'] = []
if 'past' not in st.session_state:
    st.session_state['past'] = []
    
    
    

user_input=st.text_input("You:",key='input')
if user_input:
    output=generate_gpt_chat(prompt=user_input)
    st.session_state['past'].append(user_input)
    st.session_state['generated'].append(output)
if st.session_state['generated']:
    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state["generated"][i], key=str(i))
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user') 
        st.session_state.generated = ''
        


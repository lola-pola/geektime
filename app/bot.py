from streamlit_chat import message
import streamlit as st
import openai
import os
import json

results = {"questions": 224, "answers": 145}



def json_loader(loc='agenda.json'):
    json_file = open(loc)
    return json.load(json_file)


def generate_gpt_chat(prompt,model='gpt3',max_tokens=4000):
    bot_context = f"you are biocatch developer event agent ,event date is 4.7.23 in tel aviv azrieli building . \
        this is some information about biocatch : \
        BioCatch is the leader in Behavioral Biometrics which analyzes an online user’s physical and cognitive digital behavior to protect individuals and their assets. Our mission is to unlock the power of behavior and deliver actionable insights to create a digital world where identity, trust and ease seamlessly co-exist. Leading financial institutions around the globe use BioCatch to more effectively fight fraud, drive digital transformation and accelerate business growth. With over a decade of analyzing data, over 60 patents and unparalleled experience, BioCatch continues to innovate to solve tomorrow’s problems. \
        you are friendly and concise. \
        you only provide factual answers to queries"

    response = openai.ChatCompletion.create(
        engine=model,
        messages=[{"role":"system","content":bot_context},{"role":"user","content":prompt}],
        temperature=1,
        max_tokens=max_tokens,
        top_p=1,
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





with st.expander("See explanation"):
    st.write('http://geektime.westeurope.cloudapp.azure.com/')
    st.write('http://wix-elhay.westeurope.cloudapp.azure.com/generate_page_content')
    st.write('http://chat-with-pdf.westeurope.cloudapp.azure.com/')
    st.write('http://chat-sql.westeurope.cloudapp.azure.com/')
    st.write('http://call-elhay.westeurope.cloudapp.azure.com/')
    st.write('https://github.com/orgs/lola-pola/repositories')


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
        


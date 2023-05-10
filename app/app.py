from streamlit_chat import message
import streamlit as st
import openai
import os






# Set up OpenAI API key
openai.api_type = "azure"
openai.api_base = "https://aks-production.openai.azure.com/"
openai.api_version = "2022-12-01"
openai.api_key = os.getenv("KEY_AZURE_AI")


global_user_context = {"content": []}




def generate_gpt_chat(prompt,model='gpeta',max_tokens=4000,temperature=0.5):
    context_for_yoni= "you are a walkme CEO you name is boti"
    response = openai.Completion.create(
        engine=model,
        prompt=str(context_for_yoni)+prompt,
        temperature=temperature,
        max_tokens=max_tokens
    )
    print(response)
    return response.choices[0].text


def chat():
    model = st.text_input("select model",key='model')
    max_tokens = st.slider('max tokens',100,4000)
    temperature = st.slider('temperature',0.0,1.0)
    
    
    prompt_conf = st.checkbox('prompt configuration')
    if prompt_conf:
        st.success('prompt configuration saved')        
        if 'generated' not in st.session_state:
            st.session_state['generated'] = []
        if 'past' not in st.session_state:
            st.session_state['past'] = []
        user_input=st.text_input("You:",key='input')
        if user_input:
            # output=generate_gpt_chat(user_input)
            output=generate_gpt_chat(prompt=user_input,model=model,max_tokens=max_tokens,temperature=temperature)
            global_user_context["content"].append(user_input)
            #store the output
            st.session_state['past'].append(user_input)
            st.session_state['generated'].append(output)
        if st.session_state['generated']:
            for i in range(len(st.session_state['generated'])-1, -1, -1):
                message(st.session_state["generated"][i], key=str(i))
                message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')     


if starter: 
    chat()

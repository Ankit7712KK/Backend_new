import streamlit as st
import cohere
from dotenv import dotenv_values

# cred = dotenv_values('sec.env')
# API = cred['COHERE_API_KEY']
# def hello():
#     print(".................")
#     sugst1 = prmpt + "Generate in 100 words"
#     response = co.generate(
#         model='e6366bc6-735b-4654-a319-5d4dd1fea947-ft',
#         prompt=sugst1,
#         max_tokens=100)
#
#    st.write('Prediction: {}'.format(response.generations[0].text))

# st.header("Generative AI for Indian Constitution :")
# st.divider()
prmpt = st.chat_input("Enter your prompt")
def head():
    st.header("Generative AI for Indian Constitution :")
    st.divider()


def gen(prmpt):
    if prmpt is not None and "Generate in 100 words" in prmpt:
        print(prmpt)
        head()
        co = cohere.Client('sDeY1e2YtCt3XOdGOxZgDecF2H9I108rwdLy6Emw')

        response = co.generate(
            model='e6366bc6-735b-4654-a319-5d4dd1fea947-ft',
            prompt=prmpt,
            max_tokens=300)
        st.write('Prediction: {}'.format(response.generations[0].text))
    elif prmpt is not None and "Generate in 100 words" in prmpt:
        pass
    elif prmpt is not None and " Generate in 100 words" not in prmpt:
        print("First time; ",prmpt)
        head()
        co = cohere.Client('sDeY1e2YtCt3XOdGOxZgDecF2H9I108rwdLy6Emw')

        response = co.generate(
          model='e6366bc6-735b-4654-a319-5d4dd1fea947-ft',
          prompt=prmpt,
          max_tokens=300)
        st.write('Prediction: {}'.format(response.generations[0].text))


    else:
        if prmpt is not None and "Generate in 100 words" in prmpt:

            st.info("Start_typing_your_query_")
        else:

            head()
            st.info("Start_typing_your_query_")


gen(prmpt)
def hello():
    k=0
    gen(prmpt+" Generate in 100 words")

with st.sidebar:
    st.header("Generate content more precisely",divider="blue")
    st.button(label="Generate in 100 words",on_click=hello)
    st.button(label="Elaborate article more")
    st.button(label="Show article in points")
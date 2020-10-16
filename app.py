import stanza
import streamlit as st


def get_model(lang, processors=None):
    nlp = stanza.Pipeline(lang, processors)
    return nlp


lang = "de"
nlp = get_model(lang)
text = st.text_area("Input")

st.write(nlp(text).to_dict())

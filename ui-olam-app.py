import streamlit as st
from app_core import App

st.set_page_config(page_title="F5 AI Troubleshooter - Ollama", page_icon="🤖")
st.title("🤖 F5 AI Troubleshooter - Ollama Mode")

user_input = st.text_area("Describe the network issue:", height=150)

app = App(config_file='config.json', use_ollama=True)

model_name = st.selectbox("Select AI Model", app.model_selector.available_models)

if st.button("Run AI Analysis"):
    if not user_input.strip():
        st.warning("Please enter a network issue description.")
    else:
        with st.spinner("Analyzing with Ollama..."):
            result = app.run(user_input, model_name)

        if "error" in result:
            st.error(result["error"])
        else:
            st.subheader("🤖 AI Response")
            st.text(result["ai_output"])

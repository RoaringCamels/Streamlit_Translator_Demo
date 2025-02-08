import streamlit as st
import openai

# Load API Key securely from Streamlit secrets
openai.api_key = st.secrets["openai"]["api_key"]

# Streamlit App Title
st.title("Translator 9000 🌍")

# Language Selection
input_language = st.selectbox("Select Input Language:", ["Spanish", "English"])
output_language = st.selectbox("Select Output Language:", ["Mandarin", "French", "Japanese"])

# Text Input
input_text = st.text_area(f"Enter text in {input_language}:", "")

# Translation Function
def translate_text(input_lang, output_lang, text):
    if not text.strip():
        return "⚠️ Please enter some text to translate."

    system_prompt = """
    You are a language translator. A user will give you an input language, an output
    language, and the text they want translated. Output ONLY their translated message.
    """

    user_prompt = f"{input_lang} -> {output_lang}, my message is: {text}"

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0125",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ]
        )
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        return f"🚨 Error: {e}"

# Translate Button
if st.button("Translate"):
    translation = translate_text(input_language, output_language, input_text)
    st.subheader("Translation:")
    st.success(translation)

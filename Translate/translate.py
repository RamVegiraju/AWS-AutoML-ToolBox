import boto3
import streamlit as st


st.title("AWS Translate Example")

sampText = st.text_input('Enter input text')
inpLang = st.selectbox('Input Language',
                    ('en', 'es'))
outLang = st.selectbox('Output Language',
                    ('en', 'es'))

#Using boto3 to call the Translate API
client = boto3.client('translate', region_name = "us-east-1")
response = client.translate_text(Text = sampText,
                                SourceLanguageCode = inpLang,
                                TargetLanguageCode = outLang)

output = response['TranslatedText']
st.write(output)
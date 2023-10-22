
import streamlit as st
import speech_recognition as sr
import os
import io
from PIL import Image
import openai
import io
st.title("Generate AI image using  Audio or Text ")
recording = False
record_option = st.radio('Record option', ['5 seconds', '10 seconds'])
#select_model = st.radio("open ai dall e" , ["DALLE","Stable"])
if st.button("Record"):
  if recording:
    recording = False
    st.write("Recording stopped")
  else:
    recording = True
    r = sr.Recognizer()
    with sr.Microphone() as source:
      if record_option == '5 seconds':
        seconds = 5
      elif record_option == '10 seconds':
        seconds = 10
    
      st.write("Recording...")
      audio_data = r.record(source, duration=seconds)
      st.write("Recognizing...")
      text = r.recognize_google(audio_data)
      st.write(text)
      openai.api_key = 'type here your open ai api key '
      response = openai.Image.create(prompt=text)
      st.image(response['data'][0]['url'])
prompt_manual = st.text_input("Enter a prompt manually")

if st.button("Generate"):
  openai.api_key = 'type here your open ai api key'
  response = openai.Image.create(prompt=prompt_manual)

  st.image(response['data'][0]['url'])
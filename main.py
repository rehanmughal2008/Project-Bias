import streamlit as st
import google.generativeai as genai
import requests as rs
from bs4 import BeautifulSoup 

#gemini config
genai.configure(api_key="AIzaSyCMc_G9mjk9jH7UwkquYq2-GkN5nwhdHwk")
model = genai.GenerativeModel("gemini-1.5-flash")

#Page Config
st.set_page_config(
    page_title="Project Bias"
)
st.title('Project Bias')
GLOBAL_HEIGHT = 300

#global functions
def extract_text(link):
      page = rs.get(link)
      soup = BeautifulSoup(page.content, 'html.parser')
      page_text = soup.body
      return str(page_text)

#placeholder JSON
class response:
      text=""

class percent_bias:
      text=""

col1, col2 = st.columns(2)

with col1:
    inputted_text = st.text_area('Paste Segment Here', "", height=GLOBAL_HEIGHT)


#making button process bias
if st.button("Check Bias", use_container_width=True):
    with st.spinner(text="Proccessing Bias..."):
                response = model.generate_content("Check the political bias (left or right) of the following text citing specific points. Keep it simple: " + inputted_text)
                percent_bias = model.generate_content("Off of the following text, give me just a percent of how biased it is. No extra words. if no text available say '-': " + inputted_text)
                st.metric("BIAS", f"{percent_bias.text}")
                print(percent_bias.text)
with col2:
    outputted_text = st.text_area('Bias:', response.text, disabled=True, height=GLOBAL_HEIGHT)
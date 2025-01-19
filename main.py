import streamlit as st
import google.generativeai as genai

#gemini config
genai.configure(api_key="AIzaSyCMc_G9mjk9jH7UwkquYq2-GkN5nwhdHwk")
model = genai.GenerativeModel("gemini-1.5-flash")

#Page Config
st.set_page_config(
    page_title="Project Bias"
)
st.title('Project Bias')
GLOBAL_HEIGHT = 300

#placeholder JSON
class response:
      text=""

class percent_bias:
      text=""

col1, col2 = st.columns(2)

#default slider value
slider_value = 50

with col1:
    inputted_text = st.text_area('Paste Segment Here', None, height=GLOBAL_HEIGHT)


#making button process bias
if st.button("Check Bias", use_container_width=True):
    if inputted_text is None:
         st.warning("input text")
    else:     
        with st.spinner(text="Proccessing Bias..."):
            response = model.generate_content("Check the political bias, (left or right) or other, of the following text citing specific points. Keep it simple: " + inputted_text)
            percent_bias = model.generate_content("Off of the following text, give me just a percent of how biased it is (left=0-40),(neutral=41-59),(right=60-100) without the percent symbol. No extra words. if no text available say '50': " + inputted_text)
            slider_value = int(f"{percent_bias.text}")
            slider = st.slider("BIAS (%)", 0, 100, slider_value or 0, disabled=True, key=10)
            print(percent_bias.text)
with col2:
    outputted_text = st.text_area('Bias:', response.text, disabled=True, height=GLOBAL_HEIGHT)

if slider_value <=40:
    st.html("""
        <style>
            .stMain {
            background-color: #43A0CE
            }
            *{
            color: white
            }
        </style>
    """)
elif slider_value <=59:
    st.html("""
        <style>
            .stMain {
            background-image:url("https://wallpapercave.com/wp/wp9157973.jpg");
            background-size: contain;
            opacity: 0.9
            }
            *{
            color: white
            }
        </style>
    """)
elif slider_value <=100:
    st.html("""
        <style>
            .stMain {
            background-color: #E55955 
            }
            *{
            color: white
            }
        </style>
    """)
else:
     pass
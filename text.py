import streamlit as st 
from PIL import Image
import base64
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('awesome-gif.gif')    

st.title("A Beautiful Title")
st.header("Article header")
st.subheader("Good looking sub-header")
st.write("Writing simple text, option-1")
st.text("Writing simple text, option-2")
st.markdown(" **This is a markdown style text** ")
st.info('Check out the next article on creating widgets')
st.latex('\sum a+b')
st.success('Success!')
st.error("Sorry, fix the bug!")
st.warning("Are you sure you want to run this code?")
"""
* You can also write texts within tripple quotes. 
* It's probably a good option for writing long paragraphs
"""
myCode = '''def myFunc():
    print("This is a function") '''
st.code(myCode)

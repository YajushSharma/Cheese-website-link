from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="My Webpage", page_icon=":cheese_wedge:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# LOAD ASSETS
lottie_coading = load_lottieurl ("https://assets1.lottiefiles.com/private_files/lf30_C6JlMx.json")
img_contact_form = Image.open("C:\Python practice\website\Images/203511ffdc10b3d42590ba339ebad343.jpg")
img_cheese_hehe = Image.open("C:\Python practice\website\Images/Cherry hehee.png")
# HEADER SECTION
with st.container():
    st.subheader("Hi, I am mouse :mouse:")
    st.title("A Cheese's mouse :mouse: ")
    st.write("I am passionate about my cute cheese")

# what I DO
with st.container():
    st.write("___")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Poem for cheese")
        st.write("##")
        st.write(
            '''
            Roses are red:rose:
            Voilets are blue:blue_heart:
            Cheese I Love You:cheese_wedge:
            '''
        )
        st.write("[Only cheese can click this :pleading_face:](https://sites.google.com/view/my-cheese/home)")
    with right_column:
        st.lottie(lottie_coading, height=300, key="coding")

#PROJECTS
with st.container():
    st.write("___")
    st.header("Video for cheese :heart:")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_cheese_hehe)
    with text_column:
        st.subheader("For cheese :pleading_face:")





        st.markdown("[Cheese Click on this:pleading_face:](https://www.youtube.com/watch?v=DkSBQlatxss&ab_channel=RazexEdits)")

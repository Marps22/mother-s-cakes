from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="Sweet Home Bakes", page_icon=":🍰:", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use Local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("C:/Users/ASUS/Desktop/style/Stylecodes.txt")

# --- LOAD ASSETS ---
lottie_coding = load_lottieurl("https://lottie.host/0a93c91a-9514-4eeb-8c15-d4c9c626ae51/PcWSOf1Kjl.json")
img_contact_form = Image.open("C:/Users/ASUS/Desktop/images/cake_one.jpg")
img_lottie_animation = Image.open("C:/Users/ASUS/Desktop/images/cake_two.png.jpg")
img_cake_yum = Image.open("C:/Users/ASUS/Desktop/images/cake_two.jpg")
img_cake_sarap = Image.open("C:/Users/ASUS/Desktop/images/cake_five.jpg")
img_cake_delicious = Image.open("C:/Users/ASUS/Desktop/images/cakes_four.jpg")
img_cake_number = Image.open("C:/Users/ASUS/Desktop/images/number_cake.jpg")
img_cupcake_valentines = Image.open("C:/Users/ASUS/Desktop/images/valentines_cupcakes.jpg")

# --- HEADER SECTION ---
with st.container():
    st.subheader("Hello!:wave:, I am Marfy Baccay and Welcome to...")
    st.title("SWEET HOME BAKES")
    st.write("where I showcase my mother's very beautiful, delicious, and mouthwatering cakes.")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Introduction 👩‍🍳")
        st.write("##")
        st.write(
            """
            My name is Jan Marfy S. Baccay but everyone calls me Marfy. I am a grade 10 student from Canlubang
            Christian School, learning the skills of coding. I have created this page in order to enhance my 
            skills in coding, as part of my education, and most importantly is to present my mother's small cake 
            business to the world. I hope for everyone to support her and for those who already did, thank you
            and may you continue to do so.
            
            My mother's name is Mary Jane Baccay, a loving wife and a caring mother to two children. She started
            her small business at the end of the covid pandemic. Life was truly tough during those times and her
            business was very helpful for the family. She started by herself, teaching herself through online 
            methods. She was very hardworking, taking good care of the family while perfecting her craft, she does 
            not just bake but she also sews beautiful and good quality clothes, bedsheets, curtains, and many more.
            A very talented individual indeed.   
            
            If this sounds interesting to you, consider liking her page and contacting her for more information. 
            Thankyou and God bless"""

        )
        st.write("[Facebook page (Sweets Home Bake) >](https://www.facebook.com/profile.php?id=100063972998325)")
        st.write("[Her Personal Account >](https://www.facebook.com/maryjane.stabarbarabaccay)")
    with right_column:
        st_lottie(lottie_coding, height=500, key="coding")


# --- PROJECTS ---
with st.container():
    st.write("---")
    st.header("Home Baked Cakes")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contact_form)
    with text_column:
        st.subheader("Chocomoist Drip Cake")

with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_lottie_animation)
    with text_column:
        st.subheader("Chocomoist Drip Cake (customized)")

with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_cake_yum)
    with text_column:
        st.subheader("Ube Cheesecake")

with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_cake_sarap)
    with text_column:
        st.subheader("Vanilla cake with Caramel Filling")

with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_cake_delicious)
    with text_column:
        st.subheader("Mango Cake (left)"
                     "Red Velvet Cake (middle)"
                     "Chocomoist Cake (right)")

with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_cake_number)
    with text_column:
        st.subheader("Number Cake")

with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_cupcake_valentines)
    with text_column:
        st.subheader("Valentines Cupcakes")

with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
        st.write("For more information, please check out my page.")

# --- CONTACT ---
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    contact_form = """
    <form action="https:// form submit.co/jmarbaccay28@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder= "Your name" required>
        <input type="email" name="email" placeholder= "Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.title("THANK YOU AND HAVE A GOOD DAY!")

import streamlit as st
from random import choice
import string



def password_generator(lenght,use_number,use_special_charactors):
    create_password=string.ascii_letters
    if use_number:
        create_password +=string.digits
    if use_special_charactors:
        create_password +=string.punctuation
    return "".join(choice(create_password) for _ in range(lenght))


st.title("Welcome To Password Generator App In Python  🐍🎡")

lenght=st.slider("Select Your lenght",min_value=8,max_value=35, value=15 )

use_number=st.checkbox("Make Stronge Password to use Digits 🔐")
use_special_charactors=st.checkbox("Make Stronge Password to use Special Charactor 🔐")

if st.button("Generate your Password"):
    genereted_password=password_generator(lenght,use_number,use_special_charactors)
    st.subheader(f"Your Generated Password = ' { genereted_password } '")
    
    
st.write("---------------------------------------------------------------------------------------------------------------------------------------") 

st.header("Build By 💖 Muhammad Owais Shah ")
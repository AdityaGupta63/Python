import streamlit as st
import pandas as pd

hide_st_style = """
     <style>
     #MainMenu {visibility: hidden;}
     footer {visibility: hidden;}
     # header {visibility: hidden;}
     </style
"""
st.markdown(hide_st_style, unsafe_allow_html=True)

st.title('Aditya Gupta Web-App')
st.title(' ')

st.subheader('Please fill this form to continue further process...')

user_fname = st.text_input('Enter Your first name here : ')
user_lname = st.text_input('Enter Your last name here : ')
user_email = st.text_input('Enter Your E-Mail ID here : ')
user_gender = st.selectbox('Enter Your Gender here : ',('Male','Female','Not to tell'))
user_DOB = st.date_input('Enter Your birth date here : ')

honorifics = ['MR.', 'MRs.','']
honor = ()

if user_gender == 'Male':
     honor = honorifics[0]
elif user_gender == 'Female':
     honor = honorifics[-2]
elif user_gender == 'Not to tell':
     honor = honorifics[-1]
else:
     pass

btn = st.button('Submit')

if btn:
     st.markdown(f'Hello {honor} {user_fname}. We recieve your form and now we can able to track your good vibes here in our page. If we had any query so we can mail you at {user_email}.')
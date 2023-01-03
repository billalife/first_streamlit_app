import streamlit as st
import pandas as pd

st.title('My Mom\'s New Healthy Diner') #special characters handling are to done with '\'

st.header(":red[Breakfast Favourites]")

st.text('🍜 Omega 3 & blueberry Oat meals')

st.text('🥣 Kale, Spinach & Rocket Smoothie')
        
st.text('🐔 Hard-Boiled and Free Range Eggs')        

st.text('🥑 Avacado Toast')

st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')



my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

st.dataframe(my_fruit_list)  ##streamlit library to display it on the page by typin

my_fruit_list = my_fruit_list.set_index('Fruit')  #setting index on the basis of fruits

st.multiselect('Pick some fruits:', list(my_fruit_list.index))  #adding a multi selector on the basis of indexing in the DF

st.dataframe(my_fruit_list)  #add

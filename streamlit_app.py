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

fruits_selected = st.multiselect('Pick some fruits:', list(my_fruit_list.index), ['Avocado','Strawberries'])  #adding a multi selector on the basis of indexing in the DF

#We'll ask our app to put the list of selected fruits into a variable called fruits_selected. 
#Then, we'll ask our app to use the fruits in our fruits_selected list to pull rows from the full data set (and assign that data to a variable called fruits_to_show).
#Finally, we'll ask the app to use the data in fruits_to_show in the dataframe it displays on the page. 

fruits_to_show = my_fruit_list.loc[fruits_selected] 


st.dataframe(fruits_to_show)  #Display a dataframe as an interactive table.

#new section to display fruitwise api response
st.header("Fruityvice Fruit Advice!") #adding header

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
st.text(fruityvice_response.json())

import streamlit as st
import pandas as pd
import snowflake.connector 

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

fruit_choice = st.text_input('What fruit would you like information about?','Kiwi')
st.write('The user entered ', fruit_choice)


import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")


#Normalize semi-structured JSON data into a flat table. 
fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
#Display a dataframe as an interactive table.
st.dataframe(fruityvice_normalized)

#sending message from snowflake i.e checking if the connection works
my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
my_data_rows = my_cur.fetchall() #fetches all records from fruit_load_list table 
st.text("The fruit load list contains:")
st.text(my_data_rows)

#adding new box for the user to pick fruits, Allow the end user to add fruit 

add_my_fruit = st.text_input('What fruit would you like add?','Jackfruit')
st.write('The user entered ', add_my_fruit)
st.text("Thanks for adding" add_my_fruit)

import streamlit as st
import pandas as pd
import requests
import snowflake.connector 
from urllib.error import URLError

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

##new section to display fruitwise api response
#st.header("Fruityvice Fruit Advice!") #adding header
#fruit_choice = st.text_input('What fruit would you like information about?','Kiwi')
#st.write('The user entered ', fruit_choice)

#fruityvice_response = requests.get("https://fruityvice.com/api/fruit")


##Normalize semi-structured JSON data into a flat table. 
#fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
#Display a dataframe as an interactive table.
#st.dataframe(fruityvice_normalized)

#making an if else statement to display frutiyvice api response (from line 41 to 52)
#st.header("Fruityvice Fruit Advice!") #adding header
#try:
#        fruit_choice = st.text_input('What fruit would you like information about?')
#        if not fruit_choice:
#                st.error("Please select a fruit to get information")
#        else:
#                fruityvice_response = requests.get("https://fruityvice.com/api/fruit" + fruit_choice)
#                fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
#                st.dataframe(fruityvice_normalized)
#except URLError as e:
#        st.error()

#MAKING A FUNCTION which move several lines of code into a little group of code called a function, repeatable block of code (function)
def get_fruityvice_data(this_fruit_choice):
        fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice) 
        fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
        return (fruityvice_normalized)
st.header("Fruityvice Fruit Advice!")
try:
        fruit_choice = st.text_input('What fruit would you like information about?')
        if not fruit_choice:
                st.error("Please select a fruit to get information")
        else:
                back_from_function = get_fruityvice_data(fruit_choice)
                st.dataframe(back_from_function)
except URLError as e:
        st.error()
#dont run anything post this point or troublshooting 
#st.stop()

#sending message from snowflake i.e checking if the connection works, from here to line 88 got changed into a function
#my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
#my_cur = my_cnx.cursor()
#my_cur.execute("SELECT * from fruit_load_list")
#my_data_rows = my_cur.fetchall() #fetches all records from fruit_load_list table 
#st.text("The fruit load list contains:")
#st.text(my_data_rows)


#st.header("The fruit load list contains:")
#Snowflake-related function
#def get_fruit_list():
 #       with my_cnx.cursor() as my_cur:
#                my_cur.execute("SELECT * from fruit_load_list")
#                return my_cur.fetchall()  #fetches all records from fruit_load_list table
#add a button to load the fruit                
#if st.button('Get Fruit load list'):
#        my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
#        my_data_rows = get_fruit_list()
#        st.dataframe(my_data_rows)        

#adding new box for the user to pick fruits, Allow the end user to add fruit 
#add_my_fruit = st.text_input('What fruit would you like add?','Jackfruit')
#st.write("Thanks for adding ", add_my_fruit)

#Understanding Control flow 
#my_cur.execute( "insert into pc_rivery_db.public.fruit_load_list values ('from st')") 

#Adding a new function for the final block to select fruits
#def get_fruit_load_list(new_fruit):
#        with my_cnx.cursor() as my_cur:
#                my_cur.execute( "insert into pc_rivery_db.public.fruit_load_list values ('" "')")
#                return "Thanks for adding " + new_fruit
#add_my_fruit = st.text_input('What fruit would you like add?')
# st.header("The fruit load list contains:")
#if st.button('Get Fruit list'):
#        my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
#        my_data_rows = get_fruit_load_list()
#        my_cnx.close()   
#        st.dataframe(my_data_rows)       
        
 #################################################################ignore all the fucntions which were made earlier##################################################


st.header("The fruit load list contains:")
#snowflake related function
def get_fruit_load_list():
        with my_cnx.cursor() as my_cur:
                my_cur.execute("select * from fruit_load_list ")  #here the value passed will serve as the parameter for the funtion
                return my_cur.fetchall()
        
#add button to load the fruit 
if st.button('Get fruit load list'):
        my_cnx= snowflake.connector.connect(**st.secrets["snowflake"])
        my_data_rows = get_fruit_load_list()
        st.dataframe(my_data_rows)

# Use a Function and Button to Add the Fruit Name Submissions
def insert_row_snowflake(new_fruit):
        with my_cnx.cursor() as my_cur:
                my_cur.execute( "insert into pc_rivery_db.public.fruit_load_list values ('from st')")
                return "Thanks for adding " + new_fruit
add_my_fruit = st.text_input('What fruit would you like add?')
if st.button('Add a fruit to the list'):
        my_cnx= snowflake.connector.connect(**st.secrets["snowflake"])
        back_from_function = insert_row_snowflake()
        st.text(back_from_function)
        st.write("Thanks for adding ", my_cur)

        




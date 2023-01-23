import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title('My Parents New Healthy Diner')
streamlit.header('Breakfast Favourites')
streamlit.text('🍎🍇Omega 3 & Blueberry Oatmeal🍍🍞')
streamlit.text('🥬🥣Kale, Spinach & Rocket Smoothie🥑🍊')
streamlit.text('🐔🐔Hard-boiled Free Range Egg🐔🐔')
streamlit.text('🥑🥑Avocado Toast🥑🥑')

streamlit.header('🍍🍊Build your own fruit smoothie!🍍🍎')

my_fruit_list = pandas.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
my_fruit_list = my_fruit_list.set_index('Fruit')

# let us put a pick list so that they can select what they want
fruits_selected = streamlit.multiselect('Pick some fruits:', list(my_fruit_list.index), ['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# display the page on the list
streamlit.dataframe(fruits_to_show)

# add a new header
streamlit.header("Fruityvice Fruit Advice!")
fruit_choice = streamlit.text_input('What fruit would you like information about?','kiwi')
streamlit.write('The user entered ', fruit_choice)


fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "kiwi")

# below code line is removed
# streamlit.text(fruityvice_response.json()) #just writes the data to the screen

# take the json version of the response and normalise it
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())

# output the data in the screen as a table
streamlit.dataframe(fruityvice_normalized)

#streamlit.stop()


my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select CURRENT_ACCOUNT(), CURRENT_USER(), CURRENT_REGION()")
my_data_rows = my_cur.fetchone()
streamlit.header("Hello from Snowflake:")
streamlit.dataframe(my_data_row)

#fruit_choice = streamlit.text_input('What fruit would you like to add?','jackfruit')
#streamlit.write('Thanks for adding', fruit_choice)

#streamlit.write('Thanks for adding', add_my_fruit)
#my_cur.execute("insert into fruit_load_list values('from streamlit')")

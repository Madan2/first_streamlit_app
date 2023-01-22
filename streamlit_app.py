import streamlit
import pandas

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

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response.json()) #just writes the data to the screen

# take the json version of the response and normalise it
fruityvice_normalized = python.json_normalize(fruityvice_response.json())

# output the data in the screen as a table
streamlit.dataframe(fruityvice_normalized)

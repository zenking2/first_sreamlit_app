import streamlit
streamlit.title('My Parents New Healthy Dinner')

streamlit.header('Breakfast Favourites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Half-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avacado Toast')

streamlit.header('Importing CSV File from S3 using Pandas Library')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

streamlit.text('Fruits Size Table')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)



streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

streamlit.dataframes(my_fruit_List)

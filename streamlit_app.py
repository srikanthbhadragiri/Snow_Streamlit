import streamlit

streamlit.title("Srikanth's My First Streamlit App1")
streamlit.header('Snowflake Architech Certification - Syallabus')
streamlit.text('end-to-end Data Flow')
streamlit.text('Design and Deploy - Data Architecture')
streamlit.text('Knowledge on third party tools')
streamlit.text('Shared Data Set')

import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

# Add a picklist
my_fruit_list = my_fruit_list.set_index('Fruit')
#streamlit.multiselect("Pick some fruits: ", list(my_fruit_list.index), ['Grapefruit', 'Kiwifruit'])
#streamlit.dataframe(my_fruit_list)

fruits_selected = streamlit.multiselect("Pick some fruits: ", list(my_fruit_list.index), ['Grapefruit', 'Kiwifruit'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

streamlit.dataframe(fruits_to_show)


streamlit.header('Fruityvice Fruit Advice!')

import requests
fruityvice_response = requests.get('https://fruityvice.com/api/fruit/watermelon')
#streamlit.text(fruityvice_response.json())

fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruityvice_normalized)

fruit_choice = streamlit.text_input('What fruit would you like information about?', 'Kiwi')
steamlit.write('The user entered',fruit_choice)

fruityvice_response2 = requests.get('https://fruityvice.com/api/fruit/' + fruit_choice)
fruityvice_normalized2 = pandas.json_normalize(fruityvice_response2.json())
streamlit.dataframe(fruityvice_normalized2)


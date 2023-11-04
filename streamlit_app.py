import streamlit

streamlit.title("Srikanth's My First Streamlit App")
streamlit.header('Snowflake Architech Certification - Syallabus')
streamlit.text('end-to-end Data Flow')
streamlit.text('Design and Deploy - Data Architecture')
streamlit.text('Knowledge on third party tools')
streamlit.text('Shared Data Set')

import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

# Add a picklist
streamlit.multiselect("Pick some fruits: ", list(my_fruit_list.index))

streamlit.dataframe(my_fruit_list)
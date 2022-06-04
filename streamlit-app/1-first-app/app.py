# SETUP

import streamlit as st
import pandas as pd
import datetime 


#-------------------
# CREATE DATA

# Simple dataframe
df = pd.DataFrame({
    'A': [1, 4, 3, 2],
    'B': [10, 20, 30, 40]
    })

#-------------------
# START OF APP

#-------------------
# HEADER

# Title of our app
st.title('Hallo')

# Add header

st.header ('Header')
# Add a gif from https://giphy.com/

st.markdown("![Hallo](https://media.giphy.com/media/R6gvnAxj2ISzJdbA63/giphy-downsized-large.gif)")


#-------------------
# BODY



#-------------------
# Show static DataFrame

st.dataframe(df)

#-------------------
# Bar chart

st.bar


add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)


age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')

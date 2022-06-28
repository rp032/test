# SETUP

import streamlit as st
import seaborn as sns
import pandas as pd
import altair as alt
import streamlit as st
import matplotlib.pyplot as plt


# Einlesen der CSV Datei

df = pd.read_csv("Fallstudie2_Daten.csv")


st.title('Herzlich Willkommen auf dem Dashboard von Rafaela Papanikolaou')

st.subheader('Wir analyiseren den Twitter Account von Lebron James')




# Erkenntnisse: 

st.markdown("Lebrons Akitvität ist um 10% niedriger als im letzen Monat")
st.metric(label="Twitter Aktivität", value="40%", delta="-10%", delta_color="normal")

st.dataframe(df, 1000, 1000)

st.table(df)


st.line_chart (df["sentiment"])


st.bar_chart(df["compound"])



# SelectBox
add_selectbox = st.sidebar.selectbox("Was möchtest du sehen?",("Datensatz", "Plots", "Lustige Memes"))




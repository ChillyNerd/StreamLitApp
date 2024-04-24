import os

import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

PATH = 'https://raw.githubusercontent.com/evgpat/datasets/main/penguins.csv'

file = st.file_uploader("Загрузите файл")
if file is not None:
    df = pd.read_csv(file)
else:
    df = pd.read_csv(PATH)

X = df.drop('вид', axis=1)
y = df['вид']

st.title('Пингвины')

types = y.unique()
cats = df.select_dtypes(include='object')
selected_spice = st.selectbox(options=y.unique(), label='Вид пингвина')

selected_X = st.selectbox(options=X.columns, label='Ось X')
selected_Y = st.selectbox(options=X.columns, label='Ось Y')

df[df['вид'] == selected_spice]

fig, ax = plt.subplots()
ax = sns.scatterplot(x=selected_X, y=selected_Y, data=df[df['вид'] == selected_spice])
st.pyplot(fig)

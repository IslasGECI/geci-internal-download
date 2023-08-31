import streamlit as st
import pandas as pd
import descarga_datos as dd
import json
import requests
import io


st.write(
    """
# GECI
Hello world
V3
"""
)

df = pd.read_csv("tests/data/estaciones_guadalupe.csv")

st.download_button(
    label="Download data as CSV",
    data=df.to_csv(),
    file_name='large_df.csv',
    mime='text/csv',
)

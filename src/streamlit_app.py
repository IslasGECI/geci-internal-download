import streamlit as st
import pandas as pd
import descarga_datos as dd
import json
import requests
import io


TEXTO_ANALYSIS = """{
    "source": "tabular_data_packages",
    "path": "roedores_capturarecaptura_cedros",
    "filename": "roedores_capturarecaptura_cedros.csv",
    "version": "e511b813667ef3063c47b47c954d3b8c202ef709",
    "type": "datapackage"
}"""


analisis: dict = json.loads(TEXTO_ANALYSIS)
datafile = dd.internals.DataFile(**analisis)

st.write(
    """
# GECI
Hello world
V3
"""
)

response = requests.get(datafile.get_url_to_file()).content
df = pd.read_csv(io.StringIO(response.decode("utf-8")))

st.download_button(
    label="Download data as CSV",
    data=df.to_csv(),
    file_name='large_df.csv',
    mime='text/csv',
)

import streamlit as st
import pandas as pd
import requests

st.write(
    """
# GECI
Hola Fer. \n
Aquí puedes descargar los datos de grabaciones vocalizaciones Socorro. \n
Un saludo desde CD 💻
"""
)

data_request = requests.get("http://data_api:10000/api/v1/data/grabaciones_socorro").json()
datapackage_request = requests.get(
    "http://data_api:10000/api/v1/data/grabaciones_socorro_datapackage"
).json()

df = pd.read_json(data_request)

st.write(datapackage_request["resources"][0]["description"])

st.download_button(
    label="Download data as CSV",
    data=df.to_csv(),
    file_name=f"{datapackage_request['resources'][0]['name']}.csv",
    mime="text/csv",
)


st.dataframe(df, hide_index=True)

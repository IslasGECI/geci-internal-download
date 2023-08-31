import streamlit as st
import pandas as pd


st.write(
    """
# GECI
Hello world
V3
"""
)

df = pd.read_csv("/workdir/data/seabird_tracking/bl_gps_albatross_guadalupe.csv")

st.download_button(
    label="Download data as CSV",
    data=df.to_csv(),
    file_name="large_df.csv",
    mime="text/csv",
)

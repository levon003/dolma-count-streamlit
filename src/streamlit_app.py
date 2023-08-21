from pathlib import Path

import pandas as pd
import streamlit as st

st.markdown("# Dolma")

data_filepath = Path(__file__).parent / "resources" / "wiki_word_counts.csv"

df = pd.read_csv(data_filepath)
st.dataframe(df)

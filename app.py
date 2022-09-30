import streamlit as st
import pandas as pd
import numpy as np

st.title("supermarket data")
df = pd.read_csv('supermarket.csv')
st.subheader('Top 10 performing stores')
df.sort_values(["store_sales"], 
axis=0, 
ascending=[False],
inplace=True)
st.dataframe(df[["store_id","store_sales"]].head(n=10))


st.subheader('Lowest 10 performing stores')
df.sort_values(["store_sales"], 
axis=0, 
ascending=[True],
inplace=True)
st.dataframe(df[["store_id","store_sales"]].head(n=10))


st.subheader("Average Sale Per Customer") #gauge
st.metric(label="USD", value="21.00")
st.header("Average Sale Per Customer Overall") #gauge
st.metric(label="USD", value="75.00")


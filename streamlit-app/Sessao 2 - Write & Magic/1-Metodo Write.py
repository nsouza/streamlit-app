import streamlit as st 
import pandas as pd 
import numpy as np 
import altair as alt 

st.write("Bom dia, tudo bem?")

st.write(pd.DataFrame({
    'Coluna A': [1,2,3,4],
    'Coluna b': ["Cachorro","Gato","Cavalo","Zebra"]
}))

array = [1,2,"abc","Martin",True]
st.write('Aqui temos um array',array)


st.write('Data frame')
df = pd.DataFrame(
    np.random.rand(200,3),
    columns=["a","b","c"]
)

c = alt.Chart(df).mark_circle().encode(
    x='a',y='b',size='c', tooltip=['a','b','c']
)

st.write(df)
st.write(c)

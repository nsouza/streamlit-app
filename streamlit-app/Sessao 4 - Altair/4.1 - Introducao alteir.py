from json import tool
import altair as alt 
import pandas as pd
import streamlit as st  

fonte = pd.DataFrame(
    {
        'a': ['A','B','C','D','E','F','G','H','I'],
        'b': [26,55,45,79,32,91,19,45,23]
        
    }
)

fonte

graf_barras = alt.Chart(fonte).mark_bar().encode(
    x='a',
    y='b',
    color='a',
    tooltip=['a','b']
)

rotulo = graf_barras.mark_text(
    dy= -15,
    size=17
).encode(
    text='b',
)


st.subheader('Plot de Grafico de barras')
st.altair_chart(graf_barras+rotulo, use_container_width=True)

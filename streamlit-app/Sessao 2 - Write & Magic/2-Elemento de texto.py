import streamlit as st 
st.title('Este é o título ')
st.header('Este é um cabeçalho')
st.subheader('Este é um subeçalho')

st.markdown('A nota do **alunos** não foram boas')
st.caption('Este é um caption')

#code
code = '''
    if(fome > 0):
        return "Ir para geladeira"
    else:
        retur "Estudar streamlit"
'''
st.code(code,language='python')

st.text('Este é um texto usando st.text')

st.latex('\int x*2')

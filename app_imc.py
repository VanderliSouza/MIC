import streamlit as st
import pandas as pd

st.set_page_config(page_title="Índice de massa corporal")

with st.container():
    st.subheader('Veja como está seu IMC')
    #st.title("Dashboard UOR")
    #st.write("Informacoes sobre departamentos")
   # st.write("Acesso ao Site Cometas [Sozinho](https://ds.bb.com.br/)")



with st.container():
    def compose(g, f):
        def h(*args, **kwargs):
            return g(f(*args, **kwargs))
        return h
    def BMI(weight, height):
        #st.write(weight / height**2)
        return weight / height**2
    def evaluate_BMI(bmi):
        if bmi < 15:
            return "Muito abaixo do peso"
        elif bmi > 16 and bmi < 18.5:
            return "Abaixo do peso"
        elif bmi > 18.5 and bmi < 25:
            return "Normal"
        elif bmi > 25 and bmi < 30:
            return "Excesso de peso"
        elif bmi > 30 and bmi < 35:
            return "Obesidade Classe I (Obesidade moderada)"
        elif bmi > 35 and bmi < 40:
            return "Obesesidade II (Obesidade severa)"
        elif bmi > 40:
            return "Obesidade Classe III (Obesidade extrema)"
        
    f = compose(evaluate_BMI, BMI)
    again = "s"
    while again == "s":
        peso = st.slider('Qual seu peso?', 0, 250, 50)
        #st.write("I'm ", peso, 'years old')
        weight = int(peso)
        #altura = st.slider('Qual sua altura?')
        values = st.slider(
        'Selecione a sua altura',
        0.1, 2.5)
        #st.write('Values:', values)
        height = values
        st.write(f(weight, height))
        #if st.button('Say hello'):
         #   st.write('Why hello there')
        #else:
            #st.write('Goodbye')
        again = input("Deseja novo cálculo? (s/n)")
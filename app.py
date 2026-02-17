import streamlit as st
import joblib
import pandas as pd

st.set_page_config(page_title='house price pediction', page_icon= '🏘️', layout= 'wide' )
pipeline = joblib.load('pipeline.plk')

st.title('HOUSE PRICE PREDICTION 🏘️')

col1, col2 = st.columns(2)

with col1 :
    div_list = ['Noida', 'Gurgaon', 'Ghaziabad', 'Greater Noida','ND_Rohini', 'ND_South', 'ND_Dwarka','ND_West','Faridabad','G_South','ND_East','ND_North','New Delhi','ND_Central','G_North']
    division = st.selectbox('Enter Division : ', div_list)
    
with col2 :
    reg_list = ['east', 'west', 'north', 'core', 'south']
    region = st.selectbox('Enter Region : ', reg_list)


area = st.slider('Enter area : ', 500, 2100, 750)
      
col4, col5 = st.columns(2)
with col4 :
    new_old = st.radio('Select type: ', ['New Property', 'Resale'])
    
with col5 :
    house_type_list = ['Flat', 'Individual House']
    type_of_building = st.radio('Enter House Type ', house_type_list)
    


lift = st.number_input('Enter number of lifts : ', 0, 10, 1)
parking = st.number_input('Enter number of parkings : ', 0, 10, 1)
bedroom = st.number_input('Enter number of bedrooms : ', 0, 10, 1)
bathroom = st.number_input('Enter number of bathrooms : ', 0, 10, 1)
balcony = st.number_input('Enter number of balcony : ', 0, 10, 1)


btn = st.button('Predict the price')

if btn :
    pass
import streamlit as st
import pandas as pd
from pickle import load


st.title('Car Dekho.com')
st.subheader('Selling Price of the car:')

def create_page():
    Present_price = st.sidebar.number_input('Enter the Present Price')   
    Kms_driven = st.sidebar.number_input('Enter the KM driven')
    owners = st.sidebar.radio('Owners',(0,1,3))
    years = st.sidebar.number_input('Enter the Year')
    Fuel_type_diesel = st.sidebar.radio('Fuel Type Diesel?',(0,1))
    Fuel_type_petrol = st.sidebar.radio('Fuel Type Petrol?',(0,1))
    Seller=st.sidebar.radio('Seller-Individual',(0,1))
    Transmission=st.sidebar.radio('Transmission-Manual',(0,1))
    
    
    data_dict = { 
                 'Present_Price':Present_price,
                 'Kms_Driven':Kms_driven,
                 'Owner':owners,
                 'No_of_years':years,
                 'Fuel_Type_Diesel':Fuel_type_diesel,
                 'Fuel_Type_Petrol':Fuel_type_petrol,
                 'Seller_Type_Individual':Seller,
                 'Transmission_Manual':Transmission
  }
    
    df = pd.DataFrame(data_dict, index=[0])
    return df


features =  create_page()

if st.sidebar.button('Submit'):
    st.write(features)
    loaded_model = load(open('random_forest_regression_model.pkl','rb'))
    res = loaded_model.predict(features)
    st.write(res)
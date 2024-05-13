import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np
import altair as alt
import streamlit_ext as ste

st.title("Define Wall Loading")

st.sidebar.info("This is an information page, required to prepare the input file.")

st.markdown("""
            
          Please read the variables required to build the input file.
            
            """)


Case1_pic = Image.open("./assets/WallLoading.png")

st.image(Case1_pic, width = 600)
    


    
st.markdown("""
        ---
        #### Where:
        
        $P$: Axial Load [$kg$]
          
        $V$: In Plan Shear [$kg$]
          
        $M_{oop}$: Out of Plane Moment [$kg-m$]
          
        $M_{ip}$: In Plane Moment [$kg-m$]
        
        
        """)



st.markdown("""
            ---
        Please download the input file Template 
        with the button below to check the structure of
        the input file
        
        """)
Template_input_csv = open("./csv/Template_Input_Loads.csv")

st.download_button(
label="Download input file Template",
data=Template_input_csv,
file_name='Template_Input_Loads.csv'
)



uploaded_file = ste.file_uploader("Please upload the csv file of the walls to be analyzed",key='Loads')
if uploaded_file is not None:
    dataframe = pd.read_csv(uploaded_file)
    st.write(dataframe)
    csv_Stored = dataframe.to_csv('./Inputs/Input_Walls_Loads.csv',index=False)
    
st.divider()
import streamlit as st
from PIL import Image
import pandas as pd
import streamlit_ext as ste

st.title("Define Walls Geometry")
st.sidebar.info("This is an information page, required to prepare the input file.")

st.markdown("""
            
          Please read the variables required to build the input file.
            
            """)


Case1_pic = Image.open("./assets/WallGeometry.png")

st.image(Case1_pic, width = 600)
 
st.markdown("""
          ---
          #### Where:

            """)
        
col1, col2 = st.columns(2, gap = "small")
with col1:
    
    st.markdown("""
          
          $w_b$: Beam Width [$m$]
          
          $h_b$: Beam Height [$m$]
          
          $w_c$: Column Width [$m$]
          
          $h_c$: Column Height [$m$]
          
          
          
            """)
    
with col2:
  
    st.markdown("""
          
          $H$: Wall Height [$m$]
          
          $L$: Wall Length [$m$]
          
          $t$: Wall Thickness [$m$]
          
          
            """)  
    
    

st.markdown("""
                ---
            Please download the input file Template 
            with the button below to check the structure of
            the input file
            
            """)
Template_input_csv1 = open("./csv/Template_Input_geometry.csv")

st.download_button(
    label="Download input file Template",
    data=Template_input_csv1,
    file_name='Template_Input_geometry.csv'
    )



uploaded_file1 = ste.file_uploader("Please upload the csv file of the walls to be analyzed", key = 'Geometry')
 
if uploaded_file1 is not None:
      dataframe1 = pd.read_csv(uploaded_file1)
      st.write(dataframe1)
      csv_Stored1 = dataframe1.to_csv('./Inputs/Input_Walls_geometry.csv',index=False)  
          
st.divider()
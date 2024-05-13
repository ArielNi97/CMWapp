import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np
import altair as alt
import streamlit_ext as ste
from streamlit_extras.colored_header import colored_header
from streamlit_extras.switch_page_button import switch_page
from pathlib import Path
folder_path = Path(__file__).parent.parent

st.markdown('''
            ## Resources  
            '''
            )

colored_header(
    label= "",
    color_name="blue-60",
    description= None
    )

st.markdown('''
            #### In this page can be found 4 different Confined Masonry Wall calculations regarding the Axial, Bending, Axial-bending and In Plane Shear capacities, and the particular points to build the Backbone curve. Furthermore, it can be downloaded the out of plane capacities and demands of such walls.  
            '''
            )

Example1 = folder_path.joinpath('assets/Example1.pdf')
Example2 = folder_path.joinpath('assets/Example2.pdf')
Example3 = folder_path.joinpath('assets/Example3.pdf')
Example4 = folder_path.joinpath('assets/Example4.pdf')

col1, col2, col3, col4 = st.columns(4, gap = "small")

with col1:
    with open(Example1, "rb") as pdf_file:
        PDFbyte = pdf_file.read()
    st.download_button(
        label = "📃 Download Example 1",
        data = PDFbyte,
        file_name = Example1.name,
        mime = "application/octet-stream",
        
    ) 
    
with col2:
   with open(Example2, "rb") as pdf_file:
        PDFbyte = pdf_file.read()
   st.download_button(
        label = "📃 Download Example 2",
        data = PDFbyte,
        file_name = Example2.name,
        mime = "application/octet-stream",
        
    ) 
   
with col3:
   with open(Example3, "rb") as pdf_file:
        PDFbyte = pdf_file.read()
   st.download_button(
        label = "📃 Download Example 3",
        data = PDFbyte,
        file_name = Example3.name,
        mime = "application/octet-stream",
        
    ) 

with col4:
   with open(Example4, "rb") as pdf_file:
        PDFbyte = pdf_file.read()
   st.download_button(
        label = "📃 Download Example 4",
        data = PDFbyte,
        file_name = Example4.name,
        mime = "application/octet-stream",
        
    ) 

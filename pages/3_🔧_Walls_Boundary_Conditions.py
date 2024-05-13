import streamlit as st
from PIL import Image
from pathlib import Path
import pandas as pd
import streamlit_ext as ste

# current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd() #cwd stands for current working directory
st.title("Define Boundary Condition")
st.sidebar.info("This is an information page, required to prepare the input file.")
# Case1_pic = current_dir / "assets" / "BC1.png"

st.markdown("""
            
          Please read the variables required to build the input file.
            
            """)

Case1_pic = Image.open("./assets/BC1.png")
Case2_pic = Image.open("./assets/BC2.png")

col1, col2 = st.columns(2, gap = "small")
with col1:
    st.markdown('## CASE 1')
    st.image(Case1_pic, width = 300)
    st.markdown("""
            
          For those walls with the perimeter fixed, case 1 needs to be chosen 
          and the input value needs to be set as `1` in the options available below.
          
            """)
    
with col2:
    st.markdown('## CASE 2')
    st.image(Case2_pic, width = 320)
    st.markdown("""
            
          For those walls with the bottom beam, two lateral columns fixed and the top tie beam released, case 2 needs to be chosen 
          and the input value needs to be set as `2` in the options available below.
          
            """)   
    
    
st.markdown("""
            
          ---
          When having a rigid and semirigid diaphragm at the top and bottom of the wall, constraining the top beams perpendicular to the wall,
          is it recommended to choose Case 1, Otherwise, when having a flexible diaphragm (as typical in Nicaraguan's roof), it is recommended to 
          select Case 2. For further information, please see the **Assumptions and Limitations** page.
          
            """) 

Case_option = ste.selectbox(
    'Please select the Case',
    (1,2),label_visibility="visible", key = 'case')

# Define the structure of the data

Boundary_header = ['Case']

# Define the actual data

df = pd.DataFrame([Case_option], columns = Boundary_header)
    
    
csv_Stored = df.to_csv('./Inputs/Input_Walls_Case.csv',index=False)
import streamlit as st
from PIL import Image
import pandas as pd
import streamlit_ext as ste

st.title("Define Walls Material")
st.sidebar.info("This is an information page, required to prepare the input file.")

st.markdown("""
            
          Please select the variables required to build the input file.
            
            """)





col1, col2, col3 = st.columns(3, gap = "small")
with col1:
    st.markdown("## Select $f'_m$") 
    fm = ste.slider('none', 45, 55, 50 , key = "fm1",label_visibility="hidden")
    # ste.slider()
    st.markdown(f"$f'_m = {fm if isinstance(fm, int) == True else fm[0]} kg/cm^2$ has been selected")
  
with col2:
    st.markdown("## Select $f'_c$") 
    fc = ste.selectbox(
    'Please select fc',
    (210,245),label_visibility="hidden",key = "fc")
    st.markdown(f"$f'_c = {fc} kg/cm^2$ has been selected")


with col3:
    st.markdown("## Select $f_y$") 
    fy = ste.selectbox(
    'Please select fy',
    (4200,2800),label_visibility="hidden",key = "fy")
    st.markdown(f"$f_y = {fy} kg/cm^2$ has been selected")



st.markdown("""
          
          #### Where:
          
          $f'_m$: Masonry Compressive strength based on net area [$kg/cm^2$]
          
          $f'_c$: Concrete Compressive strength at 28 days [$kg/cm^2$]
          
          $f_y$: Steel Yielding Stress for Reinforcement Bars [$kg/cm^2$]
          
            """)

# Define the structure of the data


Material_header = ['fm', 'fc', 'fy']

# Define the actual data
Material_data = [[fm if isinstance(fm, int) == True else fm[0], fc, fy]]
df = pd.DataFrame(Material_data, columns = Material_header)
    
    
csv_Stored = df.to_csv('./Inputs/Input_Walls_Material.csv',index=False)

st.divider()

st.markdown("""
          
          ### Reinforcement Bars
          
          - Please download the template as reference in order to modify it according to the reinforcement requirements
          
            """)

Template_input_csv = open("./csv/Template_Input_rebars.csv")

st.download_button(
label="Download input file Template",
data=Template_input_csv,
file_name='Template_Input_rebars.csv'
)



uploaded_file = ste.file_uploader("Please upload the csv file of the rebars of the walls to be analyzed",key='Rebars')
if uploaded_file is not None:
    dataframe = pd.read_csv(uploaded_file)
    st.write(dataframe)
    csv_Stored = dataframe.to_csv('./Inputs/Input_Walls_rebars.csv',index=False)

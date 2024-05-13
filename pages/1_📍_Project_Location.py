import streamlit as st
import pandas as pd
import csv
from PIL import Image
import streamlit_ext as ste

st.title("Define Project Location")
st.sidebar.info("This is a page to select the required project location information")

df_location = pd.read_csv("./csv/Accelerations.csv")
options = df_location['Location']


dd_location = ste.selectbox(
    'Please select the location',
    (options),label_visibility="visible",key="dd_location")

st.write(dd_location, 'option has been selected')

get_location = dd_location

get_acceleration = df_location.loc[df_location['Location']==get_location].head(20)


col1, col2 = st.columns(2, gap = "small")
with col1:
    
    st.markdown(f"""
            #### The PGA is:
             {float(get_acceleration["a"])} [g]
            
            #### The Soil Amplification Factor is:
             {float(get_acceleration["Fs"])} [-]
            
            #### Importance Factor
            """)
    dd_importance_factor = ste.selectbox(
    '## Select the Importance Factor',
    (0.75, 1, 1.3,1.65),label_visibility="visible",key = 'dd_importance_factor')
    
with col2:
    st.markdown(f"""
            ### Map of Nicaragua
            """)
    
    Case1_pic = Image.open("./assets/NicaraguanMap.png")

    st.image(Case1_pic, width = 400)

    
st.divider()

# Define the steructure of the data


Project_header = ['a', 'Fs', 'I']

# Define the actual data
Project_data = [[float(get_acceleration["a"]), float(get_acceleration["Fs"]), dd_importance_factor]]
df = pd.DataFrame(Project_data, columns = Project_header)
csv_stored = df.to_csv('./Inputs/Input_Walls_Location.csv',index=False)


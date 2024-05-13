import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np
import altair as alt
from streamlit_extras.colored_header import colored_header
from streamlit_extras.switch_page_button import switch_page
from pathlib import Path

# current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd() #cwd stands for current working directory
folder_path = Path(__file__).parent.parent

st.markdown('''
            ## User Manual  
            '''
            )
colored_header(
    label= "",
    color_name="blue-60",
    description= None
    )

colored_header(
    label="Step 1",
    color_name="red-80",
    description= None
    )

st.markdown('''
            - Start by reading the homepage to gather more information about this application. 
            '''
            )

HomePage = st.button("HomePage")   
 
if HomePage:
    switch_page("HomePage")
    
colored_header(
    label="Step 2",
    color_name="red-80",
    description= None
    )

st.markdown('''
- Navigate to the **Project Location Page** located in the left sidebar. Select the project's location where the walls are situated.
- Information about Peak Ground Acceleration and Soil Amplification factors will be displayed.
- For users outside Nicaragua, refer to the PGA and Soil Amplification Factor specific to your project location hazard.
- Select the importance factor for the project as per the NSR-21 Nicaragua code guidelines.ct the importance factor for the project. Please read the NSR-21 Nicaragua code to know when to select which value.

            '''
            
            )

colored_header(
    label="Step 3",
    color_name="red-80",
    description= None
    )

st.markdown('''
- Click on the **Walls Material Page**.
- Adjust the Masonry compressive strength by using the slider (ranging from 45 $kg/cm^2$ to 55 $kg/cm^2$).
- Choose the compressive strength at 28 days from the available options (210 $kg/cm^2$ or 245 $kg/cm^2$).
- Select the Steel yielding stress for Reinforcement Bars from the options (4200 $kg/cm^2$ or 2800 $kg/cm^2$).
- Download the Input File Template for reinforcement Bars by clicking the '**Download Input File Template**' button.
- Open the file in your local Downloads folder.
- The file consists of two columns: Wall Label and Rebars.
- Wall labels start with "W" followed by ascending numbers.
- Vertical reinforcement bars for each confined tie-column are listed under the **Rebars** header.
- The first number indicates the quantity of bars for each column, followed by a hashtag and another number representing the bar type (e.g., "#4" for 4/8" diameter).
- Customize the input file by adding, removing, or editing walls and reinforcement bars as needed.
- Wall labels are crucial for identifying walls in the results.
- Rebar quantities are limited to 4, 6, 8, 10, and 12, and types range from #3 to #8.
- Ensure that the arrangement of rebars does not exceed 8#8 in total steel reinforcement area.
- Save the edited input file locally and upload it by dragging and dropping it onto the cloud icon. Alternatively, use the '**Browse Files**' button.
- Double-check the rebar information in the chart displayed after the file upload; if it's incorrect, try uploading it again.
            
            '''
            
            )

colored_header(
    label="Step 4",
    color_name="red-80",
    description= None
    )

st.markdown('''
 - Navigate to the **Walls Boundary Conditions Page**.
- Carefully read the information provided for CASE 1 and CASE 2.
- After completing the reading, select the appropriate case for your walls.
            '''
            
            )

colored_header(
    label="Step 5",
    color_name="red-80",
    description= None
    )

st.markdown('''
 - Visit the **Walls Geometry Page**.
- Carefully review the information presented in the image.
- After reading, download the Input File Template by clicking the '**Download Input File Template**' button to guide you in preparing the CSV file.
- Open the file, and observe that it contains columns for Wall Label, Level, L, H, t, wb, hb, wc, and hc.
- Wall labels start with "W" followed by ascending numbers.
- In the Level column, specify the story to which the wall belongs.
- Add the wall lengths in meters to the L column.
- Specify wall heights in meters in the H column.
- Enter wall thickness in meters in the t column.
- Record confined beams' widths and heights in meters in the wb and hb columns, respectively.
- Include confined columns' widths and heights in meters in the wc and hc columns.
- After modifying the wall geometry parameters, save the file locally.
- Refer to the Assumptions and Limitations page for details on geometric value limits.
- Drag and drop the file onto the cloud icon within the **Walls Geometry Page**, or use the '**Browse Files**' button to upload it.
- Double-check the geometry in the chart displayed; if it's incorrect, try uploading it again.
            '''
            
            )

colored_header(
    label="Step 6",
    color_name="red-80",
    description= None
    )

st.markdown('''
- Proceed to the **Walls Loading Page**.
- Carefully review the information presented in the image.
- After completing the reading, download the Input File Template by clicking the '**Download Input File Template**' button to guide you in preparing the CSV file.
- Open the file, which includes columns for Wall Label, Level, P (kg), V (kg), Mip (kg-m), and Moop (kg-m).
- Wall labels start with "W" followed by ascending numbers.
- In the Level column, specify the story to which the wall belongs.
- Add the axial load in kilograms to the P column.
- Enter the shear in-plane load in kilograms in the V column.
- Record in-plane moment in kilograms-meters in the Mip column.
- Specify out-of-plane moment in kilograms-meters in the Moop column.
- After modifying the wall loading information, save the file locally.
- Drag and drop the file onto the cloud icon within the **Walls Loading Page**, or use the '**Browse Files**' button to upload it.
- Double-check the loading information in the chart displayed; if it's incorrect, try uploading it again.

> **Note:** Ensure the quantity of walls is consistent across all CSV files uploaded for the application to function correctly.          
            '''
            
            )

colored_header(
    label="Step 7",
    color_name="red-80",
    description= None
    )

st.markdown('''
- Access the **Walls Analysis Page** to view the results.
- This page includes six tabs, with the Axial Load Capacity (ALC) of the walls displayed by default.
- Two plots are shown: one depicting Axial Load Capacities of Walls and another displaying Axial Load Capacities vs. Demands.
- The first graphic shows wall labels on the x-axis and related axial capacities in kg on the y-axis, with colors and sizes indicating wall lengths. Hover over points for more information.
- The second graphic displays axial load demands on the x-axis and related axial capacities on the y-axis. The diagonal line represents a limit where the Demand-Capacity Ratio (DCR) should not exceed 1, indicating compliance with the code. Walls below the diagonal line may not meet code requirements. Colors are based on wall labels.
- Download data in CSV format by clicking the '**Download Data in CSV Format**' button or save plots as images by right-clicking on the graphics.
- Expand both graphics to fullscreen mode by clicking the '**View Fullscreen**' icon at the top right.
- Switch to the Pure Bending Capacities of Walls (PBC) tab to view bending results with similar features.
- The Axial-Bending Capacity of Walls (ABC) tab displays an interaction between axial and bending capacities, allowing filtering by wall labels.
- The In Plane Shear Walls Capacities (INPSC) tab provides two graphics with corresponding data download options.
- The Out of Plane Stress Capacities (OOPSC) tab displays three graphics based on wall location: first floor, any floor, and highest floor. Download data for each with the provided buttons.
- Explore the Backbone Curve (BBC) tab, offering a tri-linear model to explain confined masonry walls' non-linear behavior. Utilize the same options as the ABC tab.
  
> Thank you for reading this manual! Enjoy using the application, and please share your feedback with us!
      
            '''
            
            )

UserManual = folder_path.joinpath('assets/UserManual.pdf')

# UserManual = current_dir / "assets" / "UserManual.pdf"
with open(UserManual, "rb") as pdf_file:
    PDFbyte = pdf_file.read()

st.download_button(
        label = "📃 Download User Manual",
        data = PDFbyte,
        file_name = UserManual.name,
        mime = "application/octet-stream",
        
    ) 



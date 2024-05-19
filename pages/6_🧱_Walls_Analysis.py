import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np
import altair as alt
import subprocess
import traceback


st.title("Walls Output")

if st.button("**Run Analysis**"):
         try:
            # Replace "my_script.py" with the actual name of your script
            
            
            subprocess.call(["python", "./scripts/BuildMLInputFile.py"], check=True)
            # subprocess.run(["python", "./scripts/LoadMLmodels.py"], check=True)
            # subprocess.run(["python", "./scripts/CapacitiesVsDemands.py"], check=True)
            # subprocess.run(["python", "./scripts/BuildOOPCalculator.py"], check=True)
            # subprocess.run(["python", "./scripts/OOPLimitLines.py"], check=True)
            
            st.success("Analysis executed successfully!")
         
         except Exception as e:
            st.error(f"Error: {type(e).__name__} - {str(e)}")
            st.error(traceback.format_exc())
            
        
st.sidebar.info("This is an output page, to see the Analysis results of the walls")


st.markdown("""
            
          Please see in the tabs below the results of the analysis of the Confined Masonry Walls.

            """)

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["ALC", "PBC", "ABC", "INPSC", "OOPSC", "BBC"])

with tab1:
    st.markdown("""
            
         ## Axial Load Capacities of Walls
          
            
            """
    )

    chart_data = pd.read_csv("./outputs/Pn.csv")

    st.vega_lite_chart(chart_data, {
    'mark': {'type': 'circle', 'tooltip': True},
    'encoding': {
        'x': {'field': 'Wall Label', 'type': 'nominal'},
        'y': {'field': 'Pn (kg)', 'type': 'quantitative'},
        'size': {'field': 'L (m)', 'type': 'quantitative'},
        'color': {'field': 'L (m)', 'type': 'quantitative'},
    },
    })
    
    st.divider()
    st.markdown("""
            
         ## Axial Load Capacities vs Demands
          
            
            """
    )    
    Limit_Line = pd.read_csv("./outputs/LimitLineAxial.csv")
    PnvsPu = pd.read_csv("./outputs/PnvsPu.csv")   


    chart = alt.Chart(Limit_Line).mark_line(color='#1f77b4').encode(x = 'Pu (kg)', y = 'Pn (kg)') + \
            alt.Chart(PnvsPu).mark_point(color='#ff7f0e').encode(x = 'Pu (kg)', y = 'Pn (kg)',color= {'field': 'Wall Label', 'type': 'nominal', 'scale': {'scheme': 'Blues'}})
            
    st.altair_chart(
       chart, 
       theme="streamlit", use_container_width=True)
    
    PnvsPu_csv = open("./outputs/PnvsPu.csv")

    st.download_button(
    label="Download data in csv format",
    data=PnvsPu_csv,
    file_name='PnvsPu.csv'
    )

   
with tab2:
    st.markdown("""
            
         ## Pure Bending Capacities of Walls

            """
    )

    chart_data = pd.read_csv("./outputs/Mn.csv")

    st.vega_lite_chart(chart_data, {
    'mark': {'type': 'bar', 'tooltip': True},
    'encoding': {
        'x': {'field': 'Wall Label', 'type': 'nominal'},
        'y': {'field': 'Mn (kg-m)', 'type': 'quantitative'},
        'color': {'field': 'L (m)', 'type': 'quantitative', 'scale': {'scheme': 'viridis'}},
    },
    })
    
    st.divider()
    st.markdown("""
            
         ## Pure Bending Capacities vs Demands
          
            """
    )    
    Limit_Line = pd.read_csv("./outputs/LimitLineBending.csv")
    MnvsMu = pd.read_csv("./outputs/MnvsMu.csv")   

    chart = alt.Chart(Limit_Line).mark_line(color='#2DAD8C').encode(x = 'Mu (kg-m)', y = 'Mn (kg-m)') + \
            alt.Chart(MnvsMu).mark_point().encode(x = 'Mu (kg-m)', y = 'Mn (kg-m)',color= {'field': 'Wall Label', 'type': 'nominal', 'scale': {'scheme': 'viridis'}})
            
    st.altair_chart(
       chart, 
       theme="streamlit", use_container_width=True)
    
    MnvsMu_csv = open("./outputs/MnvsMu.csv")

    st.download_button(
    label="Download data in csv format",
    data=MnvsMu_csv,
    file_name='MnvsMu.csv'
    )
   
with tab3:
   st.markdown("""
            
         ## Axial - Bending Capacities of Walls
          
            
            """
    )


   # Sample data
   df1 = pd.read_csv("./outputs/AB1.csv")
   df2 = pd.read_csv("./outputs/AB2.csv")
   df3 = pd.read_csv("./outputs/AB3.csv")
   df4 = pd.read_csv("./outputs/AB4.csv")
   
   concatenated_df = pd.concat([df1,df2])
   concatenated_df1 = pd.concat([df2,df3,df4])
   
   data = concatenated_df.sort_values(by=['Wall Label', 'Pt number'],ascending=False)
   data1 = concatenated_df1.sort_values(by=['Wall Label', 'Pt number'],ascending=False)
      
   # Sidebar to control visibility
   st.markdown('#### Visibility Options')
   wall_labels = data['Wall Label'].unique()
   # print('Segundo print',wall_labels)
   show_wall_label = st.multiselect('Show Wall Label(s)', wall_labels, default=wall_labels)
   
   # Filter data based on user selection
   filtered_data = data[data['Wall Label'].isin(show_wall_label)]
   filtered_data1 = data1[data1['Wall Label'].isin(show_wall_label)]

   # Create Altair chart
   chart = alt.Chart(filtered_data).mark_circle().encode(
      x=alt.X('Mn (kg-m)', title='Mn (kg-m)'),
      y=alt.Y('Pn (kg)', title='Pn (kg)'),
      color=alt.Color('Wall Label'),
      size=alt.Size('Pn (kg)', scale=alt.Scale(domain=[min(data['Pn (kg)']), max(data['Pn (kg)'])]))
   )
   
   chart = alt.Chart(filtered_data).mark_line(point=True).encode(x = 'Mn (kg-m)', y = 'Pn (kg)', color = 'Wall Label',tooltip = ['Wall Label','Mn (kg-m)','Pn (kg)']) + \
               alt.Chart(filtered_data1).mark_line(point=True).encode(x = 'Mn (kg-m)', y = 'Pn (kg)', color = 'Wall Label',tooltip = ['Wall Label','Mn (kg-m)','Pn (kg)'])
   # Display chart
   
   
   st.altair_chart(
       chart, 
       theme="streamlit", use_container_width=True)

   concatenated_df3 = pd.concat([df1,df2,df3,df4])
   datax = concatenated_df3.sort_values(by=['Wall Label', 'Pt number'])   
   Ab_concatenated = datax.to_csv('./outputs/AB_concatenated.csv')

   AB_csv = open("./outputs/AB_concatenated.csv")
   st.download_button(
   label="Download data in csv format",
   data=AB_csv,
   file_name='AB.csv'
   )
      
with tab4:
    st.markdown("""
                
        ## In-Plane Shear Walls Capacities
          
        """
    )

    chart_data = pd.read_csv("./outputs/IPVn.csv")

    st.vega_lite_chart(chart_data, {
    'mark': {'type': 'area', 'tooltip': True},
    'encoding': {
        'x': {'field': 'Wall Label', 'type': 'nominal'},
        'y': {'field': 'Vn (kg)', 'type': 'quantitative'},
        'color': {'field': 'L (m)', 'type': 'quantitative', 'scale': {'scheme': 'Spectral'}},
    },
    })
    
    st.divider()
    st.markdown("""
            
         ## In-Plane Shear Capacities vs Demands
          
            
            """
    )    
    Limit_Line = pd.read_csv("./outputs/LimitLineIPShear.csv")
    VnvsVu = pd.read_csv("./outputs/IPVnvsVu.csv")   
    chart = alt.Chart(Limit_Line).mark_line(color='#DE7417').encode(x = 'Vu (kg)', y = 'Vn (kg)') + \
            alt.Chart(VnvsVu).mark_point().encode(x = 'Vu (kg)', y = 'Vn (kg)',color= {'field': 'Wall Label', 'type': 'nominal', 'scale': {'scheme': 'Spectral'}})
            
    st.altair_chart(
       chart, 
       theme="streamlit", use_container_width=True)
    
    IPVnvsVu_csv = open("./outputs/IPVnvsVu.csv")
    st.download_button(
   label="Download data in csv format",
   data=IPVnvsVu_csv,
   file_name='IPVnvsVu.csv'
   )
   
with tab5:
   st.markdown("""
               
            ## Out of plane Stress Capacities Vs Demands
          
               """
      )  
   
   st.markdown("""
               
            ## Walls in First Floor
            
               """
      )

   Limit_Line = pd.read_csv("./outputs/LimitLineOop_FirstFloor.csv")
   f_OOP_firstFloor = pd.read_csv("./outputs/fnvsfu_oop_firstfloor.csv")   
   chart = alt.Chart(Limit_Line).mark_line(color='#DE3163').encode(x = 'fu (kg/m2)', y = 'fn (kg/m2)') + \
               alt.Chart(f_OOP_firstFloor).mark_point(filled=True).encode(x = 'fu (kg/m2)', y = 'fn (kg/m2)',color= {'field': 'Wall Label', 'type': 'nominal', 'scale': {'scheme': 'Reds'}})
   st.altair_chart(
         chart, 
         theme="streamlit", use_container_width=True) 
   
   fnvsfu_oop_firstfloor_csv = open("./outputs/fnvsfu_oop_firstfloor.csv")
   st.download_button(
   label="Download data in csv format",
   data=fnvsfu_oop_firstfloor_csv,
   file_name='fnvsfu_oop_firstfloor.csv'
   )     
      
   st.divider()
   st.markdown("""
               
            ## Walls in Highest Floor
            
               """
      )

   Limit_Line = pd.read_csv("./outputs/LimitLineOop_HighestFloor.csv")
   f_OOP_HighestFloor = pd.read_csv("./outputs/fnvsfu_oop_highestfloor.csv")   
   chart = alt.Chart(Limit_Line).mark_line(color='#FFBF00').encode(x = 'fu (kg/m2)', y = 'fn (kg/m2)') + \
               alt.Chart(f_OOP_HighestFloor).mark_point(filled=True).encode(x = 'fu (kg/m2)', y = 'fn (kg/m2)',color= {'field': 'Wall Label', 'type': 'nominal', 'scale': {'scheme': 'Oranges'}})
               
   st.altair_chart(
         chart, 
         theme="streamlit", use_container_width=True)

   fnvsfu_oop_highestfloor_csv = open("./outputs/fnvsfu_oop_highestfloor.csv")
   st.download_button(
   label="Download data in csv format",
   data=fnvsfu_oop_highestfloor_csv,
   file_name='fnvsfu_oop_highestfloor.csv')
      
   st.divider()   
   
   st.markdown("""
               
            ## Walls in any Floor
            
               """
      )

   Limit_Line = pd.read_csv("./outputs/LimitLineOop_AnyFloor.csv")
   f_OOP_AnyFloor = pd.read_csv("./outputs/fnvsfu_oop_anyfloor.csv")   
   chart = alt.Chart(Limit_Line).mark_line(color='#CCCCFF').encode(x = 'f_DCR', y = 'Max_DCR') + \
               alt.Chart(f_OOP_AnyFloor).mark_point(filled=True).encode(x = 'f_DCR', y = 'Max_DCR',color= {'field': 'Wall Label', 'type': 'nominal', 'scale': {'scheme': 'Purples'}})
               
   st.altair_chart(
         chart, 
         theme="streamlit", use_container_width=True)   
   
   fnvsfu_oop_anyfloor_csv = open("./outputs/fnvsfu_oop_anyfloor.csv")
   st.download_button(
   label="Download data in csv format",
   data=fnvsfu_oop_anyfloor_csv,
   file_name='fnvsfu_oop_anyfloor.csv')  
   
with tab6:
   st.markdown("""
            
         ## General BackBone Curve
       
            """
    )

   # Sample data
   df1a = pd.read_csv("./outputs/BBC0.csv")
   df2a = pd.read_csv("./outputs/BBC1.csv")
   df3a = pd.read_csv("./outputs/BBC2.csv")
   df4a = pd.read_csv("./outputs/BBC3.csv")
   
   concatenated_df2 = pd.concat([df1a,df2a,df3a,df4a])
   data2 = concatenated_df2.sort_values(by=['Wall Label'])   
   data2.to_csv('./outputs/BBC_Concatenated.csv')
   # Sidebar to control visibility
   st.markdown('#### Visibility Options')
   wall_labels2 = data2['Wall Label'].unique()
  
   show_wall_label2 = st.multiselect('Show Wall Label (s)', wall_labels2, default=wall_labels2)
   
   # Filter data based on user selection
   filtered_data2 = data2[data2['Wall Label'].isin(show_wall_label2)]

   # Create Altair chart
   chart = alt.Chart(filtered_data2).mark_circle().encode(
      x=alt.X('Drift (-)', title='Drift (-)'),
      y=alt.Y('V (kg)', title='V (kg)'),
      color=alt.Color('Wall Label'),
      size=alt.Size('V (kg)', scale=alt.Scale(domain=[min(data2['V (kg)']), max(data2['V (kg)'])]))
   )
   
   chart = alt.Chart(filtered_data2).mark_line(point=True).encode(x = 'Drift (-)', y = 'V (kg)', color = 'Wall Label',tooltip = ['Wall Label','Drift (-)','V (kg)']) 
   # Display chart
   
   st.altair_chart(
       chart, 
       theme="streamlit", use_container_width=True)

   BBC_Concatenated_csv = open("./outputs/BBC_Concatenated.csv")
   st.download_button(
   label="Download data in csv format",
   data=BBC_Concatenated_csv,
   file_name='BBC_Concatenated.csv')  
   

 
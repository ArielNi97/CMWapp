import pandas as pd
import numpy as np
from pathlib import Path
import joblib
import logging
import streamlit as st
import traceback
import os


folder_path = Path(__file__).parent.parent

# Loading Machine Learning Models to predict each variable

Pn = joblib.load(folder_path.joinpath('models/CATB_Pn (kg)_model.pkl')) 
Mn = joblib.load(folder_path.joinpath('models/CATB_Mn (kg-m)_model.pkl'))
V = joblib.load(folder_path.joinpath('models/CATB_V (kg)_model.pkl'))
Vcr = joblib.load(folder_path.joinpath('models/CATB_Vcr (kg)_model.pkl'))
Vm = joblib.load(folder_path.joinpath('models/CATB_Vm (kg)_model.pkl'))
Vu = joblib.load(folder_path.joinpath('models/CATB_Vu (kg)_model.pkl'))
M3 = joblib.load(folder_path.joinpath('models/CATB_M3_0.33Pn (kg-m)_model.pkl'))
M2 = joblib.load(folder_path.joinpath('models/CATB_M2_0.33Pn (kg-m)_model.pkl'))
Driftu = joblib.load(folder_path.joinpath('models/CATB_Drift_u (-)_model.pkl'))
Driftm = joblib.load(folder_path.joinpath('models/CATB_Drift_m (-)_model.pkl'))
Driftcr = joblib.load(folder_path.joinpath('models/CATB_Drift_cr (-)_model.pkl'))
    

# Reading the user input

UserInput = pd.read_csv(folder_path.joinpath('Inputs/InputForML.csv'))
Geometry = pd.read_csv(folder_path.joinpath('Inputs/Input_Walls_geometry.csv'))

## Output csv

Pn_df = pd.DataFrame(Pn.predict(UserInput), columns=['Pn (kg)'])
Pn_final = pd.merge(Geometry[['Wall Label','L']], Pn_df, left_index=True, right_index=True)
Mn_df = pd.DataFrame(Mn.predict(UserInput), columns=['Mn (kg-m)'])
Mn_final = pd.merge(Geometry[['Wall Label','L']], Mn_df, left_index=True, right_index=True)
V_df = pd.DataFrame(V.predict(UserInput), columns=['Vn (kg)'])
V_final = pd.merge(Geometry[['Wall Label','L']], V_df, left_index=True, right_index=True)

## BackBone curve Data 
BB1_df = pd.DataFrame({'V (kg)': Vcr.predict(UserInput),'Drift (-)': Driftcr.predict(UserInput)})
BB1_final = pd.merge(Geometry[['Wall Label']], BB1_df, left_index=True, right_index=True)

BB2_df = pd.DataFrame({'V (kg)': Vm.predict(UserInput),'Drift (-)': Driftm.predict(UserInput)})
BB2_final = pd.merge(Geometry[['Wall Label']], BB2_df, left_index=True, right_index=True)

BB3_df = pd.DataFrame({'V (kg)': Vu.predict(UserInput),'Drift (-)': Driftu.predict(UserInput)})
BB3_final = pd.merge(Geometry[['Wall Label']], BB3_df, left_index=True, right_index=True)

BB0_df = pd.DataFrame({'V (kg)': Vcr.predict(UserInput),'Drift (-)': Driftcr.predict(UserInput)})
BB0_final = pd.merge(Geometry[['Wall Label']], BB0_df, left_index=True, right_index=True)
BB0_final['V (kg)'] = BB1_final['V (kg)']*0
BB0_final['Drift (-)'] = BB1_final['Drift (-)']*0

## Axial Bending Data
## M3 and M2 are inverted

AB2_df = pd.DataFrame({'Mn (kg-m)': M3.predict(UserInput),'Pn (kg)': Pn_df['Pn (kg)']*1/3})
AB2_final = pd.merge(Geometry[['Wall Label']], AB2_df, left_index=True, right_index=True)
AB2_final['Pt number'] = AB2_final['Pn (kg)']/AB2_final['Pn (kg)']*2

AB3_df = pd.DataFrame({'Mn (kg-m)': M2.predict(UserInput),'Pn (kg)': Pn_df['Pn (kg)']*1/3})
AB3_final = pd.merge(Geometry[['Wall Label']], AB3_df, left_index=True, right_index=True)
AB3_final['Pt number'] = AB3_final['Pn (kg)']/AB3_final['Pn (kg)']*3

AB1_final = Mn_final
AB1_final['Pn (kg)'] = AB1_final['Mn (kg-m)']*0
AB1_final['Pt number'] = AB1_final['Pn (kg)']+1

AB4_final = Pn_final
AB4_final['Mn (kg-m)'] = AB4_final['Pn (kg)']*0
AB4_final['Pt number'] = AB4_final['Mn (kg-m)']+4

### Renaming Column

Pn_final = Pn_final.rename(columns={"L": "L (m)"})
Mn_final = Mn_final.rename(columns={"L": "L (m)"})
V_final = V_final.rename(columns={"L": "L (m)"})

# ### Reorganizing Columns

Pn_final = Pn_final.iloc[:, [0,2,1]]
Mn_final = Mn_final.iloc[:, [0,2,1]]
V_final = V_final.iloc[:, [0,2,1]]

AB1_final = AB1_final.iloc[:, [4,0,2,3]]
AB2_final = AB2_final.iloc[:, [3,0,1,2]]
AB3_final = AB3_final.iloc[:, [3,0,1,2]]
AB4_final = AB4_final.iloc[:, [4,0,3,2]]


### Save csv file of predictions

Pn_final.to_csv(folder_path.joinpath('outputs/Pn.csv'), index = False)   
Mn_final.to_csv(folder_path.joinpath('outputs/Mn.csv'), index = False) 
V_final.to_csv(folder_path.joinpath('outputs/IPVn.csv'), index = False) 

BB0_final.to_csv(folder_path.joinpath('outputs/BBC0.csv'), index = False) 
BB1_final.to_csv(folder_path.joinpath('outputs/BBC1.csv'), index = False) 
BB2_final.to_csv(folder_path.joinpath('outputs/BBC2.csv'), index = False) 
BB3_final.to_csv(folder_path.joinpath('outputs/BBC3.csv'), index = False) 

AB1_final.to_csv(folder_path.joinpath('outputs/AB1.csv'), index = False) 
AB2_final.to_csv(folder_path.joinpath('outputs/AB2.csv'), index = False) 
AB3_final.to_csv(folder_path.joinpath('outputs/AB3.csv'), index = False) 
AB4_final.to_csv(folder_path.joinpath('outputs/AB4.csv'), index = False) 



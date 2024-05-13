import pandas as pd
import numpy as np
from pathlib import Path
import joblib
folder_path = Path(__file__).parent.parent

# loading Data and Capacities

LoadInput = pd.read_csv(folder_path.joinpath('Inputs/Input_Walls_Loads.csv'))
Pn_df = pd.read_csv(folder_path.joinpath('outputs/Pn.csv'))
Mn_df = pd.read_csv(folder_path.joinpath('outputs/Mn.csv'))
Vn_df = pd.read_csv(folder_path.joinpath('outputs/IPVn.csv'))

# Preparing data for the 1v1 plots

PnvsPu = pd.merge(LoadInput[['Wall Label','P (kg)']], Pn_df, on = 'Wall Label')
PnvsPu = PnvsPu.rename(columns={"P (kg)": "Pu (kg)"})
PnvsPu = PnvsPu.iloc[:, [0,2,3,1]]

MnvsMu = pd.merge(LoadInput[['Wall Label','Mip (kg-m)']], Mn_df, on = 'Wall Label')
MnvsMu = MnvsMu.rename(columns={"Mip (kg-m)": "Mu (kg-m)"})

MnvsMu = MnvsMu.iloc[:, [0,2,3,1]]

IPVnvsVu = pd.merge(LoadInput[['Wall Label','V (kg)']], Vn_df, on = 'Wall Label')
IPVnvsVu = IPVnvsVu.rename(columns={"V (kg)": "Vu (kg)"})
IPVnvsVu = IPVnvsVu.iloc[:, [0,2,3,1]]


LimitLineAxial = pd.DataFrame({'Pu (kg)': [0,np.max(PnvsPu['Pn (kg)'])],'Pn (kg)': [0,np.max(PnvsPu['Pn (kg)'])]})
LimitLineBending = pd.DataFrame({'Mu (kg-m)': [0,np.max(MnvsMu['Mn (kg-m)'])],'Mn (kg-m)': [0,np.max(MnvsMu['Mn (kg-m)'])]})
LimitLineIPShear = pd.DataFrame({'Vu (kg)': [0,np.max(IPVnvsVu['Vn (kg)'])],'Vn (kg)': [0,np.max(IPVnvsVu['Vn (kg)'])]})

## Saving the data
PnvsPu.to_csv(folder_path.joinpath('outputs/PnvsPu.csv'), index = False)   
MnvsMu.to_csv(folder_path.joinpath('outputs/MnvsMu.csv'), index = False) 
IPVnvsVu.to_csv(folder_path.joinpath('outputs/IPVnvsVu.csv'), index = False) 

LimitLineAxial.to_csv(folder_path.joinpath('outputs/LimitLineAxial.csv'), index = False)   
LimitLineBending.to_csv(folder_path.joinpath('outputs/LimitLineBending.csv'), index = False) 
LimitLineIPShear.to_csv(folder_path.joinpath('outputs/LimitLineIPShear.csv'), index = False) 


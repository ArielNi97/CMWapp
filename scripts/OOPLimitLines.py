import pandas as pd
import numpy as np
from pathlib import Path
import joblib
folder_path = Path(__file__).parent.parent

# loading Data and capacities

fnvsfu_AF = pd.read_csv(folder_path.joinpath('outputs/fnvsfu_oop_anyfloor.csv'))
fnvsfu_FF = pd.read_csv(folder_path.joinpath('outputs/fnvsfu_oop_firstfloor.csv'))
fnvsfu_HF = pd.read_csv(folder_path.joinpath('outputs/fnvsfu_oop_highestfloor.csv'))

# Preparing data for the 1v1 plots

LimitLineOop_FirstFloor = pd.DataFrame({'fu (kg/m2)': [np.max(fnvsfu_FF['fn (kg/m2)']),np.max(fnvsfu_FF['fn (kg/m2)'])],'fn (kg/m2)': [0,np.max(fnvsfu_FF['fn (kg/m2)'])]})
LimitLineOop_HighestFloor = pd.DataFrame({'fu (kg/m2)': [np.max(fnvsfu_HF['fn (kg/m2)']),np.max(fnvsfu_HF['fn (kg/m2)'])],'fn (kg/m2)': [0,np.max(fnvsfu_HF['fn (kg/m2)'])]})
LimitLineOop_AnyFloor = pd.DataFrame({'f_DCR': [np.max(fnvsfu_AF['Max_DCR']),np.max(fnvsfu_AF['Max_DCR'])],'Max_DCR': [0,np.max(fnvsfu_AF['Max_DCR'])]})

## Saving the data

LimitLineOop_FirstFloor.to_csv(folder_path.joinpath('outputs/LimitLineOop_FirstFloor.csv'), index = False)   
LimitLineOop_HighestFloor.to_csv(folder_path.joinpath('outputs/LimitLineOop_HighestFloor.csv'), index = False) 
LimitLineOop_AnyFloor.to_csv(folder_path.joinpath('outputs/LimitLineOop_AnyFloor.csv'), index = False) 


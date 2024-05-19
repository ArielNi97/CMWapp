import pandas as pd
import numpy as np



def run_OOPLimit_Lines():
    # loading Data and capacities

    fnvsfu_AF = pd.read_csv('outputs/fnvsfu_oop_anyfloor.csv')
    fnvsfu_FF = pd.read_csv('outputs/fnvsfu_oop_firstfloor.csv')
    fnvsfu_HF = pd.read_csv('outputs/fnvsfu_oop_highestfloor.csv')

    # Preparing data for the 1v1 plots

    LimitLineOop_FirstFloor = pd.DataFrame({'fu (kg/m2)': [np.max(fnvsfu_FF['fn (kg/m2)']),np.max(fnvsfu_FF['fn (kg/m2)'])],'fn (kg/m2)': [0,np.max(fnvsfu_FF['fn (kg/m2)'])]})
    LimitLineOop_HighestFloor = pd.DataFrame({'fu (kg/m2)': [np.max(fnvsfu_HF['fn (kg/m2)']),np.max(fnvsfu_HF['fn (kg/m2)'])],'fn (kg/m2)': [0,np.max(fnvsfu_HF['fn (kg/m2)'])]})
    LimitLineOop_AnyFloor = pd.DataFrame({'f_DCR': [np.max(fnvsfu_AF['Max_DCR']),np.max(fnvsfu_AF['Max_DCR'])],'Max_DCR': [0,np.max(fnvsfu_AF['Max_DCR'])]})

    ## Saving the data

    LimitLineOop_FirstFloor.to_csv('outputs/LimitLineOop_FirstFloor.csv', index = False)   
    LimitLineOop_HighestFloor.to_csv('outputs/LimitLineOop_HighestFloor.csv', index = False) 
    LimitLineOop_AnyFloor.to_csv('outputs/LimitLineOop_AnyFloor.csv', index = False) 

if __name__ == "__main__":
    run_OOPLimit_Lines()
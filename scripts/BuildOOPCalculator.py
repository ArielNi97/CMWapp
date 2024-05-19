import pandas as pd
import numpy as np
from pathlib import Path
from scripts.ConfinedMasonryWallsE070_OOP_f import OOPlaneStresses_E070_f
from scripts.ConfinedMasonryWallsE070_OOP_m import *
from scripts.ConfinedMasonryWallsE070_OOP_Ms import OOPlaneSeismicMoment_E070_Ms
from scripts.ConfinedMasonryWallsE070_OOP_Mt import OOPlaneMoment_E070_Mt
from scripts.ConfinedMasonryWallsE070_OOP_W import *
import sys



def g(x):
    if x['t'] == 0.10: return 68/129
    elif x['t'] == 0.15: return 48.75/93
    elif x['t'] == 0.2: return 42/80
    else: return 0

 
def run_BuildOOP_calculator(): 
    # loading Input data

    LoadInput = pd.read_csv('Inputs/Input_Walls_Loads.csv')
    GeometricInput = pd.read_csv('Inputs/Input_Walls_geometry.csv')
    BoundaryConditionInput = pd.read_csv('Inputs/Input_Walls_Case.csv')
    LocationInput = pd.read_csv('Inputs/Input_Walls_Location.csv')
    MaterialInput = pd.read_csv('Inputs/Input_Walls_Material.csv')

    GeometricInput['Case'] = GeometricInput['L']/GeometricInput['L']*BoundaryConditionInput['Case'].values.tolist()[0]
    GeometricInput['Case'] = GeometricInput['Case'].astype('int')
    GeometricInput['a'] = GeometricInput['L']/GeometricInput['L']*LocationInput['a'].values.tolist()[0]
    GeometricInput['Fs'] = GeometricInput['L']/GeometricInput['L']*LocationInput['Fs'].values.tolist()[0]
    GeometricInput['I'] = GeometricInput['L']/GeometricInput['L']*LocationInput['I'].values.tolist()[0]
    GeometricInput['P (kg)'] = GeometricInput['L']/GeometricInput['L']*LoadInput['P (kg)']

    ### Generating sum of P per each story and sum of V
    df = pd.DataFrame(LoadInput.groupby('Level')['P (kg)'].sum())
    df = df.reset_index(names=['Level', 'P (kg)'])
    df = df.rename(columns={'P (kg)':'Sum_P'})
    WALLS = GeometricInput.merge(df[['Sum_P','Level']], on='Level')


    df1 = pd.DataFrame(LoadInput.groupby('Level')['V (kg)'].sum())
    df1 = df1.reset_index(names=['Level', 'V (kg)'])
    df1 = df1.rename(columns={'V (kg)':'Sum_V'})
    WALLs = WALLS.merge(df1[['Sum_V','Level']], on='Level')


    WALLs['fm (kg/cm2)'] = GeometricInput['L']/GeometricInput['L']*MaterialInput['fm'].values.tolist()[0]
    WALLs['factor'] = GeometricInput.apply(g, axis=1)
    WALLs['Pe'] = GeometricInput['t']*WALLs['factor']*1800
    WALLs['Hw'] = (GeometricInput['H'] - 2*GeometricInput['hb'])/2
    WALLs['Lw'] = GeometricInput['L'] - 2*WALLs['wc']


    ## Dropping unneeded columns

    Walls = WALLs.drop(['hc',  'wb', 'hb', 'wc'], axis =1)

    ## Computing W

    Walls['w'] = Walls.apply(W, axis=1)

    ## Computing m

    Walls['m'] = Walls.apply(M, axis=1)

    # Acceleration is subtituted by a new variable called a that is used to be passed on the following parameter function
    Walls['a'] = Walls.apply(A, axis=1)

    ## Computing Ms

    Walls['ms'] = OOPlaneSeismicMoment_E070_Ms(Walls).Ms()

    ## Computing Mt

    Walls['mt'] = OOPlaneMoment_E070_Mt(Walls).Mt()

    ## Computing stresses

    Walls['fa'] = OOPlaneStresses_E070_f(Walls).fa()
    Walls['Fa'] = OOPlaneStresses_E070_f(Walls).Fa()
    Walls['fm'] = OOPlaneStresses_E070_f(Walls).fm()
    Walls['Fm'] = OOPlaneStresses_E070_f(Walls).Fm()
    Walls['ft'] = OOPlaneStresses_E070_f(Walls).ft()

    ## Dropping unneded columns

    Walls = Walls.drop(['L',  'H', 't','Case','a','P (kg)','Fs','I','fm (kg/cm2)','Pe','w','factor','m','ms','mt', 'Sum_P','Sum_V', 'Hw', 'Lw'], axis =1)

    Walls['L (m)'] = GeometricInput['L']

    Walls1 = Walls

    # Preparing Outputs for the three graphics
    ## First output


    Walls1['fu (kg/m2)'] = Walls1['fa'] + Walls1['fm']

    Walls1['fn (kg/m2)'] = 0.25*WALLs['fm (kg/cm2)']*WALLs['factor']*10000

    Walls1_filtered = Walls1[Walls1['Level'] ==  min(Walls1['Level'])]


    fnvsfu_oop_firstfloor = Walls1_filtered.iloc[:, [0,9,7,8]]
    # print(fnvsfu_oop_firstfloor)



    ## Second output

    Walls2 = Walls

    Walls2['f_DCR'] = Walls2['fa']/Walls2['Fa'] + Walls2['fm']/Walls2['Fm']

    Walls2['Max_DCR'] = Walls2['Fa']/Walls2['Fa']*1.33

    fnvsfu_oop_anyfloor = Walls2.iloc[:, [0,11,7,10]]
    # print(fnvsfu_oop_anyfloor)
    ## Third output

    Walls3 = Walls

    Walls3['fu (kg/m2)'] =  Walls3['fm'] - Walls3['fa'] 

    Walls3['fn (kg/m2)'] = Walls3['ft']

    Walls3_filered = Walls3[Walls3['Level'] ==  max(Walls1['Level'])]
    fnvsfu_oop_highestfloor = Walls3_filered.iloc[:, [0,9,7,8]]
    # print(fnvsfu_oop_highestfloor)


    # Save csv files

    fnvsfu_oop_firstfloor.to_csv('outputs/fnvsfu_oop_firstfloor.csv', index = False)
    fnvsfu_oop_anyfloor.to_csv('outputs/fnvsfu_oop_anyfloor.csv', index = False)
    fnvsfu_oop_highestfloor.to_csv('outputs/fnvsfu_oop_highestfloor.csv', index = False)

if __name__ == "__main__":
    run_BuildOOP_calculator()
import pandas as pd
import numpy as np



def g(x):
    if x['Espesor (cm)'] == 10: return 68/129
    elif x['Espesor (cm)'] == 15: return 48.75/93
    elif x['Espesor (cm)'] == 20: return 42/80
    else: return 0  


def run_build_ml_input_file():
    ## Reading Files 

    WallGeometry = pd.read_csv('Inputs/Input_Walls_geometry.csv')
    WallMaterial = pd.read_csv('Inputs/Input_Walls_Material.csv')
    WallRebars = pd.read_csv('Inputs/Input_Walls_rebars.csv')


    ## Adding the materials for the dataset

    WallGeometry['fy (kg/cm2)'] = WallGeometry['L']/WallGeometry['L']*WallMaterial['fy'].values.tolist()[0]
    WallGeometry['fc (kg/cm2)'] = WallGeometry['L']/WallGeometry['L']*WallMaterial['fc'].values.tolist()[0]
    WallGeometry['fm (kg/cm2)'] = WallGeometry['L']/WallGeometry['L']*WallMaterial['fm'].values.tolist()[0]
    Walls = WallGeometry.merge(WallRebars[['Wall Label','Rebars']], on='Wall Label')

    ## Generating the Steel rebar Area

    Walls['BarQuantity'] = Walls['Rebars'].str.extract('(\d+)').astype(int)
    Walls['BarType'] = Walls['Rebars'].str.extract(r'(?<=#)(\d+)', expand=False).fillna(0).astype(int)
    Walls['Asu1'] = Walls['BarQuantity']*(Walls['BarType']/8*2.54)**2/4*np.pi

    ## Converting from m to cm some inputs

    Walls['Longitud (cm)'] = Walls['L']*100
    Walls['Espesor (cm)'] = Walls['t']*100
    Walls['Altura (cm)'] = Walls['H']*100
    Walls['Ancho (cm)'] = Walls['wc']*100

    ## Dropping unnecessary columns

    Walls = Walls.drop(['Wall Label','Level','BarQuantity', 'BarType','Rebars','hc',  'wb', 'hb','L','H','t','wc'], axis =1)

    ## Generating parameters used to make the dataframe complete

    Walls["v_prime_m"] = np.minimum(0.8*np.sqrt(Walls["fm (kg/cm2)"]),6)
    Walls["Inercia"] = 1/12* Walls["Longitud (cm)"]* (Walls["Espesor (cm)"])**3 # This because can buckle in the oop direction
    Walls["Area gross Percentage"] = Walls.apply(g, axis=1)
    Walls["Area_neta"] = Walls["Area gross Percentage"] * Walls["Espesor (cm)"] * Walls["Longitud (cm)"]
    Walls["radio_giro"] = np.sqrt(Walls["Inercia"]/(Walls["Area_neta"]))

    Walls_sorted = Walls.iloc[:, [4,5,2,6,8,9,10,11,12,3,7,0,1]]
    Walls_sorted.to_csv('Inputs/InputForML.csv', index = False)  

if __name__ == "__main__":
    run_build_ml_input_file()
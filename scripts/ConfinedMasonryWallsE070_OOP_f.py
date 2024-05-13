import numpy as np
import pandas as pd
from sympy import init_printing
from pathlib import Path
# import handcalcs.render
import math
from math import sqrt
import itertools
import matplotlib.pyplot as plt
#Formato latex al output
init_printing(use_latex="mathjax")
#Automatizando el path del documento.
path = Path().resolve()
import seaborn as sns
from pandas.plotting import scatter_matrix
from matplotlib.patches import Polygon
   


     
     
class OOPlaneStresses_E070_f:
 
     def __init__ (self, Walls_df):
        # Walls_df()
        """
        h: [m] = Altura total del muro.
        t: 0.15 Default [m] =  Espesor del muro de mamposteria.
        f_m: 45 [kg/cm2] = Esfuerzo de la mamposteria sobre area bruta
        pg: [kg] =  Carga axial actuante en el muro
        l: [m] = Longitud total del muro incluyendo columnas.
        mt: [kg-m/m] = Momento flector generado por la carga sismica fuera del plano + la carga gravitacional por la excentricidad
        
        """

        self.t = Walls_df['t']
        self.f_m = Walls_df['fm (kg/cm2)']*Walls_df['factor']*10000
        self.h = Walls_df['H']
        self.l = Walls_df['L']
        self.pg = Walls_df['P (kg)']
        self.mt = Walls_df['mt']

      
        
     def fa(self): 
        
         self.fa1 = self.pg/(self.t) # Esfuerzo axial actuante en el muro
   
         return self.fa1      
     
     def Fa(self): 
        
         self.Fa1 = 0.20*self.f_m*(1 - (self.h/(35*self.t))**2) # Esfuerzo resistente axial del muro
         return self.Fa1 
     
     def fm(self): 
        
         self.fm1 = 6*self.mt/self.t**2# Esfuerzo a flexion actual en el muro
   
         return self.fm1
     
     def Fm(self): 
        
         self.Fm1 = 0.4*self.f_m # Esfuerzo a flexion actual en el muro
   
         return self.Fm1
     
     def ft(self):
         
         self.ft1 = 0.8*3*10000 # [kg/m2] esfuerzo maximo para mamposteria confinada simple
         
         return self.ft1
     
     
     
        
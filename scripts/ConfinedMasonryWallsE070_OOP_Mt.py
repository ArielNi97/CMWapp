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
   


     
     
class OOPlaneMoment_E070_Mt:
 
     def __init__ (self,Walls_df):
        
        """
        ms: [kg-m/m] = Momento flector generado por la carga sismica fuera del plano
        t: 0.15 Default [m] =  Espesor del muro de mamposteria.
        l: [m] = Longitud total del muro incluyendo columnas.
        pg: [kg] = Carga axial total actuante en el muro.
        """        
        
        self.ms = Walls_df['ms']
        self.t = Walls_df['t']
        self.l = Walls_df['L']
        self.pg = Walls_df['P (kg)']

        
     def Mt(self): 
        
         self.e = self.t*0.10 # 10% del espesor del muro se tomaría como la excentricidad para la carga gravitacional
         self.mg = self.pg*self.e
         self.mt = self.ms + self.mg
         

         return self.mt       
     
     
        
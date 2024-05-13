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
   


     
     
class OOPlaneSeismicMoment_E070_Ms:
 
     def __init__ (self, Walls):

        """
        m: [-] = Coeficiente de momento indicado en la tabla 23
        a: [m] = Dimension critica del paño de albañileria de tabla 23 (Longitud del muro)
        w: [kg/m2] = Magnitud de carga fuera del plano por unidad de area del muro.
        
        Tomado de Articulo 68 de la norma E070 de peru.
        """ 
 
        self.m = Walls['m']
        self.w = Walls['w']
        self.a = Walls['a']
      
        
     def Ms(self): 
 
         self.ms = self.m*self.w*self.a**2
         
         return self.ms       
     
     
        
     
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
   


def W(X): 
    if X['Level'] == 1: return  0.4*X['a']*X['I']*X['Fs']*X['Pe']
    elif X['Level'] != 1: return 0.3*X['Sum_V']/X['Sum_P']*2*X['Pe'] 
    else: return 0        

     
        
 
    
   
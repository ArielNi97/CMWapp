import numpy as np
import pandas as pd
from sympy import init_printing
from pathlib import Path
from math import sqrt
#Formato latex al output
init_printing(use_latex="mathjax")
#Automatizando el path del documento.
path = Path().resolve()


def M(x):
     
     if x['Case'] == 2: 
          
          a = x['Lw']
          b = x['Hw']  
               
          if b/a <= 0.5:
                    m = 0.060
                         
          elif b/a <= 0.6:
                    m = 0.074

          elif b/a <= 0.7:
                    m = 0.087
                    
          elif b/a <= 0.8:
                    m = 0.097
                    
          elif b/a <= 0.9:
                    m = 0.106
                    
          elif b/a <= 1.0:
                    m = 0.112        

          elif b/a <= 1.5:
                    m = 0.128 

          elif b/a <= 2:
                    m = 0.132
                              
          else:
                    m = 0.133
                    
     else:
          
          if x['Lw']  <= x['Hw'] :
               a = x['Lw'] 
               b = x['Hw'] 
               
               if b/a <= 1:
                    m = 0.060
                    
               elif b/a <= 1.2:
                    m = 0.074

               elif b/a <= 1.4:
                    m = 0.087
               
               elif b/a <= 1.6:
                    m = 0.097
               
               elif b/a <= 1.8:
                    m = 0.106
               
               elif b/a <= 2.0:
                    m = 0.112        

               elif b/a <= 3.0:
                    m = 0.128 
                         
               else:
                    m = 0.125 
                    
          
          elif x['Lw']  > x['Hw']:
               
               a = x['Hw']
               b = x['Lw'] 
               
               if b/a <= 1:
                    m = 0.0479
                         
               elif b/a <= 1.2:
                    m = 0.0627

               elif b/a <= 1.4:
                    m = 0.0755
                    
               elif b/a <= 1.6:
                    m = 0.0862
                    
               elif b/a <= 1.8:
                    m = 0.0948
                    
               elif b/a <= 2.0:
                    m = 0.1017       

               elif b/a <= 3.0:
                    m = 0.118
                              
               else:
                    m = 0.125   

     return m



def A(x):
     
     if x['Case'] == 2: 
          
          a = x['Lw']
          b = x['Hw']  
                    
     else:
          
          if x['Lw']  <= x['Hw'] :
               a = x['Lw'] 
               b = x['Hw']                
          
          elif x['Lw']  > x['Hw']:
               
               a = x['Hw']
               b = x['Lw'] 
                 
     return a
# # # # # # # # # # # # # # # # # # # # #
#                                       #
#   Author: Rishabh Mehta               #
#                                       #
#   Subroutine for Diagonalisation      #
#                                       #
# # # # # # # # # # # # # # # # # # # # # 

import sympy
import numpy as np

M = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]

def Diagonalise(M):
  Mat = sympy.Matrix(M)
  
  
  # Use sympy.diagonalize() method 
  P, D = Mat.diagonalize()  
        
  Diago = np.array(D).astype(np.float64)
  print(Diago)

Diagonalise(M)
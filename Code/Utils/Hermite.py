# # # # # # # # # # # # # # # # # # # # #
#                                       #
#   Author: Rishabh Mehta               #
#                                       #
#   Function for returning the          #
#   respective Hermite polynomial       #
#                                       #
# # # # # # # # # # # # # # # # # # # # #

import numpy as np
import sympy as sp

x = sp.symbols('x')
symArr = [1, 2*x]

def Hermite():

  for n in range (1, 4):
    symArr.append(2*x*symArr[n] - 2*n*symArr[n-1])

  print(symArr)
Hermite()

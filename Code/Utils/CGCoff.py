# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                         #
#   Author: Rishabh Mehta                                 #
#                                                         #
#   Function for returning Clebsch-Gordan                 # 
#   coefficients of a given number                        #
#                                                         #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

from Factorial import Factorial
import math

# Function for checking triangular condition on j1, j2 and j
def isTriangle(a, b, c):
     
  # check condition
  if (a + b < c) or (a + c < b) or (b + c < a) :
      return False

  return True

# Function for checking zero condition on m/j
def isZero(a, b):

  # check condition
  if (a*b == 0):
    return True

  return False

# Function for returning Clebsch-Gordan coefficients
def CGCoff(j1, j2, j, m1, m2, m):

  if (m1 + m2 == m) and isTriangle(j1, j2, j):  # checks triangular condition

    if isZero(m1, m2) or isZero(j1, j2): return 1  # checks zero condition

    # Calculation of first two terms of CG coffs
    term1 = (2*j + 1)*Factorial(int(j1+j2-j))*Factorial(int(j+j1-j2))*Factorial(int(j+j2-j1))/Factorial(int(j1+j2+j+1))
    term2 = Factorial(int(j1+m1))*Factorial(int(j1-m1))*Factorial(int(j2+m2))*Factorial(int(j2-m2))*Factorial(int(j+m))*Factorial(int(j-m))
    term3 = 0

    # Calculation of the last term of CG coffs
    termList = [
      j1 + j2 - j,
      j1 - m1,
      j2 + m2,
      j2 - j - m1,
      j1 + m2 - j
    ]

    # calculation of range of v
    minV = max(termList[3:]) if max(termList[3:]) > 0 else 0
    maxV = min(termList[:3])

    # loop for term3 calculation
    for v in range(int(minV), int(maxV) + 1):

      num = (-1 if v%2 != 0 else 1)/Factorial(int(v))
      den = Factorial(int(termList[0] - v))*Factorial(int(termList[1] - v))*Factorial(int(termList[2] - v))*Factorial(int(v - termList[3]))*Factorial(int(v - termList[4]))
      term3 += num/den

    coff = math.sqrt(term1)*math.sqrt(term2)*term3
    return coff # final result

  return 0

print(CGCoff(2, 2, 0, 1, -1, 0))
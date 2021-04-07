# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                         #
#   Author: Rishabh Mehta                                 #
#                                                         #
#   Function for returning factorial  of a given number   #
#                                                         #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Array for accessing already stored factorials for optimisation 
factArray = [1, 1, 2]

def Factorial(n):

  if (len(factArray) <= n):
    
    for i in range (len(factArray), n+1):
      factArray.append(factArray[i-1]*i)

  return factArray[n]


# # # # # # # # # # # # # # # # # # # # #
#                                       #
#   Author: Rishabh Mehta               #
#                                       #
#   Subroutine for Simpson Integration  #
#                                       #
# # # # # # # # # # # # # # # # # # # # # 

# Function for calculating integral using Simpson's rule
def SimpsonI(F, h):

    I = F[0] + F[len(F) - 1]

    I += sum([4*F[i] for i in range (1, len(F)-1, 2)])
    I += sum([2*F[i] for i in range (2, len(F)-1, 2)])

    I = I*h/3.

    return I




import numpy as np
import math as mt
import matplotlib.pyplot as plt
from Utils.CGCoff import CGCoff

# Constants
kappa = np.array([0.05 for i in range(8)])
mu = np.array([0., 0., 0., .35, .625, .630, .448, .434])

# Main loop
for N in range(0, 15, 2):
    for O in range (1, N+2, 2):

        # start basis counter
        nBas = 0
        l_arr = []
        lmbda_arr = []
        sigma_arr = []

        # start basis loop
        for l in range(N, -1, -4):
            for lmbda in range(-l, l+1, 2):

                sigma = O - lmbda
                if abs(sigma) != 1: continue
                
                nBas += 1
                l_arr.append(l)
                lmbda_arr.append(lmbda)
                sigma_arr.append(sigma)

        # start deformation loop
        for dfm in np.arange(-.3,0.301,0.01):

            fdel = mt.pow((1 + (2/3)*dfm)*(1 + (2/3)*dfm)*(1-(4/3)*dfm), -1/6)
            
            w00 = 1
            w0 = w00*fdel

            C = -2*w00*kappa[int(N/2)]
            D = 0.5*C*mu[int(N/2)]

            H_mat = np.zeros(shape=(nBas,nBas))
            # start matrix element loop
            for i in range(1, nBas+1):

                l_i = l_arr[i-1]
                lmbda_i = lmbda_arr[i-1]
                sigma_i = sigma_arr[i-1]

                for j in range(i, nBas+1):

                    l_j = l_arr[j-1]
                    lmbda_j = lmbda_arr[j-1]
                    sigma_j = sigma_arr[j-1]

                    # initialise all matrix elements
                    H00 = 0
                    Hl2 = 0
                    Hls = 0
                    Hr2 = 0
                    HY20 = 0

                    if i == j:
                        H00 = w0*(N+3)/2
                        Hl2 = l*(l+2)/4

                    if l_i == l_j:
                        Hr2 = (N + 3)/2

                        if (lmbda_j == l_i + 2) and (sigma_j == sigma_i -2):
                            Hls = mt.sqrt((l_i - lmbda_i)*(l_i + lmbda_i + 2))/4

                        elif (lmbda_j == l_i) and (sigma_j == sigma_i):
                            Hls = lmbda_i*sigma_i/4

                        elif (lmbda_j == l_i - 2) and (sigma_j == sigma_i + 2):
                            Hls = mt.sqrt((l_i + lmbda_i)*(l_i - lmbda_i + 2))/4

                    elif l_j == l_i - 4:
                        Hr2 = mt.sqrt((N - l_i + 4)*(N + l_i + 2))/2

                    elif l_j == l_i + 4:
                        Hr2 = mt.sqrt((N - l_i)*(N + l_i + 6))/2

                    if (abs(Hr2) > 1e-5) and (lmbda_i == lmbda_j):
                        HY20 = mt.sqrt((l_i + 1)/(l_j + 1))*\
                            CGCoff(l_i, 4, l_j, lmbda_i, 0, lmbda_j)*\
                            CGCoff(l_i, 4, l_j, 0, 0, 0)

                    Hdel = -dfm*w0*2*Hr2*HY20/3
                    H_mat[i-1,j-1] = H00 + Hdel + C*Hls + D*Hl2
                    H_mat[j-1, i-1] = H_mat[i-1, j-1]

            # Finding Eigen values
            egnval, egnvc = np.linalg.eig(H_mat)
            egnval = egnval.reshape(1,len(egnval))

            temp = np.zeros((nBas,1))
            temp = dfm
            plt.plot(temp, egnval, '.',markersize=0.8,linewidth=None,c='black')

plt.ylim([2., 5.])
plt.show()








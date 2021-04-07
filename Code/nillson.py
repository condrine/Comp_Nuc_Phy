import scipy as sc
import numpy as np
import math as mt
import matplotlib.pyplot as plt
from Utils.CGCoff import CGCoff

kappa = np.array([0.05 for i in range(8)])
mu = np.array([0., 0., 0., .35, .625, .630, .448, .434])

pi = 3.14159 #26536897932384626

l_arr = []
Lambda_arr = []
Sigma_arr = []

for N in range(8):
	for Omega in np.arange(0.5,N+1):
		nbas = 0
		l_arr = []
		Lambda_arr = []	
		Sigma_arr = []

		for l in range(N,-1,-2):
			for Lambda in range(-l,l+1):
				Sigma = Omega - Lambda
				#print(Sigma)
				if (abs(Sigma-0.5)>1e-5): continue;
				#print("here")
				nbas += 1 
				l_arr.append(l)
				Lambda_arr.append(Lambda)
				Sigma_arr.append(Sigma)

		#H_arr = np.zeros(shape=(nbas,nbas))	

		for defm in np.arange(-.3,0.3,0.01):
			H_arr = np.zeros(shape=(nbas,nbas))
			fdefm = mt.pow(((1.0+(2.0/3.0)*defm)**2)*(1-(4.0/3.0)*defm),-1.0/6.0)
			w00 = 1.0
			w0 = w00*fdefm

			C = -2.0*kappa[N]*w00
			D = mu[N]*C/2.0

			for i in range(0,nbas):
				l_i = l_arr[i]
				Lambda_i = Lambda_arr[i]
				Sigma_i = Sigma_arr[i] 
				for j in range(i,nbas):
					l_j = l_arr[j]
					Lambda_j = Lambda_arr[j]
					Sigma_j = Sigma_arr[j]

					H00=0.0
					Hl2=0.0
					Hls=0.0
					Hr2=0.0
					Hy20=0.0
					if(i == j):
						H00 = (N+1.5)*w0
						Hl2 = l*(l+1)
					if(l_i == l_j):
						if ((Lambda_i == Lambda_j+1) & (Sigma_i == Sigma_j-1)):
							Hls = 0.5*mt.sqrt((l_j-Lambda_j)*(l_j+Lambda_j+1))
						if ((Lambda_i == Lambda_j-1) & (Sigma_i == Sigma_j+1)):
							Hls = 0.5*mt.sqrt((l_j+Lambda_j)*(l_j-Lambda_j+1))
						if ((Lambda_i == Lambda_j) & (Sigma_i == Sigma_j)):
							Hls = Lambda_j * Sigma_j
						Hr2 = (N+1.5)
					
					elif (l_i == l_j-2):
						Hr2 = mt.sqrt((N-l_j+2)*(N+l_j+1))
					elif (l_i == l_j+2):
						Hr2 = mt.sqrt((N-l_j)*(N+l_j+3))

					if ((abs(Hr2)>1e-5) and (Lambda_i==Lambda_j)):
						Hy20 = mt.sqrt((5*(2*l_j+1))/(4*pi*(2*l_i+1)))*CGCoff(l_j,2,l_i,Lambda_j, 0, Lambda_i)*CGCoff(l_j, 2, l_i,0,0,0)
					
					Hdefm = -defm*w0*(4.0/3.0)*mt.sqrt((pi/5.0))*Hr2*Hy20		
					H_arr[i,j] = H00 + Hdefm + C*Hls + D*Hl2
					H_arr[j,i] = H_arr[i,j]

			egnval, egnvc = np.linalg.eig(H_arr)
			egnval = egnval.reshape(1,len(egnval))
			#print(egnval)
			#print((H_arr))
			# print(np.shape(egnval))
			# print(np.shape(egnvc))
			#print(nbas)
			temp = np.zeros((nbas,1))
			temp = defm
			plt.plot(temp, egnval, ".")
plt.show()
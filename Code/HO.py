import numpy as np
import math as mt
import matplotlib.pyplot as plt
import scipy.constants as spc

# equation constants
m  = spc.hbar
omega = 1.

# program consts
Nx = 60
Xmax = 5.
dx = 2*Xmax/Nx
X = np.linspace(-Nx/2, Nx/2, num=Nx+1)*dx
Xi = mt.sqrt(m*omega/spc.hbar)*X
col = ['r', 'g', 'b', 'c', 'm', 'y']

# Initialisation
norm = mt.sqrt(mt.sqrt(m*omega/(spc.hbar*mt.pi)))
H0 = 1*np.ones(Nx + 1)
H1 = 2*Xi

# loop
for n in range(0, 50):
    
    H = (n==0)*H0 + (n==1)*H1 + (n>1)*(2*Xi*H1 -2*(n-1)*H0)
    norm = norm if n==0 else norm/mt.sqrt(2.*n)

    Psi = norm*H*np.exp(-0.5*np.square(Xi))
    if (n > 1):
        H0 = H1
        H1 = H

    if (n == 48):
        plt.plot(X, Psi, col[n%6], label="n = {}".format(n))

# plot
plt.legend()
plt.xlabel("x", fontsize=15)
plt.ylabel(r'$\psi_n(x)$', fontsize=15)
plt.title("Harmonic Oscillator Wavefunctions")
plt.savefig("../Results/HO.png")
plt.show()

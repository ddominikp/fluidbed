import numpy as np
import math as m
from scipy import constants as const

"""Helper package containing useful fludised bed correlations, using numericalunits as a unit base"""
    
def diam_V(V_p):
    """Average volumetric diameter [m] - the diameter of a sphere with the same volume [m^3] as the particle volume"""
    d_V = np.power( 6*V_p/const.pi ,1.0/3) 
    return d_V

def diam_A(A_p):
    """Average area diameter [m] - the diameter of a sphere with the same area [m^2] as the particle area"""
    d_A = np.power( A_p/const.pi, 1.0/2)
    return d_A

def diam_VA(V_p, A_p):
    """Sauter mean diameter of a particle [m]"""
    d_AV = ( np.power( diam_V(V_p), 3 ) / np.power(diam_A(A_p), 2) )
    return d_AV

diam_32 = diam_VA #Function alias 

def shape_f(A_p, A_s):
    """Particle shape factor [-]"""
    phi = A_p / A_s
    return phi

def spher_f(A_p, A_s):
    """Particle sphericity"""
    psi = 1.0/shape_f(A_p, A_s)
    return psi


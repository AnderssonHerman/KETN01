"""
cstr.py
"""
import numpy as np

def cstrModel(t, y):   
    # Unknown variables
    C = y[0]
    T = y[1]

    # Parameters
    q   = 1.1       # m3/h
    C0  = 9000    #mol/m^3
    T0  = 273+21   # K
    V   = 1.3       # m^3
    k0  = 6.99E10  # h^-1
    Ea  = 69.418   # kJ/mol
    R   = 0.00833  # kJ/(mol K)
    rho = 800  # kg/m^3
    Cp  = 3.142  # kJ/(kg K)
    dH  = -69.9  # kJ/mol
    U   = 2570  # kJ/(h m^2 K)
    A   = 3    # m^2

    # Equations
    k   = k0*np.exp(-Ea/(R*T))
    ra  = k*C
    Tj  = 273+27

    # Balances
    resCB = q*(C0-C)-V*ra
    resEB = rho*Cp*q*(T0-T)-dH*V*ra-U*A*(T-Tj)
    res   = [resCB,resEB]
    
    return res
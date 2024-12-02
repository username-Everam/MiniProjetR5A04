import time;
import numpy as np
#Question 2 :

def element_commun1(L1, L2):
    while L1 and L2:
        m1 = min(L1)
        m2 = min(L2)
        if m1 == m2:
            return m1
        elif m1 < m2:
            L1.remove(m1)
        else:
            L2.remove(m2)
    return float('nan')

def chronometre_element_commun1(L1,L2):
    time_debut=time.time()
    element_commun1(L1,L2)
    time_fin=time.time()
    return time_fin-time_debut
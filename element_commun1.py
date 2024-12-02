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
    b=element_commun1(L1,L2)
    time_fin=time.time()
    return time_fin-time_debut,b

def test_element_chrono(n):
    tableau_res=[]
    tableau_reponse=[]
    for i in range(0,n,10):
        Nmax=10000
        liste1 = np.random.randint(Nmax,size=i).tolist()
        liste2 = np.random.randint(Nmax,size=i).tolist()
        temps,reponse=chronometre_element_commun1(liste1,liste2)
        tableau_res.append(temps)
        tableau_reponse.append(reponse)
    return tableau_res,tableau_reponse